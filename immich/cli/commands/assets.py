"""Generated CLI commands for Assets tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
import json
from datetime import datetime
from pathlib import Path
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""An asset is an image or video that has been uploaded to Immich.

Docs: https://api.immich.app/endpoints/assets"""
)


@app.command("check-bulk-upload", deprecated=False)
def check_bulk_upload(
    ctx: typer.Context,
    assets: list[str] = typer.Option(
        ...,
        "--assets",
        help="""Assets to check

As a JSON string""",
    ),
) -> None:
    """Check bulk upload

    Docs: https://api.immich.app/endpoints/assets/checkBulkUpload
    """
    kwargs = {}
    json_data = {}
    value_assets = [json.loads(i) for i in assets]
    set_nested(json_data, ["assets"], value_assets)
    from immich.client.models.asset_bulk_upload_check_dto import AssetBulkUploadCheckDto

    asset_bulk_upload_check_dto = AssetBulkUploadCheckDto.model_validate(json_data)
    kwargs["asset_bulk_upload_check_dto"] = asset_bulk_upload_check_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "check_bulk_upload", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("check-existing-assets", deprecated=False)
def check_existing_assets(
    ctx: typer.Context,
    device_asset_ids: list[str] = typer.Option(
        ..., "--device-asset-ids", help="""Device asset IDs to check"""
    ),
    device_id: str = typer.Option(..., "--device-id", help="""Device ID"""),
) -> None:
    """Check existing assets

    Docs: https://api.immich.app/endpoints/assets/checkExistingAssets
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["device_asset_ids"], device_asset_ids)
    set_nested(json_data, ["device_id"], device_id)
    from immich.client.models.check_existing_assets_dto import CheckExistingAssetsDto

    check_existing_assets_dto = CheckExistingAssetsDto.model_validate(json_data)
    kwargs["check_existing_assets_dto"] = check_existing_assets_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "check_existing_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("copy-asset", deprecated=False)
def copy_asset(
    ctx: typer.Context,
    albums: Literal["true", "false"] | None = typer.Option(
        None, "--albums", help="""Copy album associations"""
    ),
    favorite: Literal["true", "false"] | None = typer.Option(
        None, "--favorite", help="""Copy favorite status"""
    ),
    shared_links: Literal["true", "false"] | None = typer.Option(
        None, "--shared-links", help="""Copy shared links"""
    ),
    sidecar: Literal["true", "false"] | None = typer.Option(
        None, "--sidecar", help="""Copy sidecar file"""
    ),
    source_id: str = typer.Option(..., "--source-id", help="""Source asset ID"""),
    stack: Literal["true", "false"] | None = typer.Option(
        None, "--stack", help="""Copy stack association"""
    ),
    target_id: str = typer.Option(..., "--target-id", help="""Target asset ID"""),
) -> None:
    """Copy asset

    Docs: https://api.immich.app/endpoints/assets/copyAsset
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
    from immich.client.models.asset_copy_dto import AssetCopyDto

    asset_copy_dto = AssetCopyDto.model_validate(json_data)
    kwargs["asset_copy_dto"] = asset_copy_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "copy_asset", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-asset-metadata", deprecated=False)
def delete_asset_metadata(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Asset ID"""),
    key: str = typer.Argument(..., help="""Metadata key"""),
) -> None:
    """Delete asset metadata by key

    Docs: https://api.immich.app/endpoints/assets/deleteAssetMetadata
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["key"] = key
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "delete_asset_metadata", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-assets", deprecated=False)
def delete_assets(
    ctx: typer.Context,
    force: Literal["true", "false"] | None = typer.Option(
        None, "--force", help="""Force delete even if in use"""
    ),
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Delete assets

    Docs: https://api.immich.app/endpoints/assets/deleteAssets
    """
    kwargs = {}
    json_data = {}
    if force is not None:
        set_nested(json_data, ["force"], force.lower() == "true")
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.asset_bulk_delete_dto import AssetBulkDeleteDto

    asset_bulk_delete_dto = AssetBulkDeleteDto.model_validate(json_data)
    kwargs["asset_bulk_delete_dto"] = asset_bulk_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "delete_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-bulk-asset-metadata", deprecated=False)
def delete_bulk_asset_metadata(
    ctx: typer.Context,
    items: list[str] = typer.Option(
        ...,
        "--items",
        help="""Metadata items to delete

As a JSON string""",
    ),
) -> None:
    """Delete asset metadata

    Docs: https://api.immich.app/endpoints/assets/deleteBulkAssetMetadata
    """
    kwargs = {}
    json_data = {}
    value_items = [json.loads(i) for i in items]
    set_nested(json_data, ["items"], value_items)
    from immich.client.models.asset_metadata_bulk_delete_dto import (
        AssetMetadataBulkDeleteDto,
    )

    asset_metadata_bulk_delete_dto = AssetMetadataBulkDeleteDto.model_validate(
        json_data
    )
    kwargs["asset_metadata_bulk_delete_dto"] = asset_metadata_bulk_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "delete_bulk_asset_metadata", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("download-asset", deprecated=False)
def download_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Asset ID"""),
    edited: Literal["true", "false"] | None = typer.Option(
        None, "--edited", help="""Return edited asset if available"""
    ),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
) -> None:
    """Download original asset

    Docs: https://api.immich.app/endpoints/assets/downloadAsset
    """
    kwargs = {}
    if edited is not None:
        kwargs["edited"] = edited.lower() == "true"
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "download_asset", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("edit-asset", deprecated=False)
def edit_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    edits: list[str] = typer.Option(
        ...,
        "--edits",
        help="""List of edit actions to apply (crop, rotate, or mirror)

As a JSON string""",
    ),
) -> None:
    """Apply edits to an existing asset

    Docs: https://api.immich.app/endpoints/assets/editAsset
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_edits = [json.loads(i) for i in edits]
    set_nested(json_data, ["edits"], value_edits)
    from immich.client.models.asset_edit_action_list_dto import AssetEditActionListDto

    asset_edit_action_list_dto = AssetEditActionListDto.model_validate(json_data)
    kwargs["asset_edit_action_list_dto"] = asset_edit_action_list_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "edit_asset", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-all-user-assets-by-device-id", deprecated=True)
def get_all_user_assets_by_device_id(
    ctx: typer.Context,
    device_id: str = typer.Argument(..., help="""Device ID"""),
) -> None:
    """Retrieve assets by device ID

    Docs: https://api.immich.app/endpoints/assets/getAllUserAssetsByDeviceId
    """
    kwargs = {}
    kwargs["device_id"] = device_id
    client = ctx.obj["client"]
    result = run_command(
        client, client.assets, "get_all_user_assets_by_device_id", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-asset-edits", deprecated=False)
def get_asset_edits(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve edits for an existing asset

    Docs: https://api.immich.app/endpoints/assets/getAssetEdits
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_edits", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-asset-info", deprecated=False)
def get_asset_info(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
) -> None:
    """Retrieve an asset

    Docs: https://api.immich.app/endpoints/assets/getAssetInfo
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_info", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-asset-metadata", deprecated=False)
def get_asset_metadata(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Get asset metadata

    Docs: https://api.immich.app/endpoints/assets/getAssetMetadata
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_metadata", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-asset-metadata-by-key", deprecated=False)
def get_asset_metadata_by_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Asset ID"""),
    key: str = typer.Argument(..., help="""Metadata key"""),
) -> None:
    """Retrieve asset metadata by key

    Docs: https://api.immich.app/endpoints/assets/getAssetMetadataByKey
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["key"] = key
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_metadata_by_key", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-asset-ocr", deprecated=False)
def get_asset_ocr(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve asset OCR data

    Docs: https://api.immich.app/endpoints/assets/getAssetOcr
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_ocr", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-asset-statistics", deprecated=False)
def get_asset_statistics(
    ctx: typer.Context,
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Filter by favorite status"""
    ),
    is_trashed: Literal["true", "false"] | None = typer.Option(
        None, "--is-trashed", help="""Filter by trash status"""
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help="""Filter by visibility"""
    ),
) -> None:
    """Get asset statistics

    Docs: https://api.immich.app/endpoints/assets/getAssetStatistics
    """
    kwargs = {}
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite.lower() == "true"
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed.lower() == "true"
    if visibility is not None:
        kwargs["visibility"] = visibility
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "get_asset_statistics", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-random", deprecated=True)
def get_random(
    ctx: typer.Context,
    count: float | None = typer.Option(
        None, "--count", help="""Number of random assets to return""", min=1
    ),
) -> None:
    """Get random assets

    Docs: https://api.immich.app/endpoints/assets/getRandom
    """
    kwargs = {}
    if count is not None:
        kwargs["count"] = count
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "get_random", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("play-asset-video", deprecated=False)
def play_asset_video(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Asset ID"""),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
) -> None:
    """Play asset video

    Docs: https://api.immich.app/endpoints/assets/playAssetVideo
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "play_asset_video", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("remove-asset-edits", deprecated=False)
def remove_asset_edits(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Remove edits from an existing asset

    Docs: https://api.immich.app/endpoints/assets/removeAssetEdits
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "remove_asset_edits", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("replace-asset", deprecated=True)
def replace_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Asset ID"""),
    asset_data: Path = typer.Option(..., "--asset-data", help="""Asset file data"""),
    device_asset_id: str = typer.Option(
        ..., "--device-asset-id", help="""Device asset ID"""
    ),
    device_id: str = typer.Option(..., "--device-id", help="""Device ID"""),
    duration: str | None = typer.Option(
        None, "--duration", help="""Duration (for videos)"""
    ),
    file_created_at: datetime = typer.Option(
        ..., "--file-created-at", help="""File creation date"""
    ),
    file_modified_at: datetime = typer.Option(
        ..., "--file-modified-at", help="""File modification date"""
    ),
    filename: str | None = typer.Option(None, "--filename", help="""Filename"""),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
) -> None:
    """Replace asset

    Docs: https://api.immich.app/endpoints/assets/replaceAsset
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
    from immich.client.models.asset_media_replace_dto import AssetMediaReplaceDto

    asset_media_replace_dto = AssetMediaReplaceDto.model_validate(json_data)
    kwargs["asset_media_replace_dto"] = asset_media_replace_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "replace_asset", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("run-asset-jobs", deprecated=False)
def run_asset_jobs(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help="""Asset IDs"""),
    name: str = typer.Option(..., "--name", help="""Job name"""),
) -> None:
    """Run an asset job

    Docs: https://api.immich.app/endpoints/assets/runAssetJobs
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["asset_ids"], asset_ids)
    set_nested(json_data, ["name"], name)
    from immich.client.models.asset_jobs_dto import AssetJobsDto

    asset_jobs_dto = AssetJobsDto.model_validate(json_data)
    kwargs["asset_jobs_dto"] = asset_jobs_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "run_asset_jobs", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-asset", deprecated=False)
def update_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    date_time_original: str | None = typer.Option(
        None, "--date-time-original", help="""Original date and time"""
    ),
    description: str | None = typer.Option(
        None, "--description", help="""Asset description"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Mark as favorite"""
    ),
    latitude: float | None = typer.Option(
        None, "--latitude", help="""Latitude coordinate"""
    ),
    live_photo_video_id: str | None = typer.Option(
        None, "--live-photo-video-id", help="""Live photo video ID"""
    ),
    longitude: float | None = typer.Option(
        None, "--longitude", help="""Longitude coordinate"""
    ),
    rating: float | None = typer.Option(
        None, "--rating", help="""Rating (-1 to 5)""", min=-1, max=5
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help="""Asset visibility"""
    ),
) -> None:
    """Update an asset

    Docs: https://api.immich.app/endpoints/assets/updateAsset
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
    from immich.client.models.update_asset_dto import UpdateAssetDto

    update_asset_dto = UpdateAssetDto.model_validate(json_data)
    kwargs["update_asset_dto"] = update_asset_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "update_asset", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-asset-metadata", deprecated=False)
def update_asset_metadata(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    items: list[str] = typer.Option(
        ...,
        "--items",
        help="""Metadata items to upsert

As a JSON string""",
    ),
) -> None:
    """Update asset metadata

    Docs: https://api.immich.app/endpoints/assets/updateAssetMetadata
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_items = [json.loads(i) for i in items]
    set_nested(json_data, ["items"], value_items)
    from immich.client.models.asset_metadata_upsert_dto import AssetMetadataUpsertDto

    asset_metadata_upsert_dto = AssetMetadataUpsertDto.model_validate(json_data)
    kwargs["asset_metadata_upsert_dto"] = asset_metadata_upsert_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "update_asset_metadata", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-assets", deprecated=False)
def update_assets(
    ctx: typer.Context,
    date_time_original: str | None = typer.Option(
        None, "--date-time-original", help="""Original date and time"""
    ),
    date_time_relative: float | None = typer.Option(
        None, "--date-time-relative", help="""Relative time offset in seconds"""
    ),
    description: str | None = typer.Option(
        None, "--description", help="""Asset description"""
    ),
    duplicate_id: str | None = typer.Option(
        None, "--duplicate-id", help="""Duplicate asset ID"""
    ),
    ids: list[str] = typer.Option(..., "--ids", help="""Asset IDs to update"""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Mark as favorite"""
    ),
    latitude: float | None = typer.Option(
        None, "--latitude", help="""Latitude coordinate"""
    ),
    longitude: float | None = typer.Option(
        None, "--longitude", help="""Longitude coordinate"""
    ),
    rating: float | None = typer.Option(
        None, "--rating", help="""Rating (-1 to 5)""", min=-1, max=5
    ),
    time_zone: str | None = typer.Option(
        None, "--time-zone", help="""Time zone (IANA timezone)"""
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help="""Asset visibility"""
    ),
) -> None:
    """Update assets

    Docs: https://api.immich.app/endpoints/assets/updateAssets
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
    from immich.client.models.asset_bulk_update_dto import AssetBulkUpdateDto

    asset_bulk_update_dto = AssetBulkUpdateDto.model_validate(json_data)
    kwargs["asset_bulk_update_dto"] = asset_bulk_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "update_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-bulk-asset-metadata", deprecated=False)
def update_bulk_asset_metadata(
    ctx: typer.Context,
    items: list[str] = typer.Option(
        ...,
        "--items",
        help="""Metadata items to upsert

As a JSON string""",
    ),
) -> None:
    """Upsert asset metadata

    Docs: https://api.immich.app/endpoints/assets/updateBulkAssetMetadata
    """
    kwargs = {}
    json_data = {}
    value_items = [json.loads(i) for i in items]
    set_nested(json_data, ["items"], value_items)
    from immich.client.models.asset_metadata_bulk_upsert_dto import (
        AssetMetadataBulkUpsertDto,
    )

    asset_metadata_bulk_upsert_dto = AssetMetadataBulkUpsertDto.model_validate(
        json_data
    )
    kwargs["asset_metadata_bulk_upsert_dto"] = asset_metadata_bulk_upsert_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "update_bulk_asset_metadata", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("upload-asset", deprecated=False)
def upload_asset(
    ctx: typer.Context,
    asset_data: Path = typer.Option(..., "--asset-data", help="""Asset file data"""),
    device_asset_id: str = typer.Option(
        ..., "--device-asset-id", help="""Device asset ID"""
    ),
    device_id: str = typer.Option(..., "--device-id", help="""Device ID"""),
    duration: str | None = typer.Option(
        None, "--duration", help="""Duration (for videos)"""
    ),
    file_created_at: datetime = typer.Option(
        ..., "--file-created-at", help="""File creation date"""
    ),
    file_modified_at: datetime = typer.Option(
        ..., "--file-modified-at", help="""File modification date"""
    ),
    filename: str | None = typer.Option(None, "--filename", help="""Filename"""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Mark as favorite"""
    ),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    live_photo_video_id: str | None = typer.Option(
        None, "--live-photo-video-id", help="""Live photo video ID"""
    ),
    metadata: list[str] | None = typer.Option(
        None,
        "--metadata",
        help="""Asset metadata items

As a JSON string""",
    ),
    sidecar_data: Path | None = typer.Option(
        None, "--sidecar-data", help="""Sidecar file data"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help="""Asset visibility"""
    ),
    x_immich_checksum: str | None = typer.Option(
        None,
        "--x-immich-checksum",
        help="""sha1 checksum that can be used for duplicate detection before the file is uploaded""",
    ),
) -> None:
    """Upload asset

    Docs: https://api.immich.app/endpoints/assets/uploadAsset
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
    if metadata is not None:
        value_metadata = [json.loads(i) for i in metadata]
        set_nested(json_data, ["metadata"], value_metadata)
    if sidecar_data is not None:
        set_nested(
            json_data, ["sidecar_data"], (sidecar_data.name, sidecar_data.read_bytes())
        )
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    from immich.client.models.asset_media_create_dto import AssetMediaCreateDto

    asset_media_create_dto = AssetMediaCreateDto.model_validate(json_data)
    kwargs["asset_media_create_dto"] = asset_media_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "upload_asset", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("view-asset", deprecated=False)
def view_asset(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Asset ID"""),
    edited: Literal["true", "false"] | None = typer.Option(
        None, "--edited", help="""Return edited asset if available"""
    ),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    size: AssetMediaSize | None = typer.Option(
        None, "--size", help="""Asset media size"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
) -> None:
    """View asset thumbnail

    Docs: https://api.immich.app/endpoints/assets/viewAsset
    """
    kwargs = {}
    if edited is not None:
        kwargs["edited"] = edited.lower() == "true"
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if size is not None:
        kwargs["size"] = size
    if slug is not None:
        kwargs["slug"] = slug
    client = ctx.obj["client"]
    result = run_command(client, client.assets, "view_asset", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
