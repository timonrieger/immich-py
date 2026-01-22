"""Test command with optional body params → Conditional set_nested works.

This test verifies that commands with optional body parameters correctly use
conditional set_nested (only when the parameter is not None) to build the JSON
data structure. Optional body params are wrapped in an if statement before
calling set_nested, allowing partial updates to request bodies.

Example command tested: update-album-info
"""

import json

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import AlbumResponseDto


@pytest.mark.e2e
def test_update_album_info(
    runner_with_api_key: CliRunner, album: AlbumResponseDto
) -> None:
    """Test update-album-info command and validate response structure."""
    album_id = album.id
    result = runner_with_api_key.invoke(
        cli_app,
        [
            "albums",
            "update-album-info",
            album_id,
            "--album-name",
            "Updated Album Name",
            "--description",
            "Updated description",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    updated_album = AlbumResponseDto.model_validate(response_data)
    assert updated_album.id == album_id
    assert updated_album.album_name == "Updated Album Name"
    assert updated_album.description == "Updated description"
