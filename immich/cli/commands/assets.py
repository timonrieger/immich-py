"""Generated CLI commands for Assets tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
import json
from datetime import datetime
from pathlib import Path
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""An asset is an image or video that has been uploaded to Immich.\n\n[link=https://api.immich.app/endpoints/assets]Immich API documentation[/link]"""
)


@app.command("check-bulk-upload", deprecated=False, rich_help_panel="API commands")
def check_bulk_upload(
    ctx: typer.Context,
    assets: list[str] = typer.Option(..., "--assets", help="""As a JSON string"""),
) -> None:
    """Check bulk upload

    [link=https://api.immich.app/endpoints/assets/checkBulkUpload]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_assets = [json.loads(i) for i in assets]
    set_nested(json_data, ["assets"], value_assets)
    asset_bulk_upload_check_dto = AssetBulkUploadCheckDto.model_validate(json_data)
    kwargs["asset_bulk_upload_check_dto"] = asset_bulk_upload_check_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "check_bulk_upload", ctx, **kwargs)
    print_response(result, ctx)


@app.command("check-existing-assets", deprecated=False, rich_help_panel="API commands")
def check_existing_assets(
    ctx: typer.Context,
    device_asset_ids: list[str] = typer.Option(..., "--device-asset-ids", help=""""""),
    device_id: str = typer.Option(..., "--device-id", help=""""""),
) -> None:
    """Check existing assets

    [link=https://api.immich.app/endpoints/assets/checkExistingAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["device_asset_ids"], device_asset_ids)
    set_nested(json_data, ["device_id"], device_id)
    check_existing_assets_dto = CheckExistingAssetsDto.model_validate(json_data)
    kwargs["check_existing_assets_dto"] = check_existing_assets_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "check_existing_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("copy-asset", deprecated=False, rich_help_panel="API commands")
def copy_asset(
    ctx: typer.Context,
    albums: Literal["true", "false"] | None = typer.Option(
        None, "--albums", help=""""""
    ),
    favorite: Literal["true", "false"] | None = typer.Option(
        None, "--favorite", help=""""""
    ),
    shared_links: Literal["true", "false"] | None = typer.Option(
        None, "--shared-links", help=""""""
    ),
    sidecar: Literal["true", "false"] | None = typer.Option(
        None, "--sidecar", help=""""""
    ),
    source_id: str = typer.Option(..., "--source-id", help=""""""),
    stack: Literal["true", "false"] | None = typer.Option(None, "--stack", help=""""""),
    target_id: str = typer.Option(..., "--target-id", help=""""""),
) -> None:
    """Copy asset

    [link=https://api.immich.app/endpoints/assets/copyAsset]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if albums is not None:
        set_nested(json_data, ["albums"], albums.lower() == "true")
    if favorite is not None:
        set_nested(json_data, ["favorite"], favorite.lower() == "true")
    if shared_links is not None:
        set_nested(json_data, ["shared_links"], shared_links.lower() == "true")
    if sidecar is not None:
        set_nested(json_data, ["sidecar"], sidecar.lower() == "true")
    set_nested(json_data, ["source_id"], source_id)
    if stack is not None:
        set_nested(json_data, ["stack"], stack.lower() == "true")
    set_nested(json_data, ["target_id"], target_id)
    asset_copy_dto = AssetCopyDto.model_validate(json_data)
    kwargs["asset_copy_dto"] = asset_copy_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "copy_asset", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-asset-metadata", deprecated=False, rich_help_panel="API commands")
def delete_asset_metadata(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    key: AssetMetadataKey = typer.Argument(..., help=""""""),
) -> None:
    """Delete asset metadata by key

    [link=https://api.immich.app/endpoints/assets/deleteAssetMetadata]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["key"] = key
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "delete_asset_metadata", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-assets", deprecated=False, rich_help_panel="API commands")
def delete_assets(
    ctx: typer.Context,
    force: Literal["true", "false"] | None = typer.Option(None, "--force", help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Delete assets

    [link=https://api.immich.app/endpoints/assets/deleteAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if force is not None:
        set_nested(json_data, ["force"], force.lower() == "true")
    set_nested(json_data, ["ids"], ids)
    asset_bulk_delete_dto = AssetBulkDeleteDto.model_validate(json_data)
    kwargs["asset_bulk_delete_dto"] = asset_bulk_delete_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "delete_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("download-asset", deprecated=False, rich_help_panel="API commands")
def download_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Download original asset

    [link=https://api.immich.app/endpoints/assets/downloadAsset]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "download_asset", ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "get-all-user-assets-by-device-id", deprecated=True, rich_help_panel="API commands"
)
def get_all_user_assets_by_device_id(
    ctx: typer.Context,
    device_id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve assets by device ID

    [link=https://api.immich.app/endpoints/assets/getAllUserAssetsByDeviceId]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["device_id"] = device_id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.assets, "get_all_user_assets_by_device_id", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-asset-info", deprecated=False, rich_help_panel="API commands")
def get_asset_info(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Retrieve an asset

    [link=https://api.immich.app/endpoints/assets/getAssetInfo]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_info", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-asset-metadata", deprecated=False, rich_help_panel="API commands")
def get_asset_metadata(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Get asset metadata

    [link=https://api.immich.app/endpoints/assets/getAssetMetadata]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_metadata", ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "get-asset-metadata-by-key", deprecated=False, rich_help_panel="API commands"
)
def get_asset_metadata_by_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    key: AssetMetadataKey = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve asset metadata by key

    [link=https://api.immich.app/endpoints/assets/getAssetMetadataByKey]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["key"] = key
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.assets, "get_asset_metadata_by_key", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-asset-ocr", deprecated=False, rich_help_panel="API commands")
def get_asset_ocr(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve asset OCR data

    [link=https://api.immich.app/endpoints/assets/getAssetOcr]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_ocr", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-asset-statistics", deprecated=False, rich_help_panel="API commands")
def get_asset_statistics(
    ctx: typer.Context,
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=""""""
    ),
    is_trashed: Literal["true", "false"] | None = typer.Option(
        None, "--is-trashed", help=""""""
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help=""""""
    ),
) -> None:
    """Get asset statistics

    [link=https://api.immich.app/endpoints/assets/getAssetStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite.lower() == "true"
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed.lower() == "true"
    if visibility is not None:
        kwargs["visibility"] = visibility
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_statistics", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-random", deprecated=True, rich_help_panel="API commands")
def get_random(
    ctx: typer.Context,
    count: float | None = typer.Option(None, "--count", help="""""", min=1),
) -> None:
    """Get random assets

    [link=https://api.immich.app/endpoints/assets/getRandom]Immich API documentation[/link]
    """
    kwargs = {}
    if count is not None:
        kwargs["count"] = count
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "get_random", ctx, **kwargs)
    print_response(result, ctx)


@app.command("play-asset-video", deprecated=False, rich_help_panel="API commands")
def play_asset_video(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Play asset video

    [link=https://api.immich.app/endpoints/assets/playAssetVideo]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "play_asset_video", ctx, **kwargs)
    print_response(result, ctx)


@app.command("replace-asset", deprecated=True, rich_help_panel="API commands")
def replace_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    asset_data: Path = typer.Option(..., "--asset-data", help="""""", exists=True),
    device_asset_id: str = typer.Option(..., "--device-asset-id", help=""""""),
    device_id: str = typer.Option(..., "--device-id", help=""""""),
    duration: str | None = typer.Option(None, "--duration", help=""""""),
    file_created_at: datetime = typer.Option(..., "--file-created-at", help=""""""),
    file_modified_at: datetime = typer.Option(..., "--file-modified-at", help=""""""),
    filename: str | None = typer.Option(None, "--filename", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Replace asset

    [link=https://api.immich.app/endpoints/assets/replaceAsset]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    kwargs["asset_data"] = (asset_data.name, asset_data.read_bytes())
    set_nested(json_data, ["device_asset_id"], device_asset_id)
    set_nested(json_data, ["device_id"], device_id)
    if duration is not None:
        set_nested(json_data, ["duration"], duration)
    set_nested(json_data, ["file_created_at"], file_created_at)
    set_nested(json_data, ["file_modified_at"], file_modified_at)
    if filename is not None:
        set_nested(json_data, ["filename"], filename)
    kwargs.update(json_data)
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "replace_asset", ctx, **kwargs)
    print_response(result, ctx)


@app.command("run-asset-jobs", deprecated=False, rich_help_panel="API commands")
def run_asset_jobs(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    name: str = typer.Option(..., "--name", help=""""""),
) -> None:
    """Run an asset job

    [link=https://api.immich.app/endpoints/assets/runAssetJobs]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["asset_ids"], asset_ids)
    set_nested(json_data, ["name"], name)
    asset_jobs_dto = AssetJobsDto.model_validate(json_data)
    kwargs["asset_jobs_dto"] = asset_jobs_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "run_asset_jobs", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-asset", deprecated=False, rich_help_panel="API commands")
def update_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    date_time_original: str | None = typer.Option(
        None, "--date-time-original", help=""""""
    ),
    description: str | None = typer.Option(None, "--description", help=""""""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=""""""
    ),
    latitude: float | None = typer.Option(None, "--latitude", help=""""""),
    live_photo_video_id: str | None = typer.Option(
        None, "--live-photo-video-id", help=""""""
    ),
    longitude: float | None = typer.Option(None, "--longitude", help=""""""),
    rating: float | None = typer.Option(None, "--rating", help="""""", min=-1, max=5),
    visibility: str | None = typer.Option(None, "--visibility", help=""""""),
) -> None:
    """Update an asset

    [link=https://api.immich.app/endpoints/assets/updateAsset]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if date_time_original is not None:
        set_nested(json_data, ["date_time_original"], date_time_original)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if latitude is not None:
        set_nested(json_data, ["latitude"], latitude)
    if live_photo_video_id is not None:
        set_nested(json_data, ["live_photo_video_id"], live_photo_video_id)
    if longitude is not None:
        set_nested(json_data, ["longitude"], longitude)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    update_asset_dto = UpdateAssetDto.model_validate(json_data)
    kwargs["update_asset_dto"] = update_asset_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "update_asset", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-asset-metadata", deprecated=False, rich_help_panel="API commands")
def update_asset_metadata(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    items: list[str] = typer.Option(..., "--items", help="""As a JSON string"""),
) -> None:
    """Update asset metadata

    [link=https://api.immich.app/endpoints/assets/updateAssetMetadata]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_items = [json.loads(i) for i in items]
    set_nested(json_data, ["items"], value_items)
    asset_metadata_upsert_dto = AssetMetadataUpsertDto.model_validate(json_data)
    kwargs["asset_metadata_upsert_dto"] = asset_metadata_upsert_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "update_asset_metadata", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-assets", deprecated=False, rich_help_panel="API commands")
def update_assets(
    ctx: typer.Context,
    date_time_original: str | None = typer.Option(
        None, "--date-time-original", help=""""""
    ),
    date_time_relative: float | None = typer.Option(
        None, "--date-time-relative", help=""""""
    ),
    description: str | None = typer.Option(None, "--description", help=""""""),
    duplicate_id: str | None = typer.Option(None, "--duplicate-id", help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=""""""
    ),
    latitude: float | None = typer.Option(None, "--latitude", help=""""""),
    longitude: float | None = typer.Option(None, "--longitude", help=""""""),
    rating: float | None = typer.Option(None, "--rating", help="""""", min=-1, max=5),
    time_zone: str | None = typer.Option(None, "--time-zone", help=""""""),
    visibility: str | None = typer.Option(None, "--visibility", help=""""""),
) -> None:
    """Update assets

    [link=https://api.immich.app/endpoints/assets/updateAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if date_time_original is not None:
        set_nested(json_data, ["date_time_original"], date_time_original)
    if date_time_relative is not None:
        set_nested(json_data, ["date_time_relative"], date_time_relative)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if duplicate_id is not None:
        set_nested(json_data, ["duplicate_id"], duplicate_id)
    set_nested(json_data, ["ids"], ids)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if latitude is not None:
        set_nested(json_data, ["latitude"], latitude)
    if longitude is not None:
        set_nested(json_data, ["longitude"], longitude)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if time_zone is not None:
        set_nested(json_data, ["time_zone"], time_zone)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    asset_bulk_update_dto = AssetBulkUpdateDto.model_validate(json_data)
    kwargs["asset_bulk_update_dto"] = asset_bulk_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "update_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("upload-asset", deprecated=False, rich_help_panel="API commands")
def upload_asset(
    ctx: typer.Context,
    asset_data: Path = typer.Option(..., "--asset-data", help="""""", exists=True),
    device_asset_id: str = typer.Option(..., "--device-asset-id", help=""""""),
    device_id: str = typer.Option(..., "--device-id", help=""""""),
    duration: str | None = typer.Option(None, "--duration", help=""""""),
    file_created_at: datetime = typer.Option(..., "--file-created-at", help=""""""),
    file_modified_at: datetime = typer.Option(..., "--file-modified-at", help=""""""),
    filename: str | None = typer.Option(None, "--filename", help=""""""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=""""""
    ),
    key: str | None = typer.Option(None, "--key", help=""""""),
    live_photo_video_id: str | None = typer.Option(
        None, "--live-photo-video-id", help=""""""
    ),
    metadata: list[str] = typer.Option(..., "--metadata", help="""As a JSON string"""),
    sidecar_data: Path | None = typer.Option(
        None, "--sidecar-data", help="""""", exists=True
    ),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
    visibility: str | None = typer.Option(None, "--visibility", help=""""""),
    x_immich_checksum: str | None = typer.Option(
        None,
        "--x-immich-checksum",
        help="""sha1 checksum that can be used for duplicate detection before the file is uploaded""",
    ),
) -> None:
    """Upload asset

    [link=https://api.immich.app/endpoints/assets/uploadAsset]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    if x_immich_checksum is not None:
        kwargs["x_immich_checksum"] = x_immich_checksum
    kwargs["asset_data"] = (asset_data.name, asset_data.read_bytes())
    set_nested(json_data, ["device_asset_id"], device_asset_id)
    set_nested(json_data, ["device_id"], device_id)
    if duration is not None:
        set_nested(json_data, ["duration"], duration)
    set_nested(json_data, ["file_created_at"], file_created_at)
    set_nested(json_data, ["file_modified_at"], file_modified_at)
    if filename is not None:
        set_nested(json_data, ["filename"], filename)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if live_photo_video_id is not None:
        set_nested(json_data, ["live_photo_video_id"], live_photo_video_id)
    value_metadata = [json.loads(i) for i in metadata]
    set_nested(json_data, ["metadata"], value_metadata)
    if sidecar_data is not None:
        set_nested(
            json_data, ["sidecar_data"], (sidecar_data.name, sidecar_data.read_bytes())
        )
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    kwargs.update(json_data)
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "upload_asset", ctx, **kwargs)
    print_response(result, ctx)


@app.command("view-asset", deprecated=False, rich_help_panel="API commands")
def view_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    size: AssetMediaSize | None = typer.Option(None, "--size", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """View asset thumbnail

    [link=https://api.immich.app/endpoints/assets/viewAsset]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if size is not None:
        kwargs["size"] = size
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.assets, "view_asset", ctx, **kwargs)
    print_response(result, ctx)
