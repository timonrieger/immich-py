from __future__ import annotations

from pathlib import Path
from typing import Any, Optional
from uuid import UUID

from pydantic import StrictStr

from immich.client.generated.api.albums_api import AlbumsApi
from immich.client.generated.api.assets_api import AssetsApi
from immich.client.generated.api.server_api import ServerApi
from immich.client.generated.models.asset_media_size import AssetMediaSize
from immich.client.utils.upload import (
    UploadResult,
    UploadStats,
    check_duplicates as check_dupes,
    delete_files,
    scan_files,
    update_albums,
    upload_files,
)
from immich.client.utils.download import download_file, resolve_output_filename
from immich.client.types import HeadersType


class AssetsApiWrapped(AssetsApi):
    """Wrapper for the AssetsApi that provides convenience methods."""

    async def download_asset_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        slug: Optional[StrictStr] = None,
        filename: Optional[str] = None,
        show_progress: bool = False,
        **kwargs: Any,
    ) -> Path:
        """
        Download an asset to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the asset to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the asset can be accessed via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param filename: The filename to use. If not provided, we use the original filename from the headers or default to "orig-" + asset_id.
        :param show_progress: Whether to show a progress bar while downloading.
        :param kwargs: Additional arguments to pass to the `download_asset_without_preload_content` method.

        For exact request/response behavior, inspect `AssetsApi.download_asset_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: Optional[HeadersType]):
            return self.download_asset_without_preload_content(
                id=id,
                key=key,
                slug=slug,
                _headers=kwargs.get("_headers", {}) | (extra_headers or {}),
                **kwargs,
            )

        return await download_file(
            make_request=make_request,
            out_dir=out_dir,
            resolve_filename=lambda headers: resolve_output_filename(
                headers,
                name=filename,
                default_base=f"orig-{id}",
            ),
            show_progress=show_progress,
        )

    async def play_asset_video_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        slug: Optional[StrictStr] = None,
        filename: Optional[str] = None,
        show_progress: bool = False,
        **kwargs: Any,
    ) -> Path:
        """
        Save an asset's video stream to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the video to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the asset can be accessed via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param filename: The filename to use. If not provided, we use the original filename from the headers or default to "video-" + asset_id.
        :param show_progress: Whether to show a progress bar while downloading.
        :param kwargs: Additional arguments to pass to the `play_asset_video_without_preload_content` method.

        For exact request/response behavior, inspect `AssetsApi.play_asset_video_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: Optional[HeadersType]):
            return self.play_asset_video_without_preload_content(
                id=id,
                key=key,
                slug=slug,
                _headers=kwargs.get("_headers", {}) | (extra_headers or {}),
                **kwargs,
            )

        return await download_file(
            make_request=make_request,
            out_dir=out_dir,
            resolve_filename=lambda headers: resolve_output_filename(
                headers,
                name=filename,
                default_base=f"video-{id}",
            ),
            show_progress=show_progress,
        )

    async def view_asset_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        size: Optional[AssetMediaSize] = None,
        slug: Optional[StrictStr] = None,
        filename: Optional[str] = None,
        show_progress: bool = False,
        **kwargs: Any,
    ) -> Path:
        """
        Save an asset's thumbnail to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the asset to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the thumbnail can be fetched via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param size: Thumbnail size.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param filename: The filename to use. If not provided, we use the original filename from the headers or default to "thumb-" + asset_id.
        :param show_progress: Whether to show a progress bar while downloading.
        :param kwargs: Additional arguments to pass to the `view_asset_without_preload_content` method.

        For exact request/response behavior, inspect `AssetsApi.view_asset_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: Optional[HeadersType]):
            return self.view_asset_without_preload_content(
                id=id,
                key=key,
                size=size,
                slug=slug,
                _headers=kwargs.get("_headers", {}) | (extra_headers or {}),
                **kwargs,
            )

        return await download_file(
            make_request=make_request,
            out_dir=out_dir,
            resolve_filename=lambda headers: resolve_output_filename(
                headers,
                name=filename,
                default_base=f"thumb-{id}",
            ),
            show_progress=show_progress,
        )

    async def upload(
        self,
        paths: Path | list[Path] | str | list[str],
        *,
        ignore_pattern: Optional[str] = None,
        include_hidden: bool = False,
        skip_duplicates: bool = False,
        concurrency: int = 5,
        show_progress: bool = False,
        album_name: Optional[str] = None,
        delete_uploads: bool = False,
        delete_duplicates: bool = False,
        dry_run: bool = False,
    ) -> UploadResult:
        """
        Upload assets with smart features (duplicate detection, album management, sidecar support, dry run).

        :param paths: File or directory paths to upload. Can be a single path or list of paths. Directories are automatically walked recursively. To ignore subdirectories, use the `ignore_pattern` parameter.
        :param ignore_pattern: Wildcard pattern to ignore files (uses `fnmatch` stdlib module, not regex). Examples: "*.tmp" (ignore all .tmp files), "*/subdir/*" (ignore files in subdir at any level).
        :param include_hidden: Whether to include hidden files (starting with ".").
        :param skip_duplicates: Whether to skip duplicate checking (might still get rejected on the server).
        :param concurrency: Number of concurrent uploads. Defaults to 5. A higher number may increase upload speed, but also increases the risk of rate limiting or other issues.
        :param show_progress: Whether to show progress bars.
        :param album_name: Album name to create or use. If None, no album operations are performed.
        :param delete_uploads: Whether to delete successfully uploaded files locally.
        :param delete_duplicates: Whether to delete duplicate files locally.
        :param dry_run: Simulate uploads without actually uploading.

        :return: UploadResult with uploaded assets, rejected files, failures, and statistics.
        """
        if concurrency < 1:
            raise ValueError("concurrency must be >= 1")
        server_api = ServerApi(self.api_client)
        albums_api = AlbumsApi(self.api_client)

        _paths = [paths] if isinstance(paths, (str, Path)) else paths
        _paths = [Path(p) for p in _paths]

        files = await scan_files(_paths, server_api, ignore_pattern, include_hidden)
        if not files:
            return UploadResult(
                uploaded=[],
                rejected=[],
                failed=[],
                stats=UploadStats(total=0, uploaded=0, rejected=0, failed=0),
            )

        new_files, checked_rejected = await check_dupes(
            files=files,
            assets_api=self,
            skip_duplicates=skip_duplicates,
            show_progress=show_progress,
            dry_run=dry_run,
        )

        uploaded, actual_rejected, failed = await upload_files(
            files=new_files,
            assets_api=self,
            concurrency=concurrency,
            show_progress=show_progress,
            dry_run=dry_run,
        )

        if album_name and not dry_run:
            await update_albums(
                uploaded=uploaded, album_name=album_name, albums_api=albums_api
            )

        # we can either check pre-upload rejected files or on-upload rejected files, so we return the appropriate list
        # alternative would be to use both lists and deduplicate by asset_id, however adds overhead and assumes the API returned different results
        rejected = actual_rejected if skip_duplicates else checked_rejected

        await delete_files(
            uploaded=uploaded,
            rejected=rejected,
            delete_uploads=delete_uploads,
            delete_duplicates=delete_duplicates,
            dry_run=dry_run,
        )

        return UploadResult(
            uploaded=uploaded,
            rejected=rejected,
            failed=failed,
            stats=UploadStats(
                total=len(files),
                uploaded=len(uploaded),
                rejected=len(rejected),
                failed=len(failed),
            ),
        )
