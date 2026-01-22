"""Test command with complex body type → JSON parsing + set_nested works.

This test verifies that commands with complex body types (objects, arrays of
objects) correctly parse JSON strings using json.loads before calling set_nested.
Complex types are identified by is_complex_type() and are handled by parsing
each JSON string in the list before setting the nested value.

Example command tested: check-bulk-upload
"""

import asyncio
import json
from uuid import uuid4

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import (
    AssetBulkUploadCheckItem,
    AssetBulkUploadCheckResponseDto,
)


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_check_bulk_upload(
    runner_with_api_key: CliRunner,
) -> None:
    """Test check-bulk-upload command and validate response structure."""
    asset1 = AssetBulkUploadCheckItem(checksum=str(uuid4()), id=str(uuid4()))
    asset2 = AssetBulkUploadCheckItem(checksum=str(uuid4()), id=str(uuid4()))
    result = await asyncio.to_thread(
        runner_with_api_key.invoke,
        cli_app,
        [
            "assets",
            "check-bulk-upload",
        ]
        + [
            arg
            for asset in [asset1, asset2]
            for arg in ["--assets", asset.model_dump_json()]
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    results = AssetBulkUploadCheckResponseDto.model_validate(response_data).results
    assert len(results) == 2
    assert results[0].action == "accept"
    assert results[0].id == asset1.id
    assert results[1].action == "accept"
    assert results[1].id == asset2.id
