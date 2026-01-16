import json

from click.testing import Result
import pytest
from typer.testing import CliRunner

from immich.cli.app import app as cli_app
from immich.client.models.server_about_response_dto import ServerAboutResponseDto
from immich.client.models.server_apk_links_dto import ServerApkLinksDto
from immich.client.models.server_config_dto import ServerConfigDto
from immich.client.models.server_features_dto import ServerFeaturesDto
from immich.client.models.server_media_types_response_dto import (
    ServerMediaTypesResponseDto,
)
from immich.client.models.server_ping_response import ServerPingResponse
from immich.client.models.server_stats_response_dto import ServerStatsResponseDto
from immich.client.models.server_storage_response_dto import ServerStorageResponseDto
from immich.client.models.server_theme_dto import ServerThemeDto
from immich.client.models.server_version_history_response_dto import (
    ServerVersionHistoryResponseDto,
)
from immich.client.models.server_version_response_dto import ServerVersionResponseDto
from immich.client.models.version_check_state_response_dto import (
    VersionCheckStateResponseDto,
)
from immich.client.models.license_response_dto import LicenseResponseDto


@pytest.mark.e2e
def test_get_about_info(runner: CliRunner) -> None:
    """Test get-about-info command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-about-info"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerAboutResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_apk_links(runner: CliRunner) -> None:
    """Test get-apk-links command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-apk-links"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerApkLinksDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_server_config(runner: CliRunner) -> None:
    """Test get-server-config command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-server-config"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerConfigDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_server_features(runner: CliRunner) -> None:
    """Test get-server-features command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-server-features"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerFeaturesDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_server_statistics(runner: CliRunner) -> None:
    """Test get-server-statistics command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-server-statistics"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerStatsResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_server_version(runner: CliRunner) -> None:
    """Test get-server-version command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-server-version"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerVersionResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_storage(runner: CliRunner) -> None:
    """Test get-storage command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-storage"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerStorageResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_supported_media_types(runner: CliRunner) -> None:
    """Test get-supported-media-types command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-supported-media-types"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerMediaTypesResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_theme(runner: CliRunner) -> None:
    """Test get-theme command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-theme"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerThemeDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_version_check(runner: CliRunner) -> None:
    """Test get-version-check command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-version-check"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    VersionCheckStateResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_version_history(runner: CliRunner) -> None:
    """Test get-version-history command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-version-history"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert isinstance(response_data, list)
    for item in response_data:
        ServerVersionHistoryResponseDto.model_validate(item)


@pytest.mark.e2e
def test_ping_server(runner: CliRunner) -> None:
    """Test ping-server command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "ping-server"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ServerPingResponse.model_validate(response_data)


ACTIVATION_KEY = "4kJUNUWMq13J14zqPFm1NodRcI6MV6DeOGvQNIgrM8Sc9nv669wyEVvFw1Nz4Kb1W7zLWblOtXEQzpRRqC4r4fKjewJxfbpeo9sEsqAVIfl4Ero-Vp1Dg21-sVdDGZEAy2oeTCXAyCT5d1JqrqR6N1qTAm4xOx9ujXQRFYhjRG8uwudw7_Q49pF18Tj5OEv9qCqElxztoNck4i6O_azsmsoOQrLIENIWPh3EynBN3ESpYERdCgXO8MlWeuG14_V1HbNjnJPZDuvYg__YfMzoOEtfm1sCqEaJ2Ww-BaX7yGfuCL4XsuZlCQQNHjfscy_WywVfIZPKCiW8QR74i0cSzQ"
LICENSE_KEY = "IMSV-6ECZ-91TE-WZRM-Q7AQ-MBN4-UW48-2CPT-71X9"


@pytest.fixture
def license_setup(runner: CliRunner) -> dict:
    """Fixture to set up license and return cleanup info.

    Sets a license before tests and ensures cleanup after tests complete.
    Note: This requires valid license keys. Tests may skip if license keys are not available.
    """
    # Set up: Create license
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "server",
            "set-server-license",
            "--licenseKey",
            LICENSE_KEY,
            "--activationKey",
            ACTIVATION_KEY,
        ],
    )

    yield result

    # Cleanup: Delete license after test (only if it was successfully set)
    if result.exit_code == 0:
        runner.invoke(
            cli_app,
            ["--format", "json", "server", "delete-server-license"],
        )


@pytest.mark.e2e
def test_set_server_license(license_setup: Result) -> None:
    """Test set-server-license command and validate response structure."""
    result = license_setup
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    LicenseResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_get_server_license_after_set(runner: CliRunner, license_setup: Result) -> None:
    """Test get-server-license command - requires license to be set."""
    if license_setup.exit_code != 0:
        pytest.skip("License setup failed - cannot test get-server-license")
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-server-license"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    p = LicenseResponseDto.model_validate(response_data)
    assert p.license_key == LICENSE_KEY
    assert p.activation_key == ACTIVATION_KEY


@pytest.mark.e2e
def test_get_server_license_before_set(runner: CliRunner) -> None:
    """Test get-server-license command - requires license to be set."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "get-server-license"],
    )
    # 404 error code
    assert result.exit_code == 4, result.stdout + result.stderr


@pytest.mark.e2e
def test_delete_server_license(runner: CliRunner, license_setup: dict) -> None:
    """Test delete-server-license command - requires license to be set first."""
    if license_setup.exit_code != 0:
        pytest.skip("License setup failed - cannot test delete-server-license")

    result = runner.invoke(
        cli_app,
        ["--format", "json", "server", "delete-server-license"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    assert response_data is None
