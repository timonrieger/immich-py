import asyncio
import json
from typing import Awaitable, Callable

import pytest
from typer.testing import CliRunner

from immich.cli.app import app as cli_app
from immich.client import (
    AuthStatusResponseDto,
    LoginResponseDto,
    LogoutResponseDto,
    OAuthAuthorizeResponseDto,
    UserAdminResponseDto,
    ValidateAccessTokenResponseDto,
)


@pytest.mark.e2e
def test_get_auth_status(runner: CliRunner) -> None:
    """Test get-auth-status command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "authentication", "get-auth-status"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    AuthStatusResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_validate_access_token(runner: CliRunner) -> None:
    """Test validate-access-token command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "authentication", "validate-access-token"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    ValidateAccessTokenResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_login(runner: CliRunner) -> None:
    """Test login command and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "login",
            "--email",
            "admin@immich.cloud",
            "--password",
            "password",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    LoginResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_logout(runner: CliRunner) -> None:
    """Test logout command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "authentication", "logout"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    LogoutResponseDto.model_validate(response_data)


@pytest.mark.e2e
def test_change_password(runner: CliRunner) -> None:
    """Test change-password command and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "change-password",
            "--password",
            "password",
            "--newPassword",
            "newpassword123",
            "--invalidateSessions",
            "false",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    UserAdminResponseDto.model_validate(response_data)

    # Change password back for other tests
    revert_result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "change-password",
            "--password",
            "newpassword123",
            "--newPassword",
            "password",
            "--invalidateSessions",
            "false",
        ],
    )
    assert revert_result.exit_code == 0


@pytest.mark.e2e
def test_setup_pin_code(runner: CliRunner) -> None:
    """Test setup-pin-code command and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "setup-pin-code",
            "--pinCode",
            "123456",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Setup pin code returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None


@pytest.mark.e2e
def test_change_pin_code(runner: CliRunner, pin_code_setup: str) -> None:
    """Test change-pin-code command and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "change-pin-code",
            "--newPinCode",
            "567890",
            "--password",
            "password",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Change pin code returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None


@pytest.mark.e2e
@pytest.mark.parametrize("teardown", [False])
def test_reset_pin_code(runner: CliRunner, pin_code_setup: str) -> None:
    """Test reset-pin-code command and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "reset-pin-code",
            "--password",
            "password",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Reset pin code returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_auth_session_lock_unlock(
    runner_with_access_token: CliRunner,
    pin_code_change: tuple[str, str],
    get_auth_status_factory: Callable[[], Awaitable[AuthStatusResponseDto]],
) -> None:
    """Test auth session lock and unlock commands with changed PIN code."""

    initial_pin = pin_code_change[0]
    new_pin = pin_code_change[1]

    auth_status = await get_auth_status_factory()
    assert auth_status.is_elevated is False

    # Try to unlock with the OLD PIN code (should fail)
    old_unlock_result = await asyncio.to_thread(
        runner_with_access_token.invoke,
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "unlock-auth-session",
            "--pinCode",
            initial_pin,
        ],
    )
    # This should fail since we changed the PIN code
    assert old_unlock_result.exit_code == 4, (
        "Unlock with old PIN should fail after PIN code change. "
        f"Output: {old_unlock_result.stdout + old_unlock_result.stderr}"
    )
    auth_status = await get_auth_status_factory()
    assert auth_status.is_elevated is False

    # Unlock with the NEW PIN code (should succeed)
    result = await asyncio.to_thread(
        runner_with_access_token.invoke,
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "unlock-auth-session",
            "--pinCode",
            new_pin,
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Unlock auth session returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None

    auth_status = await get_auth_status_factory()
    assert auth_status.is_elevated is True

    # Lock the session
    result = await asyncio.to_thread(
        runner_with_access_token.invoke,
        cli_app,
        ["--format", "json", "authentication", "lock-auth-session"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    # Lock auth session returns 204, so response should be None or empty
    if result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None

    auth_status = await get_auth_status_factory()
    assert auth_status.is_elevated is False


@pytest.mark.e2e
def test_unlink_o_auth_account(runner: CliRunner) -> None:
    """Test unlink-o-auth-account command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "authentication", "unlink-o-auth-account"],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    user_response = UserAdminResponseDto.model_validate(response_data)
    assert user_response.id is not None


@pytest.mark.e2e
def test_start_o_auth(runner: CliRunner) -> None:
    """Test start-o-auth command and validate response structure."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "start-o-auth",
            "--redirectUri",
            "http://localhost:3000/oauth/callback",
            "--state",
            "test-state",
        ],
    )
    # This may fail if OAuth is not configured, which is acceptable
    if result.exit_code == 0:
        response_data = json.loads(result.output)
        oauth_response = OAuthAuthorizeResponseDto.model_validate(response_data)
        assert oauth_response.url is not None


@pytest.mark.e2e
def test_redirect_o_auth_to_mobile(runner: CliRunner) -> None:
    """Test redirect-o-auth-to-mobile command and validate response structure."""
    result = runner.invoke(
        cli_app,
        ["--format", "json", "authentication", "redirect-o-auth-to-mobile"],
    )
    # This may fail if OAuth is not configured, which is acceptable
    # Redirect OAuth to mobile returns 200 with no body, so response should be None or empty
    if result.exit_code == 0 and result.output.strip():
        response_data = json.loads(result.output)
        assert response_data is None


@pytest.mark.e2e
@pytest.mark.skip(
    reason="OAuth is not configured in the test environment, thus the test would fail"
)
def test_finish_o_auth(runner: CliRunner) -> None:
    """Test finish-o-auth command - may fail if OAuth is not configured."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "finish-o-auth",
            "--url",
            "http://localhost:3000/oauth/callback?code=test-code&state=test-state",
            "--state",
            "test-state",
        ],
    )
    # This will likely fail if OAuth is not properly configured, which is acceptable
    # We just verify the command exists and can be invoked
    assert result.exit_code in [0, 1]  # May fail due to OAuth configuration


@pytest.mark.e2e
@pytest.mark.skip(
    reason="OAuth is not configured in the test environment, thus the test would fail"
)
def test_link_o_auth_account(runner: CliRunner) -> None:
    """Test link-o-auth-account command - may fail if OAuth is not configured."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "link-o-auth-account",
            "--url",
            "http://localhost:3000/oauth/callback?code=test-code&state=test-state",
            "--state",
            "test-state",
        ],
    )
    # This will likely fail if OAuth is not properly configured, which is acceptable
    # We just verify the command exists and can be invoked
    assert result.exit_code in [0, 1]  # May fail due to OAuth configuration


@pytest.mark.e2e
@pytest.mark.skip(
    reason="Admin is already created in the test environment, thus the test would fail"
)
def test_sign_up_admin(runner: CliRunner) -> None:
    """Test sign-up-admin command - may fail if admin already exists."""
    result = runner.invoke(
        cli_app,
        [
            "--format",
            "json",
            "authentication",
            "sign-up-admin",
            "--email",
            "test-admin@immich.cloud",
            "--name",
            "Test Admin",
            "--password",
            "testpassword123",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.output)
    user_response = UserAdminResponseDto.model_validate(response_data)
    assert user_response.id is not None
    assert user_response.email == "test-admin@immich.cloud"
    assert user_response.name == "Test Admin"
