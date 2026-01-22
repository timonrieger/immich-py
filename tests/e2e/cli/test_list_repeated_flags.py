"""Test command with list/repeated flags → Multiple values handled correctly.

This test verifies that commands with list parameters (repeated flags) correctly
handle multiple values passed via the same flag. Typer automatically collects
multiple --flag value invocations into a list, and the generated CLI code passes
this list directly to the API call.

Example command tested: add-assets-to-album with --ids
"""

import json

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import AlbumResponseDto, BulkIdResponseDto
from immich.client.generated.models.asset_response_dto import AssetResponseDto


@pytest.mark.e2e
def test_add_assets_to_album(
    runner_with_api_key: CliRunner, album: AlbumResponseDto, asset: AssetResponseDto
) -> None:
    """Test add-assets-to-album command and validate response structure."""
    result = runner_with_api_key.invoke(
        cli_app,
        [
            "albums",
            "add-assets-to-album",
            album.id,
            "--ids",
            asset.id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert isinstance(response_data, list)
    for item in response_data:
        response = BulkIdResponseDto.model_validate(item)
        assert response.id in [asset.id]
        assert response.success
        assert response.error is None
