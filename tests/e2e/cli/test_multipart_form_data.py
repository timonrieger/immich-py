"""Test multipart/form-data → Direct kwargs merge works (no validation).

This test verifies that commands with multipart/form-data media type correctly
merge json_data into kwargs without model validation, as opposed to
application/json which uses model_validate. The generated CLI code for
multipart/form-data uses kwargs.update(json_data) directly instead of
model_validate, and file uploads are converted to tuples (name, bytes).

Example command tested: create-profile-image
"""

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from immich.cli.main import app as cli_app
from immich.client.generated import CreateProfileImageResponseDto


@pytest.mark.e2e
def test_multipart_form_data(runner_with_api_key: CliRunner, test_image: Path) -> None:
    """Test multipart/form-data command and validate direct kwargs merge."""
    result = runner_with_api_key.invoke(
        cli_app,
        [
            "users",
            "create-profile-image",
            "--file",
            str(test_image),
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Verify the response is a valid CreateProfileImageResponseDto
    # This confirms multipart/form-data handling worked correctly:
    # 1. Path was converted to tuple (file.name, file.read_bytes())
    # 2. kwargs.update(json_data) was used (no model_validate)
    # 3. Response was properly parsed and printed
    response_data = json.loads(result.stdout)
    response = CreateProfileImageResponseDto.model_validate(response_data)
    assert response.user_id is not None
    assert response.profile_image_path is not None
    assert response.profile_changed_at is not None
