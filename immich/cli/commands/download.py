"""Generated CLI commands for Download tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""Endpoints for downloading assets or collections of assets.

Docs: https://api.immich.app/endpoints/download""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("download-archive")
def download_archive(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key", help="""Access key for shared links"""),
    slug: str | None = typer.Option(None, "--slug", help="""Access slug for shared links"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    asset_ids: list[str] = typer.Option(..., "--assetIds", help="""Asset IDs"""),
) -> None:
    """Download asset archive

Docs: https://api.immich.app/endpoints/download/downloadArchive
    """
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([asset_ids])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_ids_dto import AssetIdsDto
        asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
        kwargs['asset_ids_dto'] = asset_ids_dto
    elif any([
        asset_ids,
    ]):
        # Build body from dotted flags
        json_data = {}
        if asset_ids is None:
            raise SystemExit("Error: --assetIds is required")
        set_nested(json_data, ['assetIds'], asset_ids)
        if json_data:
            from immich.client.models.asset_ids_dto import AssetIdsDto
            asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
            kwargs['asset_ids_dto'] = asset_ids_dto
    client = ctx.obj['client']
    api_group = client.download
    result = run_command(client, api_group, 'download_archive', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-download-info")
def get_download_info(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key", help="""Access key for shared links"""),
    slug: str | None = typer.Option(None, "--slug", help="""Access slug for shared links"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    album_id: str | None = typer.Option(None, "--albumId", help="""Album ID to download"""),
    archive_size: int | None = typer.Option(None, "--archiveSize", help="""Archive size limit in bytes"""),
    asset_ids: list[str] | None = typer.Option(None, "--assetIds", help="""Asset IDs to download"""),
    user_id: str | None = typer.Option(None, "--userId", help="""User ID to download assets from"""),
) -> None:
    """Retrieve download information

Docs: https://api.immich.app/endpoints/download/getDownloadInfo
    """
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([album_id, archive_size, asset_ids, user_id])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.download_info_dto import DownloadInfoDto
        download_info_dto = deserialize_request_body(json_data, DownloadInfoDto)
        kwargs['download_info_dto'] = download_info_dto
    elif any([
        album_id,
        archive_size,
        asset_ids,
        user_id,
    ]):
        # Build body from dotted flags
        json_data = {}
        if album_id is not None:
            set_nested(json_data, ['albumId'], album_id)
        if archive_size is not None:
            set_nested(json_data, ['archiveSize'], archive_size)
        if asset_ids is not None:
            set_nested(json_data, ['assetIds'], asset_ids)
        if user_id is not None:
            set_nested(json_data, ['userId'], user_id)
        if json_data:
            from immich.client.models.download_info_dto import DownloadInfoDto
            download_info_dto = deserialize_request_body(json_data, DownloadInfoDto)
            kwargs['download_info_dto'] = download_info_dto
    client = ctx.obj['client']
    api_group = client.download
    result = run_command(client, api_group, 'get_download_info', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
