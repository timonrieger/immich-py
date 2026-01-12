"""E2E tests for immich.client_wrapper modules against running Immich server."""

from __future__ import annotations

import base64
import os
from pathlib import Path
from uuid import UUID

import pytest

from immich import AsyncClient
from immich.client.exceptions import BadRequestException
from immich.client.models.admin_onboarding_update_dto import AdminOnboardingUpdateDto
from immich.client.models.api_key_create_dto import APIKeyCreateDto
from immich.client.models.asset_media_size import AssetMediaSize
from immich.client.models.download_info_dto import DownloadInfoDto
from immich.client.models.login_credential_dto import LoginCredentialDto
from immich.client.models.permission import Permission
from immich.client.models.sign_up_dto import SignUpDto

# Minimal 1x1 JPEG (base64) - valid minimal JPEG
JPEG_BASE64 = "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwA/wA=="

# Minimal MP4 (base64) - minimal valid MP4 header
MP4_BASE64 = "AAAAIGZ0eXBtcDQyAAAAAG1wNDJtcDQxaXNvbWF2YzEAAAGhtZGF0AAACrgYF//+q3EXpvebZSLeWLNgg2SPu73gyNjQgLSBjb3JlIDE0OCByMjA1OCBlYjc2Y2U1IC0gSC4yNjQvTVBFRy00IEFWQyBjb2RlYyAtIENvcHlsZWZ0IDIwMDMtMjAxNyAtIGh0dHA6Ly93d3cudmlkZW9sYW4ub3JnL3gyNjQuaHRtbCAtIG9wdGlvbnM6IGNhYmFjPTEgcmVmPTMgZGVibG9jaz0xOjA6MCBhbmFseXNlPTB4MzoweDExMyBtZT1oZXggc3VibWU9NyBwc3k9MSBwc3lfcmQ9MS4wMDowLjAwIG1peGVkX3JlZj0xIG1lX3JhbmdlPTE2IGNocm9tYV9tZT0xIHRyZWxsaXM9MSA4eDhkY3Q9MSBjcW09MCBkZWFkem9uZT0yMSwxMSBmYXN0X3Bza2lwPTEgY2hyb21hX3FwX29mZnNldD0tMiB0aHJlYWRzPTEgbG9va2FoZWFkX3RocmVhZHM9MSBzbGljZWRfdGhyZWFkcz0wIG5yPTAgZGVjaW1hdGU9MSBpbnRlcmxhY2VkPTAgYmx1cmF5X2NvbXBhdD0wIGNvbnN0cmFpbmVkX2ludHJhPTAgYmZyYW1lcz0zIGJfcHlyYW1pZD0yIGJfYWRhcHQ9MSBiX2JpYXM9MCBkaXJlY3Q9MSB3ZWlnaHRiPTEgb3Blbl9nb3A9MCB3ZWlnaHRwPTIga2V5aW50PTI1MCBrZXlpbnRfbWluPTI1IHNjZW5lY3V0PTQwIGludHJhX3JlZnJlc2g9MCByY19sb29rYWhlYWQ9NDAgcmM9Y3JmIG1idHJlZT0xIGNyZj0yMy4wIHFjb21wPTAuNjAgcXBtaW49MCBxcG1heD02OSBxcHN0ZXA9NCBpcF9yYXRpbz0xLjQwIGFxPTE6MS4wMAA="


@pytest.fixture
async def client_with_api_key(tmp_path: Path):
    """Set up admin user, create API key, and return authenticated client."""
    base_url = os.environ.get("IMMICH_API_URL", "http://127.0.0.1:2283/api")

    # Create unauthenticated client for setup
    setup_client = AsyncClient(base_url=base_url)

    try:
        # Sign up admin (idempotent: subsequent tests will hit "already has an admin")
        try:
            await setup_client.authentication.sign_up_admin(
                SignUpDto(
                    email="admin@immich.cloud", name="Immich Admin", password="password"
                )
            )
        except BadRequestException as e:
            if not (e.status == 400 and e.body and "already has an admin" in e.body):
                raise

        # Login to get access token
        login_response = await setup_client.authentication.login(
            LoginCredentialDto(email="admin@immich.cloud", password="password")
        )

        # Mark admin as onboarded
        await setup_client.system_metadata.update_admin_onboarding(
            # NOTE: type ignore likely a ty issue
            AdminOnboardingUpdateDto(is_onboarded=True),  # type: ignore[missing-argument]
            _headers={"Authorization": f"Bearer {login_response.access_token}"},
        )

        # Create API key with all permissions
        api_key_response = await setup_client.api_keys.create_api_key(
            APIKeyCreateDto(name="e2e", permissions=[Permission.ALL]),
            _headers={"Authorization": f"Bearer {login_response.access_token}"},
        )

        # Create authenticated client with API key
        client = AsyncClient(base_url=base_url, api_key=api_key_response.secret)

        yield client

        await client.close()
    finally:
        await setup_client.close()


@pytest.fixture
def test_image(tmp_path: Path) -> Path:
    """Create a minimal JPEG test image."""
    img_path = tmp_path / "test.jpg"
    img_path.write_bytes(base64.b64decode(JPEG_BASE64))
    return img_path


@pytest.fixture
def test_video(tmp_path: Path) -> Path:
    """Create a minimal MP4 test video."""
    vid_path = tmp_path / "test.mp4"
    vid_path.write_bytes(base64.b64decode(MP4_BASE64))
    return vid_path


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_assets_upload(
    client_with_api_key: AsyncClient, test_image: Path, test_video: Path, tmp_path: Path
):
    """Test AssetsApiWrapped.upload method."""
    result = await client_with_api_key.assets.upload(
        [test_image, test_video],
        check_duplicates=True,
        concurrency=2,
        show_progress=False,
    )

    assert result.stats.total == 2
    assert result.stats.uploaded == 2
    assert len(result.uploaded) == 2
    assert len(result.rejected) == 0
    assert len(result.failed) == 0


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_assets_download_asset_to_file(
    client_with_api_key: AsyncClient, test_image: Path, tmp_path: Path
):
    """Test AssetsApiWrapped.download_asset_to_file method."""
    # Upload an asset first
    upload_result = await client_with_api_key.assets.upload(
        [test_image], check_duplicates=True, show_progress=False
    )
    assert len(upload_result.uploaded) == 1
    asset_id = UUID(upload_result.uploaded[0].asset.id)

    # Download the asset
    out_dir = tmp_path / "downloads"
    downloaded_path = await client_with_api_key.assets.download_asset_to_file(
        id=asset_id, out_dir=out_dir, show_progress=False
    )

    assert downloaded_path.exists()
    assert downloaded_path.is_file()
    assert downloaded_path.read_bytes() == test_image.read_bytes()


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_assets_view_asset_to_file(
    client_with_api_key: AsyncClient, test_image: Path, tmp_path: Path
):
    """Test AssetsApiWrapped.view_asset_to_file method."""
    # Upload an asset first
    upload_result = await client_with_api_key.assets.upload(
        [test_image], check_duplicates=True, show_progress=False
    )
    assert len(upload_result.uploaded) == 1
    asset_id = UUID(upload_result.uploaded[0].asset.id)

    # Download thumbnail
    out_dir = tmp_path / "thumbnails"
    thumbnail_path = await client_with_api_key.assets.view_asset_to_file(
        id=asset_id, out_dir=out_dir, size=AssetMediaSize.THUMBNAIL, show_progress=False
    )

    assert thumbnail_path.exists()
    assert thumbnail_path.is_file()


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_assets_play_asset_video_to_file(
    client_with_api_key: AsyncClient, test_video: Path, tmp_path: Path
):
    """Test AssetsApiWrapped.play_asset_video_to_file method."""
    # Upload a video first
    upload_result = await client_with_api_key.assets.upload(
        [test_video], check_duplicates=True, show_progress=False
    )
    assert len(upload_result.uploaded) == 1
    asset_id = UUID(upload_result.uploaded[0].asset.id)

    # Download video stream
    out_dir = tmp_path / "videos"
    video_path = await client_with_api_key.assets.play_asset_video_to_file(
        id=asset_id, out_dir=out_dir, show_progress=False
    )

    assert video_path.exists()
    assert video_path.is_file()


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_download_archive_to_file(
    client_with_api_key: AsyncClient, test_image: Path, tmp_path: Path
):
    """Test DownloadApiWrapped.download_archive_to_file method."""
    # Upload assets first
    upload_result = await client_with_api_key.assets.upload(
        [test_image], check_duplicates=True, show_progress=False
    )
    assert len(upload_result.uploaded) == 1
    asset_id = UUID(upload_result.uploaded[0].asset.id)

    # Create download info
    download_info = DownloadInfoDto(asset_ids=[asset_id])

    # Download archive
    out_dir = tmp_path / "archives"
    archive_paths = await client_with_api_key.download.download_archive_to_file(
        download_info=download_info, out_dir=out_dir, show_progress=False
    )

    assert len(archive_paths) == 1
    assert archive_paths[0].exists()
    assert archive_paths[0].suffix == ".zip"


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_users_get_profile_image_to_file(
    client_with_api_key: AsyncClient, test_image: Path, tmp_path: Path
):
    """Test UsersApiWrapped.get_profile_image_to_file method."""
    # Get current user info
    my_user = await client_with_api_key.users.get_my_user()
    user_id = UUID(my_user.id)

    # Upload profile image
    img_bytes = test_image.read_bytes()
    await client_with_api_key.users.create_profile_image(file=img_bytes)

    # Download profile image
    out_dir = tmp_path / "profiles"
    profile_path = await client_with_api_key.users.get_profile_image_to_file(
        id=user_id, out_dir=out_dir, show_progress=False
    )

    assert profile_path.exists()
    assert profile_path.is_file()
