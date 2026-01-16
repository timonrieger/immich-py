import json

import pytest
from typer.testing import CliRunner

from immich.cli.app import app as cli_app
from immich.client import AlbumResponseDto
from immich.client.models.activity_response_dto import ActivityResponseDto
from immich.client.models.activity_statistics_response_dto import (
    ActivityStatisticsResponseDto,
)
from immich.client.models.reaction_type import ReactionType


@pytest.mark.e2e
@pytest.mark.parametrize("activity_type", [ReactionType.LIKE, ReactionType.COMMENT])
def test_create_activity(
    activity: ActivityResponseDto, activity_type: ReactionType
) -> None:
    """Test create-activity command with different activity types and validate response structure."""
    assert activity.type == activity_type.value
    if activity_type == ReactionType.COMMENT:
        assert activity.comment == "Test comment"


@pytest.mark.e2e
@pytest.mark.parametrize("activity_type", [ReactionType.LIKE])
def test_delete_activity(runner: CliRunner, activity: ActivityResponseDto) -> None:
    """Test delete-activity command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "activities", "delete-activity", str(activity.id)],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Delete returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None


@pytest.mark.e2e
def test_get_activities(runner: CliRunner, album: AlbumResponseDto) -> None:
    """Test get-activities command and validate response structure."""
    album_id = album.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "activities",
            "get-activities",
            "--album-id",
            album_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        ActivityResponseDto.model_validate(item)


@pytest.mark.e2e
def test_get_activities_with_filters(
    runner: CliRunner, album: AlbumResponseDto
) -> None:
    """Test get-activities command with optional filters and validate response structure."""
    album_id = album.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "activities",
            "get-activities",
            "--album-id",
            album_id,
            "--type",
            "like",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        activity = ActivityResponseDto.model_validate(item)
        assert activity.type == "like"


@pytest.mark.e2e
def test_get_activity_statistics(runner: CliRunner, album: AlbumResponseDto) -> None:
    """Test get-activity-statistics command and validate response structure."""
    album_id = album.id
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "activities",
            "get-activity-statistics",
            "--album-id",
            album_id,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ActivityStatisticsResponseDto.model_validate(response_data)
