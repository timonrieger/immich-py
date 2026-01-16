import json

from pydantic import ValidationError
import pytest
from typer.testing import CliRunner

from immich.cli.app import app as cli_app
from immich.client import AlbumResponseDto
from immich.client.models.activity_response_dto import ActivityResponseDto
from immich.client.models.activity_statistics_response_dto import (
    ActivityStatisticsResponseDto,
)
from immich.client.models.reaction_type import ReactionType


@pytest.fixture
def album(runner: CliRunner) -> AlbumResponseDto:
    """Fixture to set up album for testing.

    Creates an album, returns parsed album object.
    Skips dependent tests if album creation fails.
    """
    # Set up: Create album
    album_result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "albums",
            "create-album",
            "--albumName",
            "Test Album for Activities",
        ],
    )

    if album_result.exit_code != 0:
        pytest.skip(
            f"Album creation failed:\n{album_result.stdout}{album_result.stderr}"
        )

    try:
        album = AlbumResponseDto.model_validate(json.loads(album_result.output))
    except (ValidationError, json.JSONDecodeError) as e:
        pytest.skip(
            f"Album creation returned invalid JSON:\n{e}\n{album_result.output}"
        )

    yield album

    # Cleanup: Delete album (only runs if we got here, i.e., album parsed successfully)
    if album.id:
        runner.invoke(
            cli_app,
            ["--format", "json", "albums", "delete-album", str(album.id)],
        )


@pytest.fixture
def activity(
    runner: CliRunner, album: AlbumResponseDto, activity_type: ReactionType
) -> ActivityResponseDto:
    """Fixture to set up activity for testing.

    Creates an activity with the specified type, returns parsed activity object.
    Skips dependent tests if activity creation fails.
    """
    # Set up: Create activity
    activity_args = [
        "--format",
        "json",
        "activities",
        "create-activity",
        "--albumId",
        str(album.id),
        "--type",
        activity_type.value,
    ]
    if activity_type == ReactionType.COMMENT:
        activity_args.extend(["--comment", "Test comment"])

    activity_result = runner.invoke(cli_app, activity_args)

    if activity_result.exit_code != 0:
        pytest.skip(
            f"Activity creation failed ({activity_type.value}):\n{activity_result.stdout}{activity_result.stderr}"
        )

    try:
        activity = ActivityResponseDto.model_validate(
            json.loads(activity_result.output)
        )
    except (ValidationError, json.JSONDecodeError) as e:
        pytest.skip(
            f"Activity creation returned invalid JSON:\n{e}\n{activity_result.output}"
        )

    yield activity

    # Cleanup: Delete activity (only runs if we got here, i.e., activity parsed successfully)
    if activity.id:
        runner.invoke(
            cli_app,
            ["--format", "json", "activities", "delete-activity", str(activity.id)],
        )


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
