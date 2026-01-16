"""Generated CLI commands for Download tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Endpoints for downloading assets or collections of assets.

Docs: https://api.immich.app/endpoints/download""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("download-archive")
def download_archive(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    asset_ids: list[str] = typer.Option(..., "--assetIds"),
) -> None:
    """Download asset archive

    Docs: https://api.immich.app/endpoints/download/downloadArchive
    """
    kwargs = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    has_flags = any([asset_ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            asset_ids,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["assetIds"], asset_ids)
        from immich.client.models.asset_ids_dto import AssetIdsDto

        asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
        kwargs["asset_ids_dto"] = asset_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.download, "download_archive", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-download-info")
def get_download_info(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    album_id: str | None = typer.Option(None, "--albumId"),
    archive_size: int | None = typer.Option(None, "--archiveSize"),
    asset_ids: list[str] | None = typer.Option(None, "--assetIds"),
    user_id: str | None = typer.Option(None, "--userId"),
) -> None:
    """Retrieve download information

    Docs: https://api.immich.app/endpoints/download/getDownloadInfo
    """
    kwargs = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    has_flags = any([album_id, archive_size, asset_ids, user_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            album_id,
            archive_size,
            asset_ids,
            user_id,
        ]
    ):
        json_data = {}
        if album_id is not None:
            set_nested(json_data, ["albumId"], album_id)
        if archive_size is not None:
            set_nested(json_data, ["archiveSize"], archive_size)
        if asset_ids is not None:
            set_nested(json_data, ["assetIds"], asset_ids)
        if user_id is not None:
            set_nested(json_data, ["userId"], user_id)
        from immich.client.models.download_info_dto import DownloadInfoDto

        download_info_dto = deserialize_request_body(json_data, DownloadInfoDto)
        kwargs["download_info_dto"] = download_info_dto
    client = ctx.obj["client"]
    result = run_command(client, client.download, "get_download_info", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
