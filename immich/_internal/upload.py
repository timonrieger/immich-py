from __future__ import annotations

import asyncio
import fnmatch
import hashlib
import json
import logging
import os
import sys
from statx import statx
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal, Optional, cast
from uuid import UUID
import uuid

from pydantic import BaseModel, Field
import tqdm
from immich.client.api.albums_api import AlbumsApi
from immich.client.api.assets_api import AssetsApi
from immich.client.api.server_api import ServerApi
from immich.client.api_response import ApiResponse
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
    rejected: int
    failed: int


_REJECTED_REASONS = Literal["duplicate", "unsupported_format"]


class RejectedEntry(BaseModel):
    """Represents a file that was rejected during upload (check)."""

    filepath: Path = Field(
        ..., description="The path to the local file that was rejected."
    )
    asset_id: Optional[str] = Field(
        None, description="The ID of the asset. Set if reason is 'duplicate'."
    )
    reason: Optional[_REJECTED_REASONS] = Field(
        None, description="The reason for the rejection."
    )


class FailedEntry(BaseModel):
    """Represents a file that failed to upload."""

    filepath: Path = Field(
        ..., description="The path to the local file that failed to upload."
    )
    error: str = Field(..., description="The error message from the server.")


class UploadedEntry(BaseModel):
    """Represents a successfully uploaded file."""

    asset: AssetMediaResponseDto = Field(
        ..., description="The asset that was uploaded."
    )
    filepath: Path = Field(
        ..., description="The path to the local file that was uploaded."
    )


class UploadResult(BaseModel):
    """The result of an upload operation containing all uploaded, rejected, and failed entries."""

    uploaded: list[UploadedEntry] = Field(
        ..., description="The assets that were uploaded."
    )
    rejected: list[RejectedEntry] = Field(
        ..., description="The files that were rejected."
    )
    failed: list[FailedEntry] = Field(
        ..., description="The files that failed to upload."
    )
    stats: UploadStats = Field(..., description="The statistics of the upload.")


async def scan_files(
    paths: list[Path],
    server_api: ServerApi,
    ignore_pattern: Optional[str] = None,
    include_hidden: bool = False,
) -> list[Path]:
    """Scan paths for supported media files.

    :param paths: List of file or directory paths to scan.
    :param server_api: Server API instance to query supported media types.
    :param ignore_pattern: Optional glob pattern to ignore matching files.
    :param include_hidden: Whether to include hidden files (starting with .).

    :return: Sorted list of unique file paths that match supported media types.
    """
    media_types = await server_api.get_supported_media_types()
    extensions = set(media_types.image + media_types.video)

    files: list[Path] = []
    for path in paths:
        path = path.resolve()
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
                if not include_hidden and any(
                    part.startswith(".") for part in file_path.parts
                ):
                    continue
                if ignore_pattern and fnmatch.fnmatch(
                    str(file_path), f"*{ignore_pattern}"
                ):
                    continue
                files.append(file_path)
    return sorted(set(files))


def compute_sha1_sync(filepath: Path) -> str:
    """Compute SHA1 hash of a file synchronously.

    :param filepath: Path to the file to hash.

    :return: Hexadecimal SHA1 digest string.
    """
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
) -> tuple[list[Path], list[RejectedEntry]]:
    """Check which files are duplicates on the server.

    :param files: List of file paths to check.
    :param assets_api: Assets API instance for duplicate checking.
    :param check_duplicates: Whether to perform duplicate checking (if False, returns all files as new).
    :param show_progress: Whether to show progress bars.

    :return: Tuple of (new_files, rejected_entries) where new_files can be uploaded and rejected_entries are duplicates.
    """
    if not check_duplicates:
        return files, []

    pbar = tqdm.tqdm(total=len(files), desc="Hashing files", disable=not show_progress)
    checksums: list[tuple[Path, str]] = []
    for filepath in files:
        checksum = await asyncio.to_thread(compute_sha1_sync, filepath)
        checksums.append((filepath, checksum))
        pbar.update(1)
    pbar.close()

    new_files: list[Path] = []
    rejected: list[RejectedEntry] = []

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
            elif result.action == "reject":
                rejected.append(
                    RejectedEntry(
                        filepath=filepath,
                        asset_id=result.asset_id,
                        reason=cast(Optional[_REJECTED_REASONS], result.reason),
                    )
                )
            else:
                logger.warning(
                    f"Check upload result returned unexpected action {result.action} for {filepath}"
                )

        check_pbar.update(len(batch))
    check_pbar.close()

    return new_files, rejected


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


def get_file_times(path: Path, stats: os.stat_result) -> tuple[datetime, datetime]:
    """Get file creation and modification times reliably.

    Credits: https://stackoverflow.com/a/39501288

    :param path: The path to the file (used for statx fallback on Linux).
    :param stats: The stat result from os.stat() or Path.stat().

    :return: Tuple of (creation_time, modification_time) as UTC-aware datetimes.
    """
    mtime = stats.st_mtime

    try:
        ctime = stats.st_birthtime
    except AttributeError:
        if sys.platform == "win32":
            ctime = stats.st_ctime
        else:
            ctime = statx(path).btime

    return datetime.fromtimestamp(
        ctime or mtime, tz=timezone.utc
    ), datetime.fromtimestamp(mtime, tz=timezone.utc)


async def upload_file(
    filepath: Path,
    assets_api: AssetsApi,
    include_sidecars: bool = True,
    dry_run: bool = False,
) -> ApiResponse[AssetMediaResponseDto]:
    """Upload a single asset file to the server.

    :param filepath: Path to the file to upload.
    :param assets_api: Assets API instance for upload.
    :param include_sidecars: Whether to include XMP sidecar files if found.
    :param dry_run: If True, return mock response without actual upload.

    :return: API response containing the uploaded asset metadata.
    """
    if dry_run:
        mock_data = AssetMediaResponseDto(
            id=str(uuid.uuid4()), status=AssetMediaStatus.CREATED
        )
        return ApiResponse(
            status_code=201,
            headers=None,
            data=mock_data,
            raw_data=b"",
        )

    stats = filepath.stat()

    sidecar_data: Optional[str] = None
    if include_sidecars:
        sidecar_path = find_sidecar(filepath)
        if sidecar_path:
            sidecar_data = str(sidecar_path)

    asset_data = str(filepath)

    file_created_at, file_modified_at = get_file_times(filepath, stats)

    response = await assets_api.upload_asset_with_http_info(
        asset_data=asset_data,
        device_asset_id=f"{filepath.name}-{stats.st_size}".replace(" ", ""),
        device_id="immich-python-client",
        file_created_at=file_created_at,
        file_modified_at=file_modified_at,
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
) -> tuple[list[UploadedEntry], list[RejectedEntry], list[FailedEntry]]:
    """Upload multiple asset files concurrently.

    :param files: List of file paths to upload.
    :param assets_api: Assets API instance for upload.
    :param concurrency: Maximum number of concurrent uploads.
    :param show_progress: Whether to show upload progress bar.
    :param include_sidecars: Whether to include XMP sidecar files if found.
    :param dry_run: If True, simulate uploads without actual API calls.

    :return: Tuple of (uploaded_entries, rejected_entries, failed_entries).
    """
    if not files:
        return [], [], []

    total_size = sum(f.stat().st_size for f in files)
    pbar = tqdm.tqdm(
        total=total_size,
        unit="B",
        unit_scale=True,
        desc="Uploading assets",
        disable=not show_progress,
    )

    semaphore = asyncio.Semaphore(concurrency)
    uploaded: list[UploadedEntry] = []
    rejected: list[RejectedEntry] = []
    failed: list[FailedEntry] = []

    async def upload_with_semaphore(filepath: Path) -> None:
        async with semaphore:
            try:
                response = await upload_file(
                    filepath, assets_api, include_sidecars, dry_run
                )
                if response.status_code == 201:
                    uploaded.append(
                        UploadedEntry(asset=response.data, filepath=filepath)
                    )
                elif response.status_code == 200:
                    rejected.append(
                        RejectedEntry(
                            filepath=filepath,
                            asset_id=response.data.id,
                            reason="duplicate",
                        )
                    )
                else:
                    failed.append(
                        FailedEntry(
                            filepath=filepath,
                            error=f"Unexpected status_code={response.status_code}",
                        )
                    )
                if not dry_run:
                    pbar.update(filepath.stat().st_size)
            except ApiException as e:
                msg = str(e)
                if e.body:
                    try:
                        body = json.loads(cast(str, e.body))
                        msg = str(body.get("message", msg))
                    except Exception:  # nosec: B110
                        pass
                failed.append(FailedEntry(filepath=filepath, error=msg))
                logger.exception("Failed to upload %s: %s", filepath, msg)
            except Exception as e:
                msg = str(e)
                failed.append(FailedEntry(filepath=filepath, error=msg))
                logger.exception("Failed to upload %s: %s", filepath, msg)

    await asyncio.gather(*[upload_with_semaphore(f) for f in files])
    pbar.close()

    return uploaded, rejected, failed


async def update_albums(
    uploaded: list[UploadedEntry],
    album_name: Optional[str],
    albums_api: AlbumsApi,
) -> None:
    """Add uploaded assets to an album, creating the album if needed.

    :param uploaded: List of successfully uploaded entries.
    :param album_name: Name of the album to add assets to (if None, no action).
    :param albums_api: Albums API instance.

    :return: None
    """
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
    asset_ids = [UUID(str(entry.asset.id)) for entry in uploaded]

    for i in range(0, len(asset_ids), 1000):
        batch = asset_ids[i : i + 1000]
        await albums_api.add_assets_to_album(
            id=UUID(str(album_id)), bulk_ids_dto=BulkIdsDto(ids=batch)
        )


async def delete_files(
    uploaded: list[UploadedEntry],
    rejected: list[RejectedEntry],
    delete_after_upload: bool = False,
    delete_duplicates: bool = False,
    include_sidecars: bool = True,
    dry_run: bool = False,
) -> None:
    """Delete local files after upload or if they are duplicates.

    :param uploaded: List of successfully uploaded entries.
    :param rejected: List of rejected entries (e.g., duplicates).
    :param delete_after_upload: Whether to delete files that were successfully uploaded.
    :param delete_duplicates: Whether to delete files that were rejected as duplicates.
    :param include_sidecars: Whether to also delete sidecar files (.xmp).
    :param dry_run: If True, log deletions without actually deleting files.

    :return: None
    """
    to_delete: list[Path] = []
    if delete_after_upload:
        for _ in uploaded:
            to_delete.append(_.filepath)

    if delete_duplicates:
        for _ in rejected:
            # mypy false positive
            if _.reason == "duplicate":  # type: ignore[attr-defined]
                to_delete.append(_.filepath)

    for filepath in to_delete:
        main_deleted = True
        if dry_run:
            logger.info(f"Would have deleted {filepath}")
        else:
            try:
                filepath.unlink()
            except Exception:
                main_deleted = False
                logger.exception(f"Failed to delete {filepath}")

        if include_sidecars and main_deleted:
            sidecar_path = find_sidecar(filepath)
            if sidecar_path:
                if dry_run:
                    logger.info(f"Would have deleted {sidecar_path}")
                else:
                    try:
                        sidecar_path.unlink()
                    except Exception:
                        logger.exception(f"Failed to delete sidecar {sidecar_path}")
