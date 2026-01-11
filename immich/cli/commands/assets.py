"""Generated CLI commands for Assets tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""An asset is an image or video that has been uploaded to Immich.

Docs: https://api.immich.app/endpoints/assets""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("check-bulk-upload")
def check_bulk_upload(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    assets: list[str] = typer.Option(..., "--assets", help="JSON string for assets"),
) -> None:
    """Check bulk upload

Docs: https://api.immich.app/endpoints/assets/checkBulkUpload
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([assets])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_bulk_upload_check_dto import AssetBulkUploadCheckDto
        asset_bulk_upload_check_dto = deserialize_request_body(json_data, AssetBulkUploadCheckDto)
        kwargs['asset_bulk_upload_check_dto'] = asset_bulk_upload_check_dto
    elif any([
        assets,
    ]):
        # Build body from dotted flags
        json_data = {}
        if assets is None:
            raise SystemExit("Error: --assets is required")
        value_assets = json.loads(assets)
        set_nested(json_data, ['assets'], value_assets)
        if json_data:
            from immich.client.models.asset_bulk_upload_check_dto import AssetBulkUploadCheckDto
            asset_bulk_upload_check_dto = deserialize_request_body(json_data, AssetBulkUploadCheckDto)
            kwargs['asset_bulk_upload_check_dto'] = asset_bulk_upload_check_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'check_bulk_upload', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("check-existing-assets")
def check_existing_assets(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    device_asset_ids: list[str] = typer.Option(..., "--deviceAssetIds"),
    device_id: str = typer.Option(..., "--deviceId"),
) -> None:
    """Check existing assets

Docs: https://api.immich.app/endpoints/assets/checkExistingAssets
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([device_asset_ids, device_id])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.check_existing_assets_dto import CheckExistingAssetsDto
        check_existing_assets_dto = deserialize_request_body(json_data, CheckExistingAssetsDto)
        kwargs['check_existing_assets_dto'] = check_existing_assets_dto
    elif any([
        device_asset_ids,
        device_id,
    ]):
        # Build body from dotted flags
        json_data = {}
        if device_asset_ids is None:
            raise SystemExit("Error: --deviceAssetIds is required")
        set_nested(json_data, ['deviceAssetIds'], device_asset_ids)
        if device_id is None:
            raise SystemExit("Error: --deviceId is required")
        set_nested(json_data, ['deviceId'], device_id)
        if json_data:
            from immich.client.models.check_existing_assets_dto import CheckExistingAssetsDto
            check_existing_assets_dto = deserialize_request_body(json_data, CheckExistingAssetsDto)
            kwargs['check_existing_assets_dto'] = check_existing_assets_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'check_existing_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("copy-asset")
def copy_asset(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    albums: bool | None = typer.Option(None, "--albums"),
    favorite: bool | None = typer.Option(None, "--favorite"),
    shared_links: bool | None = typer.Option(None, "--sharedLinks"),
    sidecar: bool | None = typer.Option(None, "--sidecar"),
    source_id: str = typer.Option(..., "--sourceId"),
    stack: bool | None = typer.Option(None, "--stack"),
    target_id: str = typer.Option(..., "--targetId"),
) -> None:
    """Copy asset

Docs: https://api.immich.app/endpoints/assets/copyAsset
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([albums, favorite, shared_links, sidecar, source_id, stack, target_id])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_copy_dto import AssetCopyDto
        asset_copy_dto = deserialize_request_body(json_data, AssetCopyDto)
        kwargs['asset_copy_dto'] = asset_copy_dto
    elif any([
        albums,
        favorite,
        shared_links,
        sidecar,
        source_id,
        stack,
        target_id,
    ]):
        # Build body from dotted flags
        json_data = {}
        if albums is not None:
            set_nested(json_data, ['albums'], albums)
        if favorite is not None:
            set_nested(json_data, ['favorite'], favorite)
        if shared_links is not None:
            set_nested(json_data, ['sharedLinks'], shared_links)
        if sidecar is not None:
            set_nested(json_data, ['sidecar'], sidecar)
        if source_id is None:
            raise SystemExit("Error: --sourceId is required")
        set_nested(json_data, ['sourceId'], source_id)
        if stack is not None:
            set_nested(json_data, ['stack'], stack)
        if target_id is None:
            raise SystemExit("Error: --targetId is required")
        set_nested(json_data, ['targetId'], target_id)
        if json_data:
            from immich.client.models.asset_copy_dto import AssetCopyDto
            asset_copy_dto = deserialize_request_body(json_data, AssetCopyDto)
            kwargs['asset_copy_dto'] = asset_copy_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'copy_asset', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-asset-metadata")
def delete_asset_metadata(
    ctx: typer.Context,
    id: str,
    key: str,
) -> None:
    """Delete asset metadata by key

Docs: https://api.immich.app/endpoints/assets/deleteAssetMetadata
    """
    kwargs = {}
    kwargs['id'] = id
    kwargs['key'] = key
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'delete_asset_metadata', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-assets")
def delete_assets(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    force: bool | None = typer.Option(None, "--force"),
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Delete assets

Docs: https://api.immich.app/endpoints/assets/deleteAssets
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([force, ids])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_bulk_delete_dto import AssetBulkDeleteDto
        asset_bulk_delete_dto = deserialize_request_body(json_data, AssetBulkDeleteDto)
        kwargs['asset_bulk_delete_dto'] = asset_bulk_delete_dto
    elif any([
        force,
        ids,
    ]):
        # Build body from dotted flags
        json_data = {}
        if force is not None:
            set_nested(json_data, ['force'], force)
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ['ids'], ids)
        if json_data:
            from immich.client.models.asset_bulk_delete_dto import AssetBulkDeleteDto
            asset_bulk_delete_dto = deserialize_request_body(json_data, AssetBulkDeleteDto)
            kwargs['asset_bulk_delete_dto'] = asset_bulk_delete_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'delete_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-bulk-asset-metadata")
def delete_bulk_asset_metadata(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    items: list[str] = typer.Option(..., "--items", help="JSON string for items"),
) -> None:
    """Delete asset metadata

Docs: https://api.immich.app/endpoints/assets/deleteBulkAssetMetadata
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([items])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_metadata_bulk_delete_dto import AssetMetadataBulkDeleteDto
        asset_metadata_bulk_delete_dto = deserialize_request_body(json_data, AssetMetadataBulkDeleteDto)
        kwargs['asset_metadata_bulk_delete_dto'] = asset_metadata_bulk_delete_dto
    elif any([
        items,
    ]):
        # Build body from dotted flags
        json_data = {}
        if items is None:
            raise SystemExit("Error: --items is required")
        value_items = json.loads(items)
        set_nested(json_data, ['items'], value_items)
        if json_data:
            from immich.client.models.asset_metadata_bulk_delete_dto import AssetMetadataBulkDeleteDto
            asset_metadata_bulk_delete_dto = deserialize_request_body(json_data, AssetMetadataBulkDeleteDto)
            kwargs['asset_metadata_bulk_delete_dto'] = asset_metadata_bulk_delete_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'delete_bulk_asset_metadata', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("download-asset")
def download_asset(
    ctx: typer.Context,
    id: str,
    edited: bool | None = typer.Option(None, "--edited"),
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
) -> None:
    """Download original asset

Docs: https://api.immich.app/endpoints/assets/downloadAsset
    """
    kwargs = {}
    kwargs['id'] = id
    if edited is not None:
        kwargs['edited'] = edited
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'download_asset', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("edit-asset")
def edit_asset(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    edits: list[str] = typer.Option(..., "--edits", help="JSON string for edits"),
) -> None:
    """Apply edits to an existing asset

Docs: https://api.immich.app/endpoints/assets/editAsset
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([edits])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_edit_action_list_dto import AssetEditActionListDto
        asset_edit_action_list_dto = deserialize_request_body(json_data, AssetEditActionListDto)
        kwargs['asset_edit_action_list_dto'] = asset_edit_action_list_dto
    elif any([
        edits,
    ]):
        # Build body from dotted flags
        json_data = {}
        if edits is None:
            raise SystemExit("Error: --edits is required")
        value_edits = json.loads(edits)
        set_nested(json_data, ['edits'], value_edits)
        if json_data:
            from immich.client.models.asset_edit_action_list_dto import AssetEditActionListDto
            asset_edit_action_list_dto = deserialize_request_body(json_data, AssetEditActionListDto)
            kwargs['asset_edit_action_list_dto'] = asset_edit_action_list_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'edit_asset', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-user-assets-by-device-id")
def get_all_user_assets_by_device_id(
    ctx: typer.Context,
    device_id: str,
) -> None:
    """Retrieve assets by device ID

Docs: https://api.immich.app/endpoints/assets/getAllUserAssetsByDeviceId
    """
    kwargs = {}
    kwargs['device_id'] = device_id
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_all_user_assets_by_device_id', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-asset-edits")
def get_asset_edits(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve edits for an existing asset

Docs: https://api.immich.app/endpoints/assets/getAssetEdits
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_asset_edits', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-asset-info")
def get_asset_info(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
) -> None:
    """Retrieve an asset

Docs: https://api.immich.app/endpoints/assets/getAssetInfo
    """
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_asset_info', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-asset-metadata")
def get_asset_metadata(
    ctx: typer.Context,
    id: str,
) -> None:
    """Get asset metadata

Docs: https://api.immich.app/endpoints/assets/getAssetMetadata
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_asset_metadata', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-asset-metadata-by-key")
def get_asset_metadata_by_key(
    ctx: typer.Context,
    id: str,
    key: str,
) -> None:
    """Retrieve asset metadata by key

Docs: https://api.immich.app/endpoints/assets/getAssetMetadataByKey
    """
    kwargs = {}
    kwargs['id'] = id
    kwargs['key'] = key
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_asset_metadata_by_key', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-asset-ocr")
def get_asset_ocr(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve asset OCR data

Docs: https://api.immich.app/endpoints/assets/getAssetOcr
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_asset_ocr', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-asset-statistics")
def get_asset_statistics(
    ctx: typer.Context,
    is_favorite: bool | None = typer.Option(None, "--is-favorite"),
    is_trashed: bool | None = typer.Option(None, "--is-trashed"),
    visibility: str | None = typer.Option(None, "--visibility"),
) -> None:
    """Get asset statistics

Docs: https://api.immich.app/endpoints/assets/getAssetStatistics
    """
    kwargs = {}
    if is_favorite is not None:
        kwargs['is_favorite'] = is_favorite
    if is_trashed is not None:
        kwargs['is_trashed'] = is_trashed
    if visibility is not None:
        kwargs['visibility'] = visibility
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_asset_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-random")
def get_random(
    ctx: typer.Context,
    count: float | None = typer.Option(None, "--count"),
) -> None:
    """Get random assets

Docs: https://api.immich.app/endpoints/assets/getRandom
    """
    kwargs = {}
    if count is not None:
        kwargs['count'] = count
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_random', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("play-asset-video")
def play_asset_video(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
) -> None:
    """Play asset video

Docs: https://api.immich.app/endpoints/assets/playAssetVideo
    """
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'play_asset_video', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-asset-edits")
def remove_asset_edits(
    ctx: typer.Context,
    id: str,
) -> None:
    """Remove edits from an existing asset

Docs: https://api.immich.app/endpoints/assets/removeAssetEdits
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'remove_asset_edits', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("replace-asset")
def replace_asset(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON with multipart fields (non-file)"),
    asset_data: Path = typer.Option(..., "--asset-data", help="File to upload for assetData"),
) -> None:
    """Replace asset

Docs: https://api.immich.app/endpoints/assets/replaceAsset
    """
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    json_data = json.loads(json_str) if json_str is not None else {}
    missing: list[str] = []
    kwargs['asset_data'] = load_file_bytes(asset_data)
    if 'deviceAssetId' in json_data:
        kwargs['device_asset_id'] = json_data['deviceAssetId']
    elif 'device_asset_id' in json_data:
        kwargs['device_asset_id'] = json_data['device_asset_id']
    else:
        missing.append('deviceAssetId')
    if 'deviceId' in json_data:
        kwargs['device_id'] = json_data['deviceId']
    elif 'device_id' in json_data:
        kwargs['device_id'] = json_data['device_id']
    else:
        missing.append('deviceId')
    if 'duration' in json_data:
        kwargs['duration'] = json_data['duration']
    elif 'duration' in json_data:
        kwargs['duration'] = json_data['duration']
    if 'fileCreatedAt' in json_data:
        kwargs['file_created_at'] = json_data['fileCreatedAt']
    elif 'file_created_at' in json_data:
        kwargs['file_created_at'] = json_data['file_created_at']
    else:
        missing.append('fileCreatedAt')
    if 'fileModifiedAt' in json_data:
        kwargs['file_modified_at'] = json_data['fileModifiedAt']
    elif 'file_modified_at' in json_data:
        kwargs['file_modified_at'] = json_data['file_modified_at']
    else:
        missing.append('fileModifiedAt')
    if 'filename' in json_data:
        kwargs['filename'] = json_data['filename']
    elif 'filename' in json_data:
        kwargs['filename'] = json_data['filename']
    if missing:
        raise SystemExit("Error: missing required multipart fields: " + ', '.join(missing) + ". Provide them via --json and/or file options.")
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'replace_asset', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("run-asset-jobs")
def run_asset_jobs(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    asset_ids: list[str] = typer.Option(..., "--assetIds"),
    name: str = typer.Option(..., "--name"),
) -> None:
    """Run an asset job

Docs: https://api.immich.app/endpoints/assets/runAssetJobs
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([asset_ids, name])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_jobs_dto import AssetJobsDto
        asset_jobs_dto = deserialize_request_body(json_data, AssetJobsDto)
        kwargs['asset_jobs_dto'] = asset_jobs_dto
    elif any([
        asset_ids,
        name,
    ]):
        # Build body from dotted flags
        json_data = {}
        if asset_ids is None:
            raise SystemExit("Error: --assetIds is required")
        set_nested(json_data, ['assetIds'], asset_ids)
        if name is None:
            raise SystemExit("Error: --name is required")
        set_nested(json_data, ['name'], name)
        if json_data:
            from immich.client.models.asset_jobs_dto import AssetJobsDto
            asset_jobs_dto = deserialize_request_body(json_data, AssetJobsDto)
            kwargs['asset_jobs_dto'] = asset_jobs_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'run_asset_jobs', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-asset")
def update_asset(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    date_time_original: str | None = typer.Option(None, "--dateTimeOriginal"),
    description: str | None = typer.Option(None, "--description"),
    is_favorite: bool | None = typer.Option(None, "--isFavorite"),
    latitude: float | None = typer.Option(None, "--latitude"),
    live_photo_video_id: str | None = typer.Option(None, "--livePhotoVideoId"),
    longitude: float | None = typer.Option(None, "--longitude"),
    rating: float | None = typer.Option(None, "--rating"),
    visibility: str | None = typer.Option(None, "--visibility"),
) -> None:
    """Update an asset

Docs: https://api.immich.app/endpoints/assets/updateAsset
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([date_time_original, description, is_favorite, latitude, live_photo_video_id, longitude, rating, visibility])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.update_asset_dto import UpdateAssetDto
        update_asset_dto = deserialize_request_body(json_data, UpdateAssetDto)
        kwargs['update_asset_dto'] = update_asset_dto
    elif any([
        date_time_original,
        description,
        is_favorite,
        latitude,
        live_photo_video_id,
        longitude,
        rating,
        visibility,
    ]):
        # Build body from dotted flags
        json_data = {}
        if date_time_original is not None:
            set_nested(json_data, ['dateTimeOriginal'], date_time_original)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if is_favorite is not None:
            set_nested(json_data, ['isFavorite'], is_favorite)
        if latitude is not None:
            set_nested(json_data, ['latitude'], latitude)
        if live_photo_video_id is not None:
            set_nested(json_data, ['livePhotoVideoId'], live_photo_video_id)
        if longitude is not None:
            set_nested(json_data, ['longitude'], longitude)
        if rating is not None:
            set_nested(json_data, ['rating'], rating)
        if visibility is not None:
            set_nested(json_data, ['visibility'], visibility)
        if json_data:
            from immich.client.models.update_asset_dto import UpdateAssetDto
            update_asset_dto = deserialize_request_body(json_data, UpdateAssetDto)
            kwargs['update_asset_dto'] = update_asset_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'update_asset', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-asset-metadata")
def update_asset_metadata(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    items: list[str] = typer.Option(..., "--items", help="JSON string for items"),
) -> None:
    """Update asset metadata

Docs: https://api.immich.app/endpoints/assets/updateAssetMetadata
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([items])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_metadata_upsert_dto import AssetMetadataUpsertDto
        asset_metadata_upsert_dto = deserialize_request_body(json_data, AssetMetadataUpsertDto)
        kwargs['asset_metadata_upsert_dto'] = asset_metadata_upsert_dto
    elif any([
        items,
    ]):
        # Build body from dotted flags
        json_data = {}
        if items is None:
            raise SystemExit("Error: --items is required")
        value_items = json.loads(items)
        set_nested(json_data, ['items'], value_items)
        if json_data:
            from immich.client.models.asset_metadata_upsert_dto import AssetMetadataUpsertDto
            asset_metadata_upsert_dto = deserialize_request_body(json_data, AssetMetadataUpsertDto)
            kwargs['asset_metadata_upsert_dto'] = asset_metadata_upsert_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'update_asset_metadata', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-assets")
def update_assets(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    date_time_original: str | None = typer.Option(None, "--dateTimeOriginal"),
    date_time_relative: float | None = typer.Option(None, "--dateTimeRelative"),
    description: str | None = typer.Option(None, "--description"),
    duplicate_id: str | None = typer.Option(None, "--duplicateId"),
    ids: list[str] = typer.Option(..., "--ids"),
    is_favorite: bool | None = typer.Option(None, "--isFavorite"),
    latitude: float | None = typer.Option(None, "--latitude"),
    longitude: float | None = typer.Option(None, "--longitude"),
    rating: float | None = typer.Option(None, "--rating"),
    time_zone: str | None = typer.Option(None, "--timeZone"),
    visibility: str | None = typer.Option(None, "--visibility"),
) -> None:
    """Update assets

Docs: https://api.immich.app/endpoints/assets/updateAssets
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([date_time_original, date_time_relative, description, duplicate_id, ids, is_favorite, latitude, longitude, rating, time_zone, visibility])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_bulk_update_dto import AssetBulkUpdateDto
        asset_bulk_update_dto = deserialize_request_body(json_data, AssetBulkUpdateDto)
        kwargs['asset_bulk_update_dto'] = asset_bulk_update_dto
    elif any([
        date_time_original,
        date_time_relative,
        description,
        duplicate_id,
        ids,
        is_favorite,
        latitude,
        longitude,
        rating,
        time_zone,
        visibility,
    ]):
        # Build body from dotted flags
        json_data = {}
        if date_time_original is not None:
            set_nested(json_data, ['dateTimeOriginal'], date_time_original)
        if date_time_relative is not None:
            set_nested(json_data, ['dateTimeRelative'], date_time_relative)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if duplicate_id is not None:
            set_nested(json_data, ['duplicateId'], duplicate_id)
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ['ids'], ids)
        if is_favorite is not None:
            set_nested(json_data, ['isFavorite'], is_favorite)
        if latitude is not None:
            set_nested(json_data, ['latitude'], latitude)
        if longitude is not None:
            set_nested(json_data, ['longitude'], longitude)
        if rating is not None:
            set_nested(json_data, ['rating'], rating)
        if time_zone is not None:
            set_nested(json_data, ['timeZone'], time_zone)
        if visibility is not None:
            set_nested(json_data, ['visibility'], visibility)
        if json_data:
            from immich.client.models.asset_bulk_update_dto import AssetBulkUpdateDto
            asset_bulk_update_dto = deserialize_request_body(json_data, AssetBulkUpdateDto)
            kwargs['asset_bulk_update_dto'] = asset_bulk_update_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'update_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-bulk-asset-metadata")
def update_bulk_asset_metadata(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    items: list[str] = typer.Option(..., "--items", help="JSON string for items"),
) -> None:
    """Upsert asset metadata

Docs: https://api.immich.app/endpoints/assets/updateBulkAssetMetadata
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([items])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_metadata_bulk_upsert_dto import AssetMetadataBulkUpsertDto
        asset_metadata_bulk_upsert_dto = deserialize_request_body(json_data, AssetMetadataBulkUpsertDto)
        kwargs['asset_metadata_bulk_upsert_dto'] = asset_metadata_bulk_upsert_dto
    elif any([
        items,
    ]):
        # Build body from dotted flags
        json_data = {}
        if items is None:
            raise SystemExit("Error: --items is required")
        value_items = json.loads(items)
        set_nested(json_data, ['items'], value_items)
        if json_data:
            from immich.client.models.asset_metadata_bulk_upsert_dto import AssetMetadataBulkUpsertDto
            asset_metadata_bulk_upsert_dto = deserialize_request_body(json_data, AssetMetadataBulkUpsertDto)
            kwargs['asset_metadata_bulk_upsert_dto'] = asset_metadata_bulk_upsert_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'update_bulk_asset_metadata', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("upload-asset")
def upload_asset(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    x_immich_checksum: str | None = typer.Option(None, "--x-immich-checksum"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON with multipart fields (non-file)"),
    asset_data: Path = typer.Option(..., "--asset-data", help="File to upload for assetData"),
    sidecar_data: Path | None = typer.Option(None, "--sidecar-data", help="File to upload for sidecarData"),
) -> None:
    """Upload asset

Docs: https://api.immich.app/endpoints/assets/uploadAsset
    """
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if x_immich_checksum is not None:
        kwargs['x_immich_checksum'] = x_immich_checksum
    json_data = json.loads(json_str) if json_str is not None else {}
    missing: list[str] = []
    kwargs['asset_data'] = load_file_bytes(asset_data)
    if 'deviceAssetId' in json_data:
        kwargs['device_asset_id'] = json_data['deviceAssetId']
    elif 'device_asset_id' in json_data:
        kwargs['device_asset_id'] = json_data['device_asset_id']
    else:
        missing.append('deviceAssetId')
    if 'deviceId' in json_data:
        kwargs['device_id'] = json_data['deviceId']
    elif 'device_id' in json_data:
        kwargs['device_id'] = json_data['device_id']
    else:
        missing.append('deviceId')
    if 'duration' in json_data:
        kwargs['duration'] = json_data['duration']
    elif 'duration' in json_data:
        kwargs['duration'] = json_data['duration']
    if 'fileCreatedAt' in json_data:
        kwargs['file_created_at'] = json_data['fileCreatedAt']
    elif 'file_created_at' in json_data:
        kwargs['file_created_at'] = json_data['file_created_at']
    else:
        missing.append('fileCreatedAt')
    if 'fileModifiedAt' in json_data:
        kwargs['file_modified_at'] = json_data['fileModifiedAt']
    elif 'file_modified_at' in json_data:
        kwargs['file_modified_at'] = json_data['file_modified_at']
    else:
        missing.append('fileModifiedAt')
    if 'filename' in json_data:
        kwargs['filename'] = json_data['filename']
    elif 'filename' in json_data:
        kwargs['filename'] = json_data['filename']
    if 'isFavorite' in json_data:
        kwargs['is_favorite'] = json_data['isFavorite']
    elif 'is_favorite' in json_data:
        kwargs['is_favorite'] = json_data['is_favorite']
    if 'livePhotoVideoId' in json_data:
        kwargs['live_photo_video_id'] = json_data['livePhotoVideoId']
    elif 'live_photo_video_id' in json_data:
        kwargs['live_photo_video_id'] = json_data['live_photo_video_id']
    if 'metadata' in json_data:
        kwargs['metadata'] = json_data['metadata']
    elif 'metadata' in json_data:
        kwargs['metadata'] = json_data['metadata']
    if sidecar_data is not None:
        kwargs['sidecar_data'] = load_file_bytes(sidecar_data)
    if 'visibility' in json_data:
        kwargs['visibility'] = json_data['visibility']
    elif 'visibility' in json_data:
        kwargs['visibility'] = json_data['visibility']
    if missing:
        raise SystemExit("Error: missing required multipart fields: " + ', '.join(missing) + ". Provide them via --json and/or file options.")
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'upload_asset', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("view-asset")
def view_asset(
    ctx: typer.Context,
    id: str,
    edited: bool | None = typer.Option(None, "--edited"),
    key: str | None = typer.Option(None, "--key"),
    size: str | None = typer.Option(None, "--size"),
    slug: str | None = typer.Option(None, "--slug"),
) -> None:
    """View asset thumbnail

Docs: https://api.immich.app/endpoints/assets/viewAsset
    """
    kwargs = {}
    kwargs['id'] = id
    if edited is not None:
        kwargs['edited'] = edited
    if key is not None:
        kwargs['key'] = key
    if size is not None:
        kwargs['size'] = size
    if slug is not None:
        kwargs['slug'] = slug
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'view_asset', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
