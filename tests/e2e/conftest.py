import json
import os
from pathlib import Path
from uuid import UUID

import pytest
from pydantic import ValidationError
from typer.testing import CliRunner

from immich import AsyncClient
from immich.cli.app import app as cli_app
from immich.client import AlbumResponseDto
from immich.client.exceptions import BadRequestException
from immich.client.models.activity_response_dto import ActivityResponseDto
from immich.client.models.admin_onboarding_update_dto import AdminOnboardingUpdateDto
from immich.client.models.api_key_create_dto import APIKeyCreateDto
from immich.client.models.asset_bulk_delete_dto import AssetBulkDeleteDto
from immich.client.models.login_credential_dto import LoginCredentialDto
from immich.client.models.permission import Permission
from immich.client.models.reaction_type import ReactionType
from immich.client.models.sign_up_dto import SignUpDto

from tests.e2e.client.generators import make_random_image, make_random_video


@pytest.fixture
def env() -> dict[str, str]:
    return {
        "IMMICH_API_URL": os.environ.get("IMMICH_API_URL", "http://127.0.0.1:2283/api"),
        "IMMICH_API_KEY": os.environ.get("IMMICH_API_KEY", ""),
    }


@pytest.fixture
async def client_with_api_key(env: dict[str, str]):
    """Set up admin user, create API key, and return authenticated client."""

    # Create unauthenticated client for setup
    setup_client = AsyncClient(base_url=env["IMMICH_API_URL"])

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
            AdminOnboardingUpdateDto(isOnboarded=True),
            _headers={"Authorization": f"Bearer {login_response.access_token}"},
        )

        # Create API key with all permissions
        api_key_response = await setup_client.api_keys.create_api_key(
            APIKeyCreateDto(name="e2e", permissions=[Permission.ALL]),
            _headers={"Authorization": f"Bearer {login_response.access_token}"},
        )

        # Create authenticated client with API key
        client = AsyncClient(
            base_url=env["IMMICH_API_URL"], api_key=api_key_response.secret
        )

        yield client

        await client.close()
    finally:
        await setup_client.close()


@pytest.fixture
def test_image(tmp_path: Path) -> Path:
    """Create a minimal JPEG test image."""
    img_path = tmp_path / "test.jpg"
    img_path.write_bytes(make_random_image())
    return img_path


@pytest.fixture
def test_video(tmp_path: Path) -> Path:
    """Create a minimal MP4 test video."""
    vid_path = tmp_path / "test.mp4"
    vid_path.write_bytes(make_random_video())
    return vid_path


@pytest.fixture
def asset_cleanup():
    """Fixture to track uploaded assets and profile images for cleanup."""
    cleanup_data: dict[str, list[UUID] | bool] = {
        "asset_ids": [],
        "profile_image": False,
    }
    yield cleanup_data


@pytest.fixture(autouse=True)
async def cleanup_assets_teardown(
    client_with_api_key: AsyncClient, asset_cleanup: dict
):
    """Autouse fixture to clean up uploaded assets after each test."""
    yield

    # Teardown: Clean up all uploaded assets
    asset_ids = asset_cleanup.get("asset_ids", [])
    if asset_ids:
        try:
            await client_with_api_key.assets.delete_assets(
                AssetBulkDeleteDto(ids=asset_ids, force=True)
            )
        except Exception:
            pass  # Ignore cleanup errors

    # Teardown: Clean up profile image if uploaded
    if asset_cleanup.get("profile_image", False):
        try:
            await client_with_api_key.users.delete_profile_image()
        except Exception:
            pass  # Ignore cleanup errors


@pytest.fixture
def runner(client_with_api_key: AsyncClient) -> CliRunner:
    """Typer CliRunner fixture for CLI testing."""
    return CliRunner(
        env={
            "IMMICH_API_URL": client_with_api_key.base_client.configuration.host,
            "IMMICH_API_KEY": client_with_api_key.base_client.configuration.api_key[
                "api_key"
            ],
        }
    )


@pytest.fixture
def album(runner: CliRunner) -> AlbumResponseDto:
    """Fixture to set up album for testing.

    Creates an album, returns parsed album object.
    Skips dependent tests if album creation fails.
    """
    # Set up: Create album
    album_result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "create-album",
            "--albumName",
            "Test Album for Activities",
        ],
    )

    if album_result.exit_code != 0:
        pytest.skip(
            f"Album creation failed:\n{album_result.stdout}{album_result.stderr}"
        )

    try:
        album = AlbumResponseDto.model_validate(json.loads(album_result.output))
    except (ValidationError, json.JSONDecodeError) as e:
        pytest.skip(
            f"Album creation returned invalid JSON:\n{e}\n{album_result.output}"
        )

    yield album

    # Cleanup: Delete album (only runs if we got here, i.e., album parsed successfully)
    if album.id:
        runner.invoke(
            cli_app,
            ["--format", "json", "albums", "delete-album", str(album.id)],
        )


@pytest.fixture
def activity(
    runner: CliRunner, album: AlbumResponseDto, activity_type: ReactionType
) -> ActivityResponseDto:
    """Fixture to set up activity for testing.

    Creates an activity with the specified type, returns parsed activity object.
    Skips dependent tests if activity creation fails.
    """
    # Set up: Create activity
    activity_args = [
        "--format",
        "json",
        "activities",
        "create-activity",
        "--albumId",
        str(album.id),
        "--type",
        activity_type.value,
    ]
    if activity_type == ReactionType.COMMENT:
        activity_args.extend(["--comment", "Test comment"])

    activity_result = runner.invoke(cli_app, activity_args)

    if activity_result.exit_code != 0:
        pytest.skip(
            f"Activity creation failed ({activity_type.value}):\n{activity_result.stdout}{activity_result.stderr}"
        )

    try:
        activity = ActivityResponseDto.model_validate(
            json.loads(activity_result.output)
        )
    except (ValidationError, json.JSONDecodeError) as e:
        pytest.skip(
            f"Activity creation returned invalid JSON:\n{e}\n{activity_result.output}"
        )

    yield activity

    # Cleanup: Delete activity (only runs if we got here, i.e., activity parsed successfully)
    if activity.id:
        runner.invoke(
            cli_app,
            ["--format", "json", "activities", "delete-activity", str(activity.id)],
        )
