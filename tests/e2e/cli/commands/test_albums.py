import asyncio
import json
from collections.abc import Awaitable, Callable

import pytest
from typer.testing import CliRunner

from immich.cli.app import app as cli_app
from immich.client import (
    AlbumResponseDto,
    AlbumStatisticsResponseDto,
    AlbumUserCreateDto,
    AlbumUserRole,
    AlbumsAddAssetsResponseDto,
    BulkIdResponseDto,
    CreateAlbumDto,
    UserResponseDto,
)
from immich.client.models.asset_response_dto import AssetResponseDto


@pytest.mark.e2e
def test_create_album(runner: CliRunner, user: UserResponseDto) -> None:
    """Test create-album command with description and validate response structure."""
    album_name = "Test Album with Description"
    description = "Test description"
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "create-album",
            "--albumName",
            album_name,
            "--description",
            description,
            # TODO: find a way in the generator to pass multiple album users at once without stringifying the list
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    album = AlbumResponseDto.model_validate(response_data)
    assert album.album_name == album_name
    assert album.description == description
    assert len(album.album_users) == 0


@pytest.mark.e2e
def test_get_all_albums(runner: CliRunner, album: AlbumResponseDto) -> None:
    """Test get-all-albums command and validate response structure."""
    album_id = album.id
    result = runner.invoke(
        cli_app,
        ["--format", "json", "albums", "get-all-albums"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    albums: list[AlbumResponseDto] = []
    for item in response_data:
        album = AlbumResponseDto.model_validate(item)
        albums.append(album)
    assert any(album.id == album_id for album in albums)


@pytest.mark.asyncio
@pytest.mark.e2e
@pytest.mark.skip(reason="Waiting for CLI support on list objects")
async def test_get_all_albums_with_shared_filter(
    runner: CliRunner,
    user: UserResponseDto,
    album_factory: Callable[..., Awaitable[AlbumResponseDto]],
) -> None:
    """Test get-all-albums command with shared filter and validate response structure."""
    album_users = [AlbumUserCreateDto(role=AlbumUserRole.VIEWER, userId=user.id)]
    request = CreateAlbumDto(albumName="Test Album", albumUsers=album_users)
    album = await album_factory(request.model_dump())
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "get-all-albums",
            "--shared",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    albums: list[AlbumResponseDto] = []
    for item in response_data:
        albums.append(AlbumResponseDto.model_validate(item))
    assert any(a.id == album.id for a in albums)


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_get_all_albums_non_shared_filter(
    runner: CliRunner,
    user: UserResponseDto,
    album_factory: Callable[..., Awaitable[AlbumResponseDto]],
) -> None:
    """Test get-all-albums command with no shared filter and validate response structure."""
    album_users = [AlbumUserCreateDto(role=AlbumUserRole.VIEWER, userId=user.id)]
    request = CreateAlbumDto(albumName="Test Album", albumUsers=album_users)
    album = await album_factory(request.model_dump())
    result = await asyncio.to_thread(
        runner.invoke,
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "get-all-albums",
            "--not-shared",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    albums: list[AlbumResponseDto] = []
    for item in response_data:
        albums.append(AlbumResponseDto.model_validate(item))
    assert all(a.id != album.id for a in albums)


@pytest.mark.e2e
def test_get_album_info(runner: CliRunner, album: AlbumResponseDto) -> None:
    """Test get-album-info command and validate response structure."""
    album_id = album.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "get-album-info",
            album_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    album_info = AlbumResponseDto.model_validate(response_data)
    assert album_info.id == album_id


@pytest.mark.e2e
def test_get_album_statistics(runner: CliRunner) -> None:
    """Test get-album-statistics command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "albums", "get-album-statistics"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    AlbumStatisticsResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_update_album_info(runner: CliRunner, album: AlbumResponseDto) -> None:
    """Test update-album-info command and validate response structure."""
    album_id = album.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "update-album-info",
            album_id,
            "--albumName",
            "Updated Album Name",
            "--description",
            "Updated description",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    updated_album = AlbumResponseDto.model_validate(response_data)
    assert updated_album.id == album_id
    assert updated_album.album_name == "Updated Album Name"
    assert updated_album.description == "Updated description"


@pytest.mark.e2e
def test_add_assets_to_album(
    runner: CliRunner, album: AlbumResponseDto, asset: AssetResponseDto
) -> None:
    """Test add-assets-to-album command and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "add-assets-to-album",
            album.id,
            "--ids",
            asset.id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        response = BulkIdResponseDto.model_validate(item)
        assert response.id in [asset.id]
        assert response.success
        assert response.error is None


@pytest.mark.e2e
def test_add_assets_to_albums(
    runner: CliRunner, album: AlbumResponseDto, asset: AssetResponseDto
) -> None:
    """Test add-assets-to-albums command and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "add-assets-to-albums",
            "--albumIds",
            album.id,
            "--assetIds",
            asset.id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    response = AlbumsAddAssetsResponseDto.model_validate(response_data)
    assert response.success
    assert response.error is None


@pytest.mark.e2e
def test_remove_asset_from_album(
    runner: CliRunner, album: AlbumResponseDto, asset: AssetResponseDto
) -> None:
    """Test remove-asset-from-album command and validate response structure."""
    album_id = album.id
    asset_id = asset.id

    # First add the asset to the album
    add_result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "add-assets-to-album",
            album_id,
            "--ids",
            asset_id,
        ],
    )
    if add_result.exit_code != 0:
        pytest.skip(
            f"Failed to add asset to album: {add_result.stdout + add_result.stderr}"
        )

    # Then remove it
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "remove-asset-from-album",
            album_id,
            "--ids",
            asset_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        response = BulkIdResponseDto.model_validate(item)
        assert response.id in [asset_id]
        assert response.success
        assert response.error is None


@pytest.mark.e2e
@pytest.mark.skip(reason="Waiting for CLI support on list objects")
def test_add_users_to_album(
    runner: CliRunner, album: AlbumResponseDto, user: UserResponseDto
) -> None:
    """Test add-users-to-album command and validate response structure."""
    album_id = album.id

    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "add-users-to-album",
            album_id,
            "--albumUsers",
            f'{{"role": "viewer", "userId": "{user.id}"}}',  # TODO: find a way in the generator to pass multiple album users at once without stringifying the list
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Add users returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None


@pytest.mark.e2e
@pytest.mark.skip(reason="Waiting for CLI support on list objects")
def test_remove_user_from_album(
    runner: CliRunner, album: AlbumResponseDto, user: UserResponseDto
) -> None:
    """Test remove-user-from-album command and validate response structure."""
    # First add the user to the album
    add_result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "add-users-to-album",
            album.id,
            "--albumUsers",
            f'{{"role": "viewer", "userId": "{user.id}"}}',  # TODO: find a way in the generator to pass multiple album users at once without stringifying the list
        ],
    )
    if add_result.exit_code != 0:
        pytest.skip(
            f"Failed to add user to album: {add_result.stdout + add_result.stderr}"
        )

    # Then remove them
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "remove-user-from-album",
            album.id,
            user.id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        response = BulkIdResponseDto.model_validate(item)
        assert response.id in [user.id]
        assert response.success
        assert response.error is None


@pytest.mark.e2e
@pytest.mark.skip(reason="Waiting for CLI support on list objects")
def test_update_album_user(
    runner: CliRunner, album: AlbumResponseDto, user: UserResponseDto
) -> None:
    """Test update-album-user command and validate response structure."""
    # First add the user to the album
    add_result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "add-users-to-album",
            album.id,
            "--albumUsers",
            f'{{"role": "viewer", "userId": "{user.id}"}}',  # TODO: find a way in the generator to pass multiple album users at once without stringifying the list
        ],
    )
    if add_result.exit_code != 0:
        pytest.skip(
            f"Failed to add user to album: {add_result.stdout + add_result.stderr}"
        )

    # Then update their role
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "update-album-user",
            album.id,
            user.id,
            "--role",
            "editor",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Update album user returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None


@pytest.mark.e2e
@pytest.mark.parametrize("teardown", [False])
def test_delete_album(runner: CliRunner, album: AlbumResponseDto) -> None:
    """Test delete-album command and validate response structure."""
    album_id = album.id
    result = runner.invoke(
        cli_app,
        ["--format", "json", "albums", "delete-album", album_id],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Delete returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None
