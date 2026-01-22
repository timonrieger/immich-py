"""Test command with no parameters → Returns data.

This test verifies that commands with no parameters correctly execute and return
data. The generated CLI code should handle commands that don't require any
arguments or options, directly calling the API method and printing the response.

Example command tested: get-all-albums
"""

import json

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import AlbumResponseDto


@pytest.mark.e2e
def test_get_all_albums(
    runner_with_api_key: CliRunner, album: AlbumResponseDto
) -> None:
    """Test get-all-albums command and validate response structure."""
    album_id = album.id
    result = runner_with_api_key.invoke(
        cli_app,
        ["albums", "get-all-albums"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert isinstance(response_data, list)
    albums: list[AlbumResponseDto] = []
    for item in response_data:
        album = AlbumResponseDto.model_validate(item)
        albums.append(album)
    assert any(album.id == album_id for album in albums)
