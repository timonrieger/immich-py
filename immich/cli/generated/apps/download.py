"""Generated CLI commands for Download tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Download operations")

@app.command("download-archive")
def download_archive(
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Download asset archive"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Retrieve download information"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.download_info_dto import DownloadInfoDto
        download_info_dto = deserialize_request_body(json_data, DownloadInfoDto)
        kwargs['download_info_dto'] = download_info_dto
    client = ctx.obj['client']
    api_group = client.download
    result = run_command(client, api_group, 'get_download_info', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
