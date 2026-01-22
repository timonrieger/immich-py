"""Test command with required body params → set_nested + model_validate works.

This test verifies that commands with required body parameters correctly use
set_nested to build the JSON data structure and then use model_validate to
create the Pydantic model instance before passing it to the API call. Required
body params are always added to json_data via set_nested, and the final
json_data is validated into a model for application/json requests.

Example command tested: create-album
"""

import json
from uuid import UUID

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import (
    AlbumResponseDto,
    AlbumUserCreateDto,
    AlbumUserRole,
    UserResponseDto,
)


@pytest.mark.e2e
def test_create_album(runner_with_api_key: CliRunner, user: UserResponseDto) -> None:
    """Test create-album command with description and validate response structure."""
    album_name = "Test Album with Description"
    description = "Test description"
    album_users = [
        AlbumUserCreateDto(role=AlbumUserRole.EDITOR, userId=UUID(str(user.id)))
    ]
    result = runner_with_api_key.invoke(
        cli_app,
        [
            "albums",
            "create-album",
            "--album-name",
            album_name,
            "--description",
            description,
        ]
        + [
            arg
            for user in album_users
            for arg in ["--album-users", user.model_dump_json()]
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    album = AlbumResponseDto.model_validate(response_data)
    assert album.album_name == album_name
    assert album.description == description
    assert len(album.album_users) == 1
    assert album.album_users[0].role == AlbumUserRole.EDITOR
    assert album.album_users[0].user.id == user.id
