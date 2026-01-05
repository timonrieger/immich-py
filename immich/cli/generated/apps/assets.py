"""Generated CLI commands for Assets tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Assets operations")

@app.command("check-bulk-upload")
def check_bulk_upload(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Check bulk upload"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Check existing assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Copy asset"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    """Delete asset metadata by key"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Delete assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.asset_bulk_delete_dto import AssetBulkDeleteDto
        asset_bulk_delete_dto = deserialize_request_body(json_data, AssetBulkDeleteDto)
        kwargs['asset_bulk_delete_dto'] = asset_bulk_delete_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'delete_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("download-asset")
def download_asset(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
) -> None:
    """Download original asset"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'download_asset', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-user-assets-by-device-id")
def get_all_user_assets_by_device_id(
    ctx: typer.Context,
    device_id: str,
) -> None:
    """Retrieve assets by device ID"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['device_id'] = device_id
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'get_all_user_assets_by_device_id', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-asset-info")
def get_asset_info(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
) -> None:
    """Retrieve an asset"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    """Get asset metadata"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    """Retrieve asset metadata by key"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    """Retrieve asset OCR data"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    """Get asset statistics"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    """Get random assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    """Play asset video"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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

@app.command("replace-asset")
def replace_asset(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with multipart fields (non-file)"),
    asset_data: Path = typer.Option(..., "--asset-data", help="File to upload for assetData"),
) -> None:
    """Replace asset"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    json_data = load_json_file(json_path) if json_path is not None else {}
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Run an asset job"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update an asset"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update asset metadata"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.asset_bulk_update_dto import AssetBulkUpdateDto
        asset_bulk_update_dto = deserialize_request_body(json_data, AssetBulkUpdateDto)
        kwargs['asset_bulk_update_dto'] = asset_bulk_update_dto
    client = ctx.obj['client']
    api_group = client.assets
    result = run_command(client, api_group, 'update_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("upload-asset")
def upload_asset(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    x_immich_checksum: str | None = typer.Option(None, "--x-immich-checksum"),
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with multipart fields (non-file)"),
    asset_data: Path = typer.Option(..., "--asset-data", help="File to upload for assetData"),
    sidecar_data: Path | None = typer.Option(None, "--sidecar-data", help="File to upload for sidecarData"),
) -> None:
    """Upload asset"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if x_immich_checksum is not None:
        kwargs['x_immich_checksum'] = x_immich_checksum
    json_data = load_json_file(json_path) if json_path is not None else {}
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
    else:
        missing.append('metadata')
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
    key: str | None = typer.Option(None, "--key"),
    size: str | None = typer.Option(None, "--size"),
    slug: str | None = typer.Option(None, "--slug"),
) -> None:
    """View asset thumbnail"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
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
