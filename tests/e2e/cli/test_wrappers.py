import asyncio
import json
from pathlib import Path
from typing import Awaitable, Callable

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import AssetResponseDto, CreateProfileImageResponseDto
from immich.client.utils.upload import UploadResult


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


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_download_archive_to_file(
    runner: CliRunner,
    asset: AssetResponseDto,
    tmp_path: Path,
) -> None:
    """Test download-archive-to-file command and verify archive is downloaded."""
    asset_id = asset.id
    out_dir = tmp_path / "archives"
    out_dir.mkdir()

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "download",
            "download-archive-to-file",
            str(out_dir),
            "--asset-ids",
            asset_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is not None

    # Verify archive file was downloaded
    downloaded_files = list(out_dir.glob("*"))
    assert len(downloaded_files) > 0, "No archive files were downloaded"
    assert downloaded_files[0].exists(), "Downloaded archive file does not exist"
    assert downloaded_files[0].stat().st_size > 0, "Downloaded archive file is empty"
    assert downloaded_files[0].suffix == ".zip", "Downloaded file is not a ZIP archive"


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_users_get_profile_image_to_file(
    runner: CliRunner,
    test_image: Path,
    tmp_path: Path,
) -> None:
    """Test users-get-profile-image-to-file command and verify profile image is downloaded."""
    # First, create a profile image for the current user
    create_result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "users",
            "create-profile-image",
            "--file",
            str(test_image),
        ],
    )
    assert create_result.exit_code == 0, create_result.stdout + create_result.stderr
    create_response_data = json.loads(create_result.stdout)
    create_response = CreateProfileImageResponseDto.model_validate(create_response_data)
    user_id = create_response.user_id

    # Now download the profile image
    out_dir = tmp_path / "profile_images"
    out_dir.mkdir()

    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "users",
            "get-profile-image-to-file",
            user_id,
            str(out_dir),
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert response_data is not None

    # Verify profile image file was downloaded
    downloaded_files = list(out_dir.glob("*"))
    assert len(downloaded_files) > 0, "No profile image files were downloaded"
    assert downloaded_files[0].exists(), "Downloaded profile image file does not exist"
    assert downloaded_files[0].stat().st_size > 0, (
        "Downloaded profile image file is empty"
    )
