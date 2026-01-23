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
from typing import Optional, cast
from uuid import UUID
import uuid

from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)
from immich.client.consts import DEVICE_ID
from immich.client.types import (
    RejectedEntry,
    FailedEntry,
    UploadedEntry,
    RejectionReason,
)
from immich.client.generated.api.albums_api import AlbumsApi
from immich.client.generated.api.assets_api import AssetsApi
from immich.client.generated.api.server_api import ServerApi
from immich.client.generated.api_response import ApiResponse
from immich.client.generated.models.asset_bulk_upload_check_dto import (
    AssetBulkUploadCheckDto,
)
from immich.client.generated.models.asset_bulk_upload_check_item import (
    AssetBulkUploadCheckItem,
)
from immich.client.generated.models.asset_media_response_dto import (
    AssetMediaResponseDto,
)
from immich.client.generated.models.asset_media_status import AssetMediaStatus
from immich.client.generated.models.bulk_ids_dto import BulkIdsDto
from immich.client.generated.models.create_album_dto import CreateAlbumDto
from immich.client.generated.exceptions import ApiException

logger = logging.getLogger(__name__)

BATCH_SIZE = 5000


def get_device_asset_id(filepath: Path, stats: os.stat_result) -> str:
    """Get the device asset ID for a given file path and stats.

    :param filepath: The path to the file.
    :param stats: The stats of the file.

    :return: The device asset ID.
    """
    return f"{filepath.name}-{stats.st_size}".replace(" ", "")


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
            if not include_hidden and any(part.startswith(".") for part in path.parts):
                continue
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


def compute_sha1_sync(filepath: Path) -> str:  # pragma: no cover
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
    skip_duplicates: bool = False,
    show_progress: bool = False,
    dry_run: bool = False,
) -> tuple[list[Path], list[RejectedEntry]]:
    """Check which files are duplicates on the server.

    :param files: List of file paths to check.
    :param assets_api: Assets API instance for duplicate checking.
    :param skip_duplicates: Whether to skip duplicate checking (might still get rejected on the server).
    :param show_progress: Whether to show progress bars.
    :param dry_run: Whether to run in dry run mode (no actual API calls).

    :return: Tuple of (new_files, rejected_entries) where new_files can be uploaded and rejected_entries are duplicates.
    """
    if skip_duplicates or dry_run:
        return files, []

    progress_columns = [
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ]

    with Progress(*progress_columns, disable=not show_progress) as progress:
        hashing_task = progress.add_task("[cyan]Hashing files", total=len(files))
        checksums: list[tuple[Path, str]] = []
        for filepath in files:
            checksum = await asyncio.to_thread(compute_sha1_sync, filepath)
            checksums.append((filepath, checksum))
            progress.update(hashing_task, advance=1)

        new_files: list[Path] = []
        rejected: list[RejectedEntry] = []

        check_task = progress.add_task("[cyan]Checking duplicates", total=len(files))

        for i in range(0, len(checksums), BATCH_SIZE):
            batch = checksums[i : i + BATCH_SIZE]
            items = [
                AssetBulkUploadCheckItem(id=str(filepath), checksum=checksum)
                for filepath, checksum in batch
            ]
            dto = AssetBulkUploadCheckDto(assets=items)
            response = await assets_api.check_bulk_upload(
                asset_bulk_upload_check_dto=dto
            )

            for result in response.results:
                filepath = Path(result.id)
                if result.action == "accept":
                    new_files.append(filepath)
                elif result.action == "reject":
                    rejected.append(
                        RejectedEntry(
                            filepath=filepath,
                            asset_id=result.asset_id,
                            reason=cast(Optional[RejectionReason], result.reason),
                        )
                    )
                else:
                    logger.warning(
                        f"Check upload result returned unexpected action {result.action} for {filepath}"
                    )

            progress.update(check_task, advance=len(batch))

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


def get_file_times(
    path: Path, stats: os.stat_result
) -> tuple[datetime, datetime]:  # pragma: no cover
    """Get file creation and modification times reliably.

    Credits: https://stackoverflow.com/a/39501288

    :param path: The path to the file (used for statx fallback on Linux).
    :param stats: The stat result from os.stat() or Path.stat().

    :return: Tuple of (creation_time, modification_time) as UTC-aware datetimes.
    """
    mtime = stats.st_mtime

    try:
        # not available on all platforms and python versions, thus the AttributeError guard and type ignore
        # ty says to remove the type ignore, however in the ci the lint would raise an error
        ctime = stats.st_birthtime  # type: ignore[unresolved-attribute]
    except AttributeError:
        if sys.platform == "win32":
            ctime = stats.st_ctime
        else:
            ctime = statx(os.fspath(path)).btime

    return datetime.fromtimestamp(
        ctime or mtime, tz=timezone.utc
    ), datetime.fromtimestamp(mtime, tz=timezone.utc)


async def upload_file(
    filepath: Path,
    assets_api: AssetsApi,
    dry_run: bool = False,
) -> ApiResponse[AssetMediaResponseDto]:
    """Upload a single asset file to the server.

    :param filepath: Path to the file to upload.
    :param assets_api: Assets API instance for upload.
    :param dry_run: Return mock response without actual upload.

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
    sidecar_path = find_sidecar(filepath)
    if sidecar_path:
        sidecar_data = str(sidecar_path)

    asset_data = str(filepath)

    file_created_at, file_modified_at = get_file_times(filepath, stats)

    response = await assets_api.upload_asset_with_http_info(
        asset_data=asset_data,
        device_asset_id=get_device_asset_id(filepath, stats),
        device_id=DEVICE_ID,
        file_created_at=file_created_at,
        file_modified_at=file_modified_at,
        sidecar_data=sidecar_data,
    )
    return response


async def upload_files(
    files: list[Path],
    assets_api: AssetsApi,
    concurrency: int = 5,
    show_progress: bool = False,
    dry_run: bool = False,
) -> tuple[list[UploadedEntry], list[RejectedEntry], list[FailedEntry]]:
    """Upload multiple asset files concurrently.

    :param files: List of file paths to upload.
    :param assets_api: Assets API instance for upload.
    :param concurrency: Maximum number of concurrent uploads.
    :param show_progress: Whether to show upload progress bar.
    :param dry_run: Simulate uploads without actual API calls.

    :return: Tuple of (uploaded_entries, rejected_entries, failed_entries).
    """
    if not files:
        return [], [], []

    total_size = sum(f.stat().st_size for f in files)
    progress_columns = [
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
    ]

    semaphore = asyncio.Semaphore(concurrency)
    uploaded: list[UploadedEntry] = []
    rejected: list[RejectedEntry] = []
    failed: list[FailedEntry] = []

    with Progress(*progress_columns, disable=not show_progress) as progress:
        upload_task = progress.add_task("[green]Uploading assets", total=total_size)

        async def upload_with_semaphore(filepath: Path) -> None:
            async with semaphore:
                try:
                    response = await upload_file(filepath, assets_api, dry_run)
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
                        progress.update(upload_task, advance=filepath.stat().st_size)
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
            create_album_dto=CreateAlbumDto(albumName=album_name)
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
    delete_uploads: bool = False,
    delete_duplicates: bool = False,
    dry_run: bool = False,
) -> None:
    """Delete local files after upload or if they are duplicates.

    :param uploaded: List of successfully uploaded entries.
    :param rejected: List of rejected entries (e.g., duplicates).
    :param delete_uploads: Whether to delete files that were successfully uploaded.
    :param delete_duplicates: Whether to delete files that were rejected as duplicates.
    :param dry_run: Log deletions without actually deleting files.

    :return: None
    """
    to_delete: list[Path] = []
    if delete_uploads:
        for _ in uploaded:
            to_delete.append(_.filepath)

    if delete_duplicates:
        for _ in rejected:
            if _.reason == "duplicate":
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

        if main_deleted:
            sidecar_path = find_sidecar(filepath)
            if sidecar_path:
                if dry_run:
                    logger.info(f"Would have deleted {sidecar_path}")
                else:
                    try:
                        sidecar_path.unlink()
                    except Exception:
                        logger.exception(f"Failed to delete sidecar {sidecar_path}")
