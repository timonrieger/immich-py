import os
from pathlib import Path
from typing import AsyncGenerator, Awaitable, Callable, Optional
from uuid import UUID, uuid4

import pytest

from immich import AsyncClient
from immich._internal.upload import UploadResult
from immich.client import (
    ActivityCreateDto,
    ActivityResponseDto,
    AlbumResponseDto,
    AssetBulkDeleteDto,
    AssetResponseDto,
    CreateAlbumDto,
    LicenseKeyDto,
    LicenseResponseDto,
    ReactionType,
    UserAdminCreateDto,
    UserResponseDto,
)
from immich.client.exceptions import BadRequestException
from immich.client.models.admin_onboarding_update_dto import AdminOnboardingUpdateDto
from immich.client.models.api_key_create_dto import APIKeyCreateDto
from immich.client.models.login_credential_dto import LoginCredentialDto
from immich.client.models.permission import Permission
from immich.client.models.sign_up_dto import SignUpDto
from immich.client.models.user_admin_delete_dto import UserAdminDeleteDto

from tests.e2e.client.generators import make_random_image, make_random_video

ACTIVATION_KEY = "4kJUNUWMq13J14zqPFm1NodRcI6MV6DeOGvQNIgrM8Sc9nv669wyEVvFw1Nz4Kb1W7zLWblOtXEQzpRRqC4r4fKjewJxfbpeo9sEsqAVIfl4Ero-Vp1Dg21-sVdDGZEAy2oeTCXAyCT5d1JqrqR6N1qTAm4xOx9ujXQRFYhjRG8uwudw7_Q49pF18Tj5OEv9qCqElxztoNck4i6O_azsmsoOQrLIENIWPh3EynBN3ESpYERdCgXO8MlWeuG14_V1HbNjnJPZDuvYg__YfMzoOEtfm1sCqEaJ2Ww-BaX7yGfuCL4XsuZlCQQNHjfscy_WywVfIZPKCiW8QR74i0cSzQ"
LICENSE_KEY = "IMSV-6ECZ-91TE-WZRM-Q7AQ-MBN4-UW48-2CPT-71X9"


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
async def album(
    album_factory: Callable[..., Awaitable[AlbumResponseDto]],
) -> AsyncGenerator[AlbumResponseDto, None]:
    """Fixture to set up album for testing.

    Creates an album, returns parsed album object.
    Skips dependent tests if album creation fails.
    """
    request = CreateAlbumDto(albumName="Test Album")
    yield await album_factory(request.model_dump())


@pytest.fixture
async def album_factory(
    client_with_api_key: AsyncClient, teardown: bool
) -> AsyncGenerator[Callable[..., Awaitable[AlbumResponseDto]], None]:
    """Fixture to set up album for testing with factory pattern.

    Creates an album, returns parsed album object.
    Skips dependent tests if album creation fails.
    """
    _album_id: Optional[UUID] = None

    async def _create_album(*args, **kwargs) -> AlbumResponseDto:
        nonlocal _album_id
        try:
            result = await client_with_api_key.albums.create_album(*args, **kwargs)
        except Exception as e:
            pytest.skip(f"Asset upload failed:\n{e}")

        _album_id = UUID(str(result.id))
        return result

    yield _create_album

    if teardown and _album_id:
        await client_with_api_key.albums.delete_album(_album_id)


@pytest.fixture
def teardown(request: pytest.FixtureRequest) -> bool:
    """Fixture to control whether teardown should be performed.

    Can be parametrized in tests to override the default True value.
    """
    # Check if teardown was parametrized
    if hasattr(request, "param"):
        return request.param
    return True


@pytest.fixture
async def activity(
    client_with_api_key: AsyncClient,
    album: AlbumResponseDto,
    activity_type: ReactionType,
    teardown: bool,
) -> AsyncGenerator[ActivityResponseDto, None]:
    """Fixture to set up activity for testing.

    Creates an activity with the specified type, returns parsed activity object.
    Skips dependent tests if activity creation fails.
    """
    # Set up: Create activity
    activity = await client_with_api_key.activities.create_activity(
        ActivityCreateDto(
            albumId=UUID(str(album.id)),
            type=activity_type,
            comment="Test comment" if activity_type == ReactionType.COMMENT else None,
        )
    )
    yield activity
    if teardown:
        await client_with_api_key.activities.delete_activity(UUID(str(activity.id)))


@pytest.fixture
async def license(
    client_with_api_key: AsyncClient, teardown: bool
) -> AsyncGenerator[LicenseResponseDto, None]:
    """Fixture to set up license for testing.

    Sets a license, returns parsed license object.
    Skips dependent tests if license setup fails.
    Note: This requires valid license keys. Tests may skip if license keys are not available.
    """
    license = await client_with_api_key.server.set_server_license(
        LicenseKeyDto(licenseKey=LICENSE_KEY, activationKey=ACTIVATION_KEY)
    )
    yield license
    if teardown:
        await client_with_api_key.server.delete_server_license()


@pytest.fixture
async def upload_assets(
    client_with_api_key: AsyncClient,
    teardown: bool,
) -> AsyncGenerator[Callable[..., Awaitable[UploadResult]], None]:
    """Factory fixture: yields an async callable to upload assets and auto-clean them up.

    Example:
        upload_result = await upload_assets([test_image], check_duplicates=False, show_progress=False)
    """

    _uploaded_ids: list[UUID] = []

    async def _upload(*args, **kwargs) -> UploadResult:
        nonlocal _uploaded_ids
        try:
            result = await client_with_api_key.assets.upload(*args, **kwargs)
        except Exception as e:
            pytest.skip(f"Asset upload failed:\n{e}")

        _uploaded_ids.extend(UUID(u.asset.id) for u in result.uploaded)
        return result

    yield _upload

    if teardown and _uploaded_ids:
        await client_with_api_key.assets.delete_assets(
            AssetBulkDeleteDto(ids=_uploaded_ids, force=True)
        )


@pytest.fixture
async def asset(
    test_image: Path,
    upload_assets: Callable[..., Awaitable[UploadResult]],
    teardown: bool,
) -> AsyncGenerator[AssetResponseDto, None]:
    """Fixture to set up asset for testing.

    Uploads a test image, returns parsed asset object.
    Skips dependent tests if asset upload fails.
    """
    # Set up: Upload asset
    upload_result = await upload_assets(
        [test_image], check_duplicates=False, show_progress=False
    )
    assert len(upload_result.uploaded) == 1
    asset = upload_result.uploaded[0].asset
    yield asset
    # Teardown is handled by upload_assets fixture


@pytest.fixture
async def user(
    client_with_api_key: AsyncClient, teardown: bool
) -> AsyncGenerator[UserResponseDto, None]:
    """Fixture to set up user for testing.

    Creates a user, returns parsed user object.
    Skips dependent tests if user creation fails.
    """
    uuid = uuid4()
    user = await client_with_api_key.users_admin.create_user_admin(
        UserAdminCreateDto(
            email=f"test_{uuid}@immich.cloud",
            password="password",
            name=f"Test User {uuid}",
        )
    )
    yield user
    if teardown:
        await client_with_api_key.users_admin.delete_user_admin(
            UUID(str(user.id)),
            UserAdminDeleteDto(force=True),
        )
