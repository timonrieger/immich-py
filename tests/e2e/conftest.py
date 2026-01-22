import os
from pathlib import Path
from typing import AsyncGenerator, Awaitable, Callable, Optional
from uuid import UUID, uuid4

import pytest
from typer.testing import CliRunner

from immich import AsyncClient
from immich.cli.consts import (
    DEFAULT_FORMAT,
    DEFAULT_PROFILE,
    IMMICH_API_KEY,
    IMMICH_API_URL,
    IMMICH_FORMAT,
    IMMICH_PROFILE,
)
from immich.client.utils.upload import UploadResult
from immich.client.generated import (
    AlbumResponseDto,
    AssetBulkDeleteDto,
    AssetResponseDto,
    CreateAlbumDto,
    UserAdminCreateDto,
    UserAdminDeleteDto,
    UserResponseDto,
)
from immich.client.generated.exceptions import BadRequestException
from immich.client.generated.models.admin_onboarding_update_dto import (
    AdminOnboardingUpdateDto,
)
from immich.client.generated.models.api_key_create_dto import APIKeyCreateDto
from immich.client.generated.models.login_credential_dto import LoginCredentialDto
from immich.client.generated.models.permission import Permission
from immich.client.generated.models.sign_up_dto import SignUpDto

ACTIVATION_KEY = "4kJUNUWMq13J14zqPFm1NodRcI6MV6DeOGvQNIgrM8Sc9nv669wyEVvFw1Nz4Kb1W7zLWblOtXEQzpRRqC4r4fKjewJxfbpeo9sEsqAVIfl4Ero-Vp1Dg21-sVdDGZEAy2oeTCXAyCT5d1JqrqR6N1qTAm4xOx9ujXQRFYhjRG8uwudw7_Q49pF18Tj5OEv9qCqElxztoNck4i6O_azsmsoOQrLIENIWPh3EynBN3ESpYERdCgXO8MlWeuG14_V1HbNjnJPZDuvYg__YfMzoOEtfm1sCqEaJ2Ww-BaX7yGfuCL4XsuZlCQQNHjfscy_WywVfIZPKCiW8QR74i0cSzQ"
LICENSE_KEY = "IMSV-6ECZ-91TE-WZRM-Q7AQ-MBN4-UW48-2CPT-71X9"


@pytest.fixture
def env() -> dict[str, str]:
    return {
        IMMICH_API_URL: os.environ.get(IMMICH_API_URL, "http://127.0.0.1:2283/api"),
        IMMICH_API_KEY: os.environ.get(IMMICH_API_KEY, ""),
        IMMICH_FORMAT: "json",
    }


@pytest.fixture
async def client_with_api_key(client_with_access_token: AsyncClient):
    """Set up admin user, create API key, and return authenticated client."""
    # Create API key with all permissions
    api_key_response = await client_with_access_token.api_keys.create_api_key(
        APIKeyCreateDto(name="e2e", permissions=[Permission.ALL]),
    )

    # Create authenticated client with API key
    client = AsyncClient(
        base_url=client_with_access_token.config.host, api_key=api_key_response.secret
    )

    try:
        yield client
    finally:
        await client.close()


@pytest.fixture
async def client_with_access_token(env: dict[str, str]):
    """Set up admin user, create API key, and return authenticated client."""

    # Create unauthenticated client for setup
    setup_client = AsyncClient(base_url=env[IMMICH_API_URL])

    try:
        # Sign up admin (idempotent: subsequent tests will hit "already has an admin")
        try:
            await setup_client.auth.sign_up_admin(
                SignUpDto(
                    email="admin@immich.cloud", name="Immich Admin", password="password"
                )
            )
        except BadRequestException as e:
            if not (e.status == 400 and e.body and "already has an admin" in e.body):
                raise

        # Login to get access token
        login_response = await setup_client.auth.login(
            LoginCredentialDto(email="admin@immich.cloud", password="password")
        )

        client = AsyncClient(
            base_url=env[IMMICH_API_URL], access_token=login_response.access_token
        )

        # Mark admin as onboarded
        await client.system_metadata.update_admin_onboarding(
            # NOTE: type ignore likely a ty issue
            AdminOnboardingUpdateDto(isOnboarded=True),
        )

        try:
            yield client
        finally:
            await client.close()
    finally:
        await setup_client.close()


@pytest.fixture
def runner(client_with_api_key: AsyncClient) -> CliRunner:
    """Typer CliRunner fixture for CLI testing."""
    return CliRunner(
        env={
            IMMICH_API_URL: client_with_api_key.base_client.configuration.host,
            IMMICH_API_KEY: client_with_api_key.base_client.configuration.api_key[
                "api_key"
            ],
            IMMICH_FORMAT: DEFAULT_FORMAT,
            IMMICH_PROFILE: DEFAULT_PROFILE,
        }
    )


@pytest.fixture
def runner_simple() -> CliRunner:
    """Simple Typer CliRunner fixture for CLI testing without client setup."""
    return CliRunner(
        env={IMMICH_FORMAT: DEFAULT_FORMAT, IMMICH_PROFILE: DEFAULT_PROFILE}
    )


@pytest.fixture
async def upload_assets(
    client_with_api_key: AsyncClient,
) -> AsyncGenerator[Callable[..., Awaitable[UploadResult]], None]:
    """Factory fixture: yields an async callable to upload assets and auto-clean them up.

    Example:
        upload_result = await upload_assets([test_image], skip_duplicates=True)
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

    if _uploaded_ids:
        await client_with_api_key.assets.delete_assets(
            AssetBulkDeleteDto(
                ids=_uploaded_ids, force=True
            )  # deletes without moving to trash
        )


@pytest.fixture
async def asset(
    test_image: Path,
    upload_assets: Callable[..., Awaitable[UploadResult]],
) -> AsyncGenerator[AssetResponseDto, None]:
    """Fixture to set up asset for testing.

    Uploads a test image, returns parsed asset object.
    Skips dependent tests if asset upload fails.
    """
    # Set up: Upload asset
    upload_result = await upload_assets([test_image], skip_duplicates=True)
    assert len(upload_result.uploaded) == 1
    asset = upload_result.uploaded[0].asset
    yield asset


@pytest.fixture
async def user(
    client_with_api_key: AsyncClient,
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
    await client_with_api_key.users_admin.delete_user_admin(
        UUID(str(user.id)),
        UserAdminDeleteDto(force=True),
    )


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
    client_with_api_key: AsyncClient,
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

    if _album_id:
        await client_with_api_key.albums.delete_album(_album_id)
