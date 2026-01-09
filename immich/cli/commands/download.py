"""Generated CLI commands for Download tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Endpoints for downloading assets or collections of assets.. https://api.immich.app/endpoints/download', context_settings={'help_option_names': ['-h', '--help']})

@app.command("download-archive")
def download_archive(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Download asset archive"""
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if json_str is not None:
        json_data = json.loads(json_str)
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
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Retrieve download information"""
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.download_info_dto import DownloadInfoDto
        download_info_dto = deserialize_request_body(json_data, DownloadInfoDto)
        kwargs['download_info_dto'] = download_info_dto
    client = ctx.obj['client']
    api_group = client.download
    result = run_command(client, api_group, 'get_download_info', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
