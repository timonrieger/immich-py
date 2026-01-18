"""Generated CLI commands for Download tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Endpoints for downloading assets or collections of assets.\n\nDocs: https://api.immich.app/endpoints/download"""
)


@app.command("download-archive", deprecated=False)
def download_archive(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Download asset archive

    Docs: https://api.immich.app/endpoints/download/downloadArchive
    """
    kwargs = {}
    json_data = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    set_nested(json_data, ["asset_ids"], asset_ids)
    from immich.client.models.asset_ids_dto import AssetIdsDto

    asset_ids_dto = AssetIdsDto.model_validate(json_data)
    kwargs["asset_ids_dto"] = asset_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.download, "download_archive", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-download-info", deprecated=False)
def get_download_info(
    ctx: typer.Context,
    album_id: str | None = typer.Option(None, "--album-id", help=""""""),
    archive_size: int | None = typer.Option(None, "--archive-size", help="""""", min=1),
    asset_ids: list[str] | None = typer.Option(None, "--asset-ids", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
    user_id: str | None = typer.Option(None, "--user-id", help=""""""),
) -> None:
    """Retrieve download information

    Docs: https://api.immich.app/endpoints/download/getDownloadInfo
    """
    kwargs = {}
    json_data = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    if album_id is not None:
        set_nested(json_data, ["album_id"], album_id)
    if archive_size is not None:
        set_nested(json_data, ["archive_size"], archive_size)
    if asset_ids is not None:
        set_nested(json_data, ["asset_ids"], asset_ids)
    if user_id is not None:
        set_nested(json_data, ["user_id"], user_id)
    from immich.client.models.download_info_dto import DownloadInfoDto

    download_info_dto = DownloadInfoDto.model_validate(json_data)
    kwargs["download_info_dto"] = download_info_dto
    client = ctx.obj["client"]
    result = run_command(client, client.download, "get_download_info", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
