"""Test command with path param only → Returns data.

This test verifies that commands with path parameters (typer.Argument) correctly
assign the path parameter directly to kwargs and execute the API call. Path
parameters are always required and are added directly without conditional checks.

Example command tested: get-album-info
"""

import json

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import AlbumResponseDto


@pytest.mark.e2e
def test_get_album_info(
    runner_with_api_key: CliRunner, album: AlbumResponseDto
) -> None:
    """Test get-album-info command and validate response structure."""
    album_id = album.id
    result = runner_with_api_key.invoke(
        cli_app,
        [
            "albums",
            "get-album-info",
            album_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    album_info = AlbumResponseDto.model_validate(response_data)
    assert album_info.id == album_id
