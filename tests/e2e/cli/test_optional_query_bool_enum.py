"""Test command with optional query bool enum → String-to-bool conversion works.

This test verifies that optional boolean query parameters are correctly converted
from string literals ("true"/"false") to actual boolean values. The generated
CLI code uses Literal["true", "false"] | None for optional bool query params
and converts them using .lower() == 'true' before adding to kwargs.

Example command tested: get-all-albums with --shared "true"
"""

import asyncio
import json
from collections.abc import Awaitable, Callable
from uuid import UUID

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import (
    AlbumResponseDto,
    AlbumUserCreateDto,
    AlbumUserRole,
    CreateAlbumDto,
    UserResponseDto,
)


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_get_all_albums_with_shared_filter(
    runner_with_api_key: CliRunner,
    user: UserResponseDto,
    album_factory: Callable[..., Awaitable[AlbumResponseDto]],
) -> None:
    """Test get-all-albums command with shared filter and validate response structure."""
    album_users = [
        AlbumUserCreateDto(role=AlbumUserRole.VIEWER, userId=UUID(str(user.id)))
    ]
    request = CreateAlbumDto(albumName="Test Album", album_users=album_users)
    album = await album_factory(request.model_dump())
    result = await asyncio.to_thread(
        runner_with_api_key.invoke,
        cli_app,
        [
            "albums",
            "get-all-albums",
            "--shared",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert isinstance(response_data, list)
    albums: list[AlbumResponseDto] = []
    for item in response_data:
        albums.append(AlbumResponseDto.model_validate(item))
    assert any(a.id == album.id for a in albums)
