from __future__ import annotations

from uuid import UUID, uuid4
from pathlib import Path
from typing import Any, Optional

from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)
from pydantic import StrictStr

from immich.client.generated.api.download_api import DownloadApi
from immich.client.generated.models.asset_ids_dto import AssetIdsDto
from immich.client.generated.models.download_info_dto import DownloadInfoDto
from immich.client.utils.download import download_file
from immich.client.types import HeadersType


class DownloadApiWrapped(DownloadApi):
    """Wrapper for the DownloadApi that provides convenience methods."""

    async def download_archive_to_file(
        self,
        download_info: DownloadInfoDto,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        slug: Optional[StrictStr] = None,
        show_progress: bool = False,
        **kwargs: Any,
    ) -> list[Path]:
        """
        Download one or more asset archives and save them to ZIP files.

        Note: This method intentionally downloads archives **sequentially** (not in parallel) by default.
        Immich has to build ZIP archives server-side; parallelizing many archive requests can put significant
        CPU/disk load on the Immich server and may lead to timeouts or degraded performance for other users.
        If you choose to parallelize, keep concurrency low and do so at your own risk.

        :param download_info: The download info (two-step flow; downloads all archives returned by `get_download_info`).
        :param out_dir: The directory to write the ZIP archive to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). Allows access without authentication. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param show_progress: Whether to show progress bars (per-archive bytes + overall archive count).
        :param kwargs: Additional arguments to pass to the underlying SDK calls.

        :return: The list of paths to the downloaded archives.

        For exact request/response behavior, inspect `DownloadApi.download_archive_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        # Normalize to a list of archive requests.
        info = await super().get_download_info(
            download_info, key=key, slug=slug, **kwargs
        )
        archive_requests: list[tuple[AssetIdsDto, int]] = [
            (
                AssetIdsDto(
                    assetIds=[UUID(str(asset_id)) for asset_id in archive.asset_ids]
                ),
                int(archive.size),
            )
            for archive in info.archives
        ]

        out_paths: list[Path] = []

        progress_columns = [
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
        ]

        with Progress(*progress_columns, disable=not show_progress) as progress:
            archives_task = progress.add_task(
                f"[cyan]Downloading {len(archive_requests)} archives",
                total=len(archive_requests),
            )
            for asset_ids_dto, expected_size in archive_requests:
                filename = f"archive-{uuid4()}.zip"

                def make_request(extra_headers: Optional[HeadersType]):
                    return self.download_archive_without_preload_content(
                        asset_ids_dto=asset_ids_dto,
                        key=key,
                        slug=slug,
                        _headers=kwargs.get("_headers", {}) | (extra_headers or {}),
                        **kwargs,
                    )

                download_task = progress.add_task(
                    f"[green]{filename}",
                    total=expected_size or None,
                )
                await download_file(
                    make_request=make_request,
                    out_dir=out_dir,
                    resolve_filename=lambda headers: filename,
                    show_progress=show_progress,
                    progress=progress,
                    task_id=download_task,
                    resumeable=False,  # zip files are not resumable
                )
                out_paths.append(out_dir / filename)
                progress.update(archives_task, advance=1)

        return out_paths
