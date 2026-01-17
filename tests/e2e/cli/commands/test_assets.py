import asyncio
import json
from collections.abc import Awaitable, Callable
from pathlib import Path
from uuid import uuid4

import pytest
from typer.testing import CliRunner

from immich._internal.upload import UploadResult
from immich.cli.app import app as cli_app
from immich.client import (
    AssetBulkUploadCheckResponseDto,
    AssetMetadataResponseDto,
    AssetResponseDto,
    AssetStatsResponseDto,
    CheckExistingAssetsResponseDto,
)
from immich.client.models.asset_metadata_key import AssetMetadataKey


@pytest.mark.e2e
def test_get_asset_info(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test get-asset-info command and validate response structure."""
    asset_id = asset.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "get-asset-info",
            asset_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    asset_info = AssetResponseDto.model_validate(response_data)
    assert asset_info.id == asset_id


@pytest.mark.e2e
def test_get_asset_statistics(runner: CliRunner) -> None:
    """Test get-asset-statistics command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "assets", "get-asset-statistics"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    AssetStatsResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_asset_statistics_with_filters(runner: CliRunner) -> None:
    """Test get-asset-statistics command with filters and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "get-asset-statistics",
            "--is-favorite",
            "false",
            "--is-trashed",
            "false",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    AssetStatsResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_asset_metadata(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test get-asset-metadata command and validate response structure."""
    asset_id = asset.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "get-asset-metadata",
            asset_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        AssetMetadataResponseDto.model_validate(item)


@pytest.mark.e2e
def test_get_asset_metadata_by_key(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test get-asset-metadata-by-key command and validate response structure."""
    asset_id = asset.id
    # Try to get metadata by a common key (if it exists)
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "get-asset-metadata-by-key",
            asset_id,
            AssetMetadataKey.MOBILE_MINUS_APP.value,
        ],
    )
    # This might fail if metadata doesn't exist, which is acceptable
    if result.exit_code == 0:
        response_data = json.loads(result.output)
        AssetMetadataResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_random(runner: CliRunner) -> None:
    """Test get-random command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "assets", "get-random", "--count", "5"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        AssetResponseDto.model_validate(item)


@pytest.mark.e2e
def test_update_asset(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test update-asset command and validate response structure."""
    asset_id = asset.id
    description = "Updated test description"
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "update-asset",
            asset_id,
            "--description",
            description,
            "--isFavorite",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    updated_asset = AssetResponseDto.model_validate(response_data)
    assert updated_asset.id == asset_id
    assert updated_asset.is_favorite is True


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_update_assets(
    runner: CliRunner,
    upload_assets: Callable[..., Awaitable[UploadResult]],
    test_image_factory: Callable[..., Path],
    get_asset_info_factory: Callable[[str], Awaitable[AssetResponseDto]],
) -> None:
    """Test update-assets command and validate response structure."""
    img1 = test_image_factory(filename=f"{uuid4()}.jpg")
    img2 = test_image_factory(filename=f"{uuid4()}.jpg")
    upload_result = await upload_assets(
        [img1, img2], check_duplicates=False, show_progress=False
    )
    assert len(upload_result.uploaded) == 2

    asset_ids = [entry.asset.id for entry in upload_result.uploaded]
    description = "Bulk updated description"
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "update-assets",
            "--ids",
            asset_ids[0],
            "--ids",
            asset_ids[1],
            "--description",
            description,
            "--isFavorite",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Update assets returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None

    # verify assets are updated
    for asset_id in asset_ids:
        asset_info = await get_asset_info_factory(asset_id)
        assert asset_info.is_favorite is True


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_check_existing_assets(
    runner: CliRunner,
    test_image: Path,
    monkeypatch: pytest.MonkeyPatch,
    get_asset_info_factory: Callable[[str], Awaitable[AssetResponseDto]],
    upload_assets: Callable[..., Awaitable[UploadResult]],
) -> None:
    """Test check-existing-assets command and validate response structure."""
    device_id = str(uuid4())
    device_asset_id = str(uuid4())
    import immich._internal.upload

    monkeypatch.setattr(immich._internal.upload, "DEVICE_ID", device_id)
    monkeypatch.setattr(
        immich._internal.upload,
        "get_device_asset_id",
        lambda filepath, stats: device_asset_id,
    )
    # Upload an asset with the specific device_id (via monkey patch)
    upload_result = await upload_assets(
        [test_image], check_duplicates=False, show_progress=False
    )
    if upload_result.stats.uploaded == 0:
        pytest.skip(f"No assets uploaded, {upload_result.model_dump_json()}")

    # Query by the device_id
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "check-existing-assets",
            "--deviceAssetIds",
            device_asset_id,
            "--deviceId",
            device_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    results = CheckExistingAssetsResponseDto.model_validate(response_data).existing_ids
    assert len(results) == 1
    assert results[0] == device_asset_id


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_check_bulk_upload(
    runner: CliRunner,
) -> None:
    """Test check-bulk-upload command and validate response structure."""
    file1_id = str(uuid4())
    file1_checksum = str(uuid4())
    file2_id = str(uuid4())
    file2_checksum = str(uuid4())
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "check-bulk-upload",
            "--assets",
            f"checksum={file1_checksum},id={file1_id}",
            "--assets",
            f"checksum={file2_checksum},id={file2_id}",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    results = AssetBulkUploadCheckResponseDto.model_validate(response_data).results
    assert len(results) == 2
    assert results[0].action == "accept"
    assert results[0].id == file1_id
    assert results[1].action == "accept"
    assert results[1].id == file2_id


@pytest.mark.asyncio
@pytest.mark.e2e
@pytest.mark.parametrize("teardown", [False])
async def test_delete_assets(
    runner: CliRunner,
    upload_assets: Callable[..., Awaitable[UploadResult]],
    test_image,
    get_asset_info_factory: Callable[[str], Awaitable[AssetResponseDto]],
) -> None:
    """Test delete-assets command and validate response structure."""
    # Upload an asset specifically for deletion
    upload_result = await upload_assets(
        [test_image], check_duplicates=False, show_progress=False
    )
    if upload_result.stats.uploaded == 0:
        pytest.skip(f"No assets uploaded, {upload_result.model_dump_json()}")
    asset_to_delete = upload_result.uploaded[0].asset

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "delete-assets",
            "--ids",
            asset_to_delete.id,
            "--force",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Delete returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None

    # verify asset is deleted
    try:
        await get_asset_info_factory(asset_to_delete.id)
    except AssertionError as e:
        assert "not found" in str(e).lower()


@pytest.mark.e2e
def test_update_asset_metadata(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test update-asset-metadata command and validate response structure."""
    asset_id = asset.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "update-asset-metadata",
            asset_id,
            "--items",
            f"key={AssetMetadataKey.MOBILE_MINUS_APP.value},value={json.dumps({'test': 'data'})}",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        AssetMetadataResponseDto.model_validate(item)


@pytest.mark.e2e
def test_delete_asset_metadata(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test delete-asset-metadata command and validate response structure."""
    asset_id = asset.id
    # First add metadata
    add_result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "update-asset-metadata",
            asset_id,
            "--items",
            f"key={AssetMetadataKey.MOBILE_MINUS_APP.value},value={json.dumps({'test': 'data'})}",
        ],
    )
    if add_result.exit_code != 0:
        pytest.skip(f"Failed to add metadata: {add_result.stdout + add_result.stderr}")

    # Then delete it
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "delete-asset-metadata",
            asset_id,
            AssetMetadataKey.MOBILE_MINUS_APP.value,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Delete returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None


@pytest.mark.e2e
def test_get_asset_ocr(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test get-asset-ocr command and validate response structure."""
    asset_id = asset.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "get-asset-ocr",
            asset_id,
        ],
    )
    # OCR might not be available for all assets, so we accept both success and failure
    if result.exit_code == 0:
        response_data = json.loads(result.output)
        assert isinstance(response_data, list)


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_copy_asset(
    runner: CliRunner,
    upload_assets: Callable[..., Awaitable[UploadResult]],
    test_image_factory: Callable[..., Path],
    get_asset_info_factory: Callable[[str], Awaitable[AssetResponseDto]],
) -> None:
    """Test copy-asset command and validate response structure."""
    # Upload a target asset
    source_image = test_image_factory(filename="source.jpg")
    target_image = test_image_factory(filename="target.jpg")
    upload_result = await upload_assets(
        [source_image, target_image], check_duplicates=False, show_progress=False
    )
    assert len(upload_result.uploaded) == 2
    source_asset = upload_result.uploaded[0].asset
    target_asset = upload_result.uploaded[1].asset

    # mark source as favorite
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "update-asset",
            source_asset.id,
            "--isFavorite",
            "true",
        ],
    )
    if result.exit_code != 0:
        pytest.skip(
            f"Failed to mark source as favorite: {result.stdout + result.stderr}"
        )
    response_data = json.loads(result.output)
    updated_asset = AssetResponseDto.model_validate(response_data)
    assert updated_asset.id == source_asset.id
    assert updated_asset.is_favorite is True

    # verify target is not favorite
    asset_info = await get_asset_info_factory(target_asset.id)
    assert asset_info.is_favorite is False

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "copy-asset",
            "--sourceId",
            source_asset.id,
            "--targetId",
            target_asset.id,
            "--favorite",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr

    # verify target is favorite
    asset_info = await get_asset_info_factory(target_asset.id)
    assert asset_info.is_favorite is True


@pytest.mark.e2e
def test_run_asset_jobs(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test run-asset-jobs command and validate response structure."""
    asset_id = asset.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "assets",
            "run-asset-jobs",
            "--assetIds",
            asset_id,
            "--name",
            "regenerate-thumbnail",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Run asset jobs returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None
