from __future__ import annotations

import asyncio
import fnmatch
import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Optional, cast
from uuid import UUID
import uuid

from pydantic import BaseModel
import tqdm
from immich.client.api.albums_api import AlbumsApi
from immich.client.api.assets_api import AssetsApi
from immich.client.api.server_api import ServerApi
from immich.client.models.asset_bulk_upload_check_dto import AssetBulkUploadCheckDto
from immich.client.models.asset_bulk_upload_check_item import AssetBulkUploadCheckItem
from immich.client.models.asset_media_response_dto import AssetMediaResponseDto
from immich.client.models.asset_media_status import AssetMediaStatus
from immich.client.models.bulk_ids_dto import BulkIdsDto
from immich.client.models.create_album_dto import CreateAlbumDto
from immich.client.exceptions import ApiException

logger = logging.getLogger(__name__)

BATCH_SIZE = 5000


class UploadStats(BaseModel):
    total: int
    uploaded: int
    duplicates: int
    failed: int


class UploadResult(BaseModel):
    uploaded: list[AssetMediaResponseDto]
    duplicates: list[tuple[Path, str]]
    failed: list[tuple[Path, str]]
    stats: UploadStats


async def scan_files(
    paths: Path | list[Path] | str | list[str],
    server_api: ServerApi,
    ignore_pattern: Optional[str] = None,
    include_hidden: bool = False,
) -> list[Path]:
    if isinstance(paths, (str, Path)):
        paths = [paths]
    paths = [Path(p) for p in paths]

    media_types = await server_api.get_supported_media_types()
    extensions = set(media_types.image + media_types.video)

    files: list[Path] = []
    for path in paths:
        path = Path(path).resolve()
        if path.is_file():
            if path.suffix.lower() in extensions:
                if ignore_pattern and fnmatch.fnmatch(str(path), f"*{ignore_pattern}"):
                    continue
                files.append(path)
        elif path.is_dir():
            for file_path in path.rglob("*"):
                if not file_path.is_file():
                    continue
                if file_path.suffix.lower() not in extensions:
                    continue
                if not include_hidden and file_path.name.startswith("."):
                    continue
                if ignore_pattern and fnmatch.fnmatch(
                    str(file_path), f"*{ignore_pattern}"
                ):
                    continue
                files.append(file_path)
    return sorted(set(files))


async def compute_sha1(filepath: Path) -> str:
    sha1 = hashlib.sha1(usedforsecurity=False)
    with open(filepath, "rb") as f:
        while chunk := f.read(1024 * 1024):
            sha1.update(chunk)
    return sha1.hexdigest()


async def check_duplicates(
    files: list[Path],
    assets_api: AssetsApi,
    check_duplicates: bool = True,
    show_progress: bool = True,
) -> tuple[list[Path], list[tuple[Path, str]]]:
    if not check_duplicates:
        return files, []

    pbar = tqdm.tqdm(total=len(files), desc="Hashing files", disable=not show_progress)
    checksums: list[tuple[Path, str]] = []
    for filepath in files:
        checksum = await compute_sha1(filepath)
        checksums.append((filepath, checksum))
        pbar.update(1)
    pbar.close()

    new_files: list[Path] = []
    duplicates: list[tuple[Path, str]] = []

    check_pbar = tqdm.tqdm(
        total=len(files), desc="Checking duplicates", disable=not show_progress
    )

    for i in range(0, len(checksums), BATCH_SIZE):
        batch = checksums[i : i + BATCH_SIZE]
        items = [
            AssetBulkUploadCheckItem(id=str(filepath), checksum=checksum)
            for filepath, checksum in batch
        ]
        dto = AssetBulkUploadCheckDto(assets=items)
        response = await assets_api.check_bulk_upload(asset_bulk_upload_check_dto=dto)

        for result in response.results:
            filepath = Path(result.id)
            if result.action == "accept":
                new_files.append(filepath)
            else:
                # TODO: pass reason to caller (https://api.immich.app/models/AssetBulkUploadCheckResult)
                # e.g. is_trashed, unsupported_format, duplicate
                duplicates.append((filepath, result.asset_id or ""))

        check_pbar.update(len(batch))
    check_pbar.close()

    return new_files, duplicates


def find_sidecar(filepath: Path) -> Optional[Path]:
    """Find sidecar file for a given media file path.

    Checks both naming conventions:
    - {filename}.xmp (e.g., photo.xmp for photo.jpg)
    - {filename}.{ext}.xmp (e.g., photo.jpg.xmp for photo.jpg)

    :param filepath: The path to the media file.

    :return: The path to the first sidecar file that exists, or None if neither exists.
    """
    no_ext = filepath.parent / filepath.stem
    for sidecar_path in [
        no_ext.with_suffix(".xmp"),
        filepath.with_suffix(filepath.suffix + ".xmp"),
    ]:
        if sidecar_path.exists():
            return sidecar_path
    return None


async def upload_file(
    filepath: Path,
    assets_api: AssetsApi,
    include_sidecars: bool = True,
    dry_run: bool = False,
) -> AssetMediaResponseDto:
    if dry_run:
        return AssetMediaResponseDto(
            id=str(uuid.uuid4()), status=AssetMediaStatus.CREATED
        )

    stats = filepath.stat()

    sidecar_data: Optional[str] = None
    if include_sidecars:
        sidecar_path = find_sidecar(filepath)
        if sidecar_path:
            sidecar_data = str(sidecar_path)

    asset_data = str(filepath)

    response = await assets_api.upload_asset(
        asset_data=asset_data,
        device_asset_id=f"{filepath.name}-{stats.st_size}".replace(" ", ""),
        device_id="immich-python-client",
        file_created_at=datetime.fromtimestamp(stats.st_ctime),
        file_modified_at=datetime.fromtimestamp(stats.st_mtime),
        metadata=[],
        sidecar_data=sidecar_data,
    )
    return response


async def upload_files(
    files: list[Path],
    assets_api: AssetsApi,
    concurrency: int = 5,
    show_progress: bool = True,
    include_sidecars: bool = True,
    dry_run: bool = False,
) -> tuple[list[tuple[AssetMediaResponseDto, Path]], list[tuple[Path, str]]]:
    if not files:
        return [], []

    total_size = sum(f.stat().st_size for f in files)
    pbar = tqdm.tqdm(
        total=total_size,
        unit="B",
        unit_scale=True,
        desc="Uploading assets",
        disable=not show_progress,
    )

    semaphore = asyncio.Semaphore(concurrency)
    uploaded: list[tuple[AssetMediaResponseDto, Path]] = []
    failed: list[tuple[Path, str]] = []

    async def upload_with_semaphore(filepath: Path) -> None:
        async with semaphore:
            try:
                response = await upload_file(
                    filepath, assets_api, include_sidecars, dry_run
                )
                uploaded.append((response, filepath))
                if not dry_run:
                    pbar.update(filepath.stat().st_size)
            except Exception as e:
                if isinstance(e, ApiException) and e.body:
                    body: dict[str, Any] = json.loads(cast(str, e.body))
                    msg = body.get("message", str(e))
                else:
                    msg = str(e)
                failed.append((filepath, msg))
                logger.exception(f"Failed to upload {filepath}: {msg}")

    await asyncio.gather(*[upload_with_semaphore(f) for f in files])
    pbar.close()

    return uploaded, failed


async def update_albums(
    uploaded: list[tuple[AssetMediaResponseDto, Path]],
    album_name: Optional[str],
    albums_api: AlbumsApi,
) -> None:
    if not album_name or not uploaded:
        return

    all_albums = await albums_api.get_all_albums()
    album_map = {album.album_name: album.id for album in all_albums}

    if album_name not in album_map:
        album = await albums_api.create_album(
            create_album_dto=CreateAlbumDto(album_name=album_name)
        )
        album_map[album_name] = album.id

    album_id = album_map[album_name]
    asset_ids = [UUID(asset.id) for asset, _ in uploaded]

    for i in range(0, len(asset_ids), 1000):
        batch = asset_ids[i : i + 1000]
        await albums_api.add_assets_to_album(
            id=album_id, bulk_ids_dto=BulkIdsDto(ids=batch)
        )


async def delete_files(
    uploaded: list[tuple[AssetMediaResponseDto, Path]],
    duplicates: list[tuple[Path, str]],
    delete_after_upload: bool = False,
    delete_duplicates: bool = False,
    include_sidecars: bool = True,
    dry_run: bool = False,
) -> None:
    to_delete: list[Path] = []
    if delete_after_upload:
        for _, filepath in uploaded:
            to_delete.append(filepath)

    if delete_duplicates:
        for filepath, _ in duplicates:
            to_delete.append(filepath)

    for filepath in to_delete:
        main_deleted = True
        if dry_run:
            logger.info(f"Would have deleted {filepath}")
        else:
            try:
                filepath.unlink()
            except Exception as e:
                main_deleted = False
                logger.exception(f"Failed to delete {filepath}: {e}")

        if include_sidecars and main_deleted:
            sidecar_path = find_sidecar(filepath)
            if sidecar_path:
                if dry_run:
                    logger.info(f"Would have deleted {sidecar_path}")
                else:
                    try:
                        sidecar_path.unlink()
                    except Exception as e:
                        logger.exception(f"Failed to delete {sidecar_path}: {e}")
