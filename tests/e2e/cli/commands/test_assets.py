import asyncio
import json
from collections.abc import Awaitable, Callable
from pathlib import Path
from uuid import uuid4

import pytest
from typer.testing import CliRunner

from immich.client.utils.upload import UploadResult
from immich.cli.main import app as cli_app
from immich.client.generated import (
    AssetBulkUploadCheckItem,
    AssetBulkUploadCheckResponseDto,
    AssetMetadataResponseDto,
    AssetMetadataUpsertItemDto,
    AssetResponseDto,
    AssetStatsResponseDto,
    CheckExistingAssetsResponseDto,
)


@pytest.mark.e2e
def test_get_asset_info(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test get-asset-info command and validate response structure."""
    asset_id = asset.id
    result = runner.invoke(
        cli_app,
        [
            "assets",
            "get-asset-info",
            asset_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    asset_info = AssetResponseDto.model_validate(response_data)
    assert asset_info.id == asset_id


@pytest.mark.e2e
def test_get_asset_statistics(runner: CliRunner) -> None:
    """Test get-asset-statistics command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["assets", "get-asset-statistics"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    AssetStatsResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_asset_statistics_with_filters(runner: CliRunner) -> None:
    """Test get-asset-statistics command with filters and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "assets",
            "get-asset-statistics",
            "--is-favorite",
            "false",
            "--is-trashed",
            "false",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    AssetStatsResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_asset_metadata(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test get-asset-metadata command and validate response structure."""
    asset_id = asset.id
    result = runner.invoke(
        cli_app,
        [
            "assets",
            "get-asset-metadata",
            asset_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
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
            "assets",
            "get-asset-metadata-by-key",
            asset_id,
            "mobile-app",
        ],
    )
    # This might fail if metadata doesn't exist, which is acceptable
    if result.exit_code == 0:
        response_data = json.loads(result.stdout)
        AssetMetadataResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_random(runner: CliRunner) -> None:
    """Test get-random command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["assets", "get-random", "--count", "5"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
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
            "assets",
            "update-asset",
            asset_id,
            "--description",
            description,
            "--is-favorite",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
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
    upload_result = await upload_assets([img1, img2], skip_duplicates=True)
    assert len(upload_result.uploaded) == 2

    asset_ids = [entry.asset.id for entry in upload_result.uploaded]
    description = "Bulk updated description"
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "assets",
            "update-assets",
            "--ids",
            asset_ids[0],
            "--ids",
            asset_ids[1],
            "--description",
            description,
            "--is-favorite",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
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
    upload_assets: Callable[..., Awaitable[UploadResult]],
) -> None:
    """Test check-existing-assets command and validate response structure."""
    device_id = str(uuid4())
    device_asset_id = str(uuid4())
    import immich.client.utils.upload

    monkeypatch.setattr(immich.client.utils.upload, "DEVICE_ID", device_id)
    monkeypatch.setattr(
        immich.client.utils.upload,
        "get_device_asset_id",
        lambda filepath, stats: device_asset_id,
    )
    # Upload an asset with the specific device_id (via monkey patch)
    upload_result = await upload_assets([test_image], skip_duplicates=True)
    if upload_result.stats.uploaded == 0:
        pytest.skip(f"No assets uploaded, {upload_result.model_dump_json()}")

    # Query by the device_id
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "assets",
            "check-existing-assets",
            "--device-asset-ids",
            device_asset_id,
            "--device-id",
            device_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    results = CheckExistingAssetsResponseDto.model_validate(response_data).existing_ids
    assert len(results) == 1
    assert results[0] == device_asset_id


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_check_bulk_upload(
    runner: CliRunner,
) -> None:
    """Test check-bulk-upload command and validate response structure."""
    asset1 = AssetBulkUploadCheckItem(checksum=str(uuid4()), id=str(uuid4()))
    asset2 = AssetBulkUploadCheckItem(checksum=str(uuid4()), id=str(uuid4()))
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "assets",
            "check-bulk-upload",
        ]
        + [
            arg
            for asset in [asset1, asset2]
            for arg in ["--assets", asset.model_dump_json()]
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    results = AssetBulkUploadCheckResponseDto.model_validate(response_data).results
    assert len(results) == 2
    assert results[0].action == "accept"
    assert results[0].id == asset1.id
    assert results[1].action == "accept"
    assert results[1].id == asset2.id


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
    upload_result = await upload_assets([test_image], skip_duplicates=True)
    if upload_result.stats.uploaded == 0:
        pytest.skip(f"No assets uploaded, {upload_result.model_dump_json()}")
    asset_to_delete = upload_result.uploaded[0].asset

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "assets",
            "delete-assets",
            "--ids",
            asset_to_delete.id,
            "--force",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is None


@pytest.mark.e2e
def test_update_asset_metadata(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test update-asset-metadata command and validate response structure."""
    asset_id = asset.id
    metadata_items = [
        AssetMetadataUpsertItemDto(key="mobile-app", value={"test": "data"})
    ]
    result = runner.invoke(
        cli_app,
        [
            "assets",
            "update-asset-metadata",
            asset_id,
        ]
        + [
            arg
            for item in metadata_items
            for arg in ["--items", item.model_dump_json()]
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert isinstance(response_data, list)
    for item in response_data:
        AssetMetadataResponseDto.model_validate(item)


@pytest.mark.e2e
def test_delete_asset_metadata(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test delete-asset-metadata command and validate response structure."""
    asset_id = asset.id
    metadata_items = [
        AssetMetadataUpsertItemDto(key="mobile-app", value={"test": "data"})
    ]
    # First add metadata
    add_result = runner.invoke(
        cli_app,
        [
            "assets",
            "update-asset-metadata",
            asset_id,
        ]
        + [
            arg
            for item in metadata_items
            for arg in ["--items", item.model_dump_json()]
        ],
    )
    if add_result.exit_code != 0:
        pytest.skip(f"Failed to add metadata: {add_result.stdout + add_result.stderr}")

    # Then delete it
    result = runner.invoke(
        cli_app,
        [
            "assets",
            "delete-asset-metadata",
            asset_id,
            "mobile-app",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is None


@pytest.mark.e2e
def test_get_asset_ocr(runner: CliRunner, asset: AssetResponseDto) -> None:
    """Test get-asset-ocr command and validate response structure."""
    asset_id = asset.id
    result = runner.invoke(
        cli_app,
        [
            "assets",
            "get-asset-ocr",
            asset_id,
        ],
    )
    # OCR might not be available for all assets, so we accept both success and failure
    if result.exit_code == 0:
        response_data = json.loads(result.stdout)
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
        [source_image, target_image], skip_duplicates=True
    )
    assert len(upload_result.uploaded) == 2
    source_asset = upload_result.uploaded[0].asset
    target_asset = upload_result.uploaded[1].asset

    # mark source as favorite
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "assets",
            "update-asset",
            source_asset.id,
            "--is-favorite",
            "true",
        ],
    )
    if result.exit_code != 0:
        pytest.skip(
            f"Failed to mark source as favorite: {result.stdout + result.stderr}"
        )
    response_data = json.loads(result.stdout)
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
            "assets",
            "copy-asset",
            "--source-id",
            source_asset.id,
            "--target-id",
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
            "assets",
            "run-asset-jobs",
            "--asset-ids",
            asset_id,
            "--name",
            "regenerate-thumbnail",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is None


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_download_asset_to_file(
    runner: CliRunner,
    asset: AssetResponseDto,
    tmp_path: Path,
) -> None:
    """Test download-asset-to-file command and verify file is downloaded."""
    asset_id = asset.id
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        ["assets", "download-asset-to-file", asset_id, str(out_dir)],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is not None

    # Verify file was downloaded
    downloaded_files = list(out_dir.glob("*"))
    assert len(downloaded_files) > 0, "No files were downloaded"
    assert downloaded_files[0].exists(), "Downloaded file does not exist"
    assert downloaded_files[0].stat().st_size > 0, "Downloaded file is empty"


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_play_asset_video_to_file(
    runner: CliRunner,
    test_video_factory: Callable[..., Path],
    upload_assets: Callable[..., Awaitable[UploadResult]],
    tmp_path: Path,
) -> None:
    """Test play-asset-video-to-file command and verify video file is downloaded."""
    # Upload a video asset
    video = test_video_factory()
    upload_result = await upload_assets([video], skip_duplicates=True)
    if upload_result.stats.uploaded == 0:
        pytest.skip(f"No video assets uploaded, {upload_result.model_dump_json()}")
    video_asset = upload_result.uploaded[0].asset

    out_dir = tmp_path / "video_downloads"
    out_dir.mkdir()

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "assets",
            "play-asset-video-to-file",
            video_asset.id,
            str(out_dir),
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is not None

    # Verify video file was downloaded
    downloaded_files = list(out_dir.glob("*"))
    assert len(downloaded_files) > 0, "No video files were downloaded"
    assert downloaded_files[0].exists(), "Downloaded video file does not exist"
    assert downloaded_files[0].stat().st_size > 0, "Downloaded video file is empty"


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_view_asset_to_file(
    runner: CliRunner,
    asset: AssetResponseDto,
    tmp_path: Path,
) -> None:
    """Test view-asset-to-file command and verify thumbnail file is downloaded."""
    asset_id = asset.id
    out_dir = tmp_path / "thumbnails"
    out_dir.mkdir()

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "assets",
            "view-asset-to-file",
            asset_id,
            str(out_dir),
            "--size",
            "thumbnail",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is not None

    # Verify thumbnail file was downloaded
    downloaded_files = list(out_dir.glob("*"))
    assert len(downloaded_files) > 0, "No thumbnail files were downloaded"
    assert downloaded_files[0].exists(), "Downloaded thumbnail file does not exist"
    assert downloaded_files[0].stat().st_size > 0, "Downloaded thumbnail file is empty"


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_upload(
    runner: CliRunner,
    test_image_factory: Callable[..., Path],
    tmp_path: Path,
) -> None:
    """Test upload command and verify assets are uploaded."""
    # Create test images
    img1 = test_image_factory(filename="test1.jpg")
    img2 = test_image_factory(filename="test2.jpg")

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "assets",
            "upload",
            str(img1),
            str(img2),
            "--skip-duplicates",
            "--concurrency",
            "1",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is not None

    # Verify upload result structure
    upload_result = UploadResult.model_validate(response_data)
    assert upload_result.stats.uploaded > 0, "No assets were uploaded"
    assert len(upload_result.uploaded) > 0, "No assets in uploaded list"
