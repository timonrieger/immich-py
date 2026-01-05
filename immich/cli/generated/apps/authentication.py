"""Generated CLI commands for Authentication tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Authentication operations")

@app.command("change-password")
def change_password(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Change password"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.change_password_dto import ChangePasswordDto
        change_password_dto = deserialize_request_body(json_data, ChangePasswordDto)
        kwargs['change_password_dto'] = change_password_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'change_password', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("change-pin-code")
def change_pin_code(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Change pin code"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.pin_code_change_dto import PinCodeChangeDto
        pin_code_change_dto = deserialize_request_body(json_data, PinCodeChangeDto)
        kwargs['pin_code_change_dto'] = pin_code_change_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'change_pin_code', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("finish-o-auth")
def finish_o_auth(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Finish OAuth"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.o_auth_callback_dto import OAuthCallbackDto
        o_auth_callback_dto = deserialize_request_body(json_data, OAuthCallbackDto)
        kwargs['o_auth_callback_dto'] = o_auth_callback_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'finish_o_auth', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-auth-status")
def get_auth_status(
    ctx: typer.Context,
) -> None:
    """Retrieve auth status"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'get_auth_status', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("link-o-auth-account")
def link_o_auth_account(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Link OAuth account"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.o_auth_callback_dto import OAuthCallbackDto
        o_auth_callback_dto = deserialize_request_body(json_data, OAuthCallbackDto)
        kwargs['o_auth_callback_dto'] = o_auth_callback_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'link_o_auth_account', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("lock-auth-session")
def lock_auth_session(
    ctx: typer.Context,
) -> None:
    """Lock auth session"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'lock_auth_session', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("login")
def login(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Login"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.login_credential_dto import LoginCredentialDto
        login_credential_dto = deserialize_request_body(json_data, LoginCredentialDto)
        kwargs['login_credential_dto'] = login_credential_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'login', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("logout")
def logout(
    ctx: typer.Context,
) -> None:
    """Logout"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'logout', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("redirect-o-auth-to-mobile")
def redirect_o_auth_to_mobile(
    ctx: typer.Context,
) -> None:
    """Redirect OAuth to mobile"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'redirect_o_auth_to_mobile', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("reset-pin-code")
def reset_pin_code(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Reset pin code"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.pin_code_reset_dto import PinCodeResetDto
        pin_code_reset_dto = deserialize_request_body(json_data, PinCodeResetDto)
        kwargs['pin_code_reset_dto'] = pin_code_reset_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'reset_pin_code', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("setup-pin-code")
def setup_pin_code(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Setup pin code"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.pin_code_setup_dto import PinCodeSetupDto
        pin_code_setup_dto = deserialize_request_body(json_data, PinCodeSetupDto)
        kwargs['pin_code_setup_dto'] = pin_code_setup_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'setup_pin_code', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("sign-up-admin")
def sign_up_admin(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Register admin"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.sign_up_dto import SignUpDto
        sign_up_dto = deserialize_request_body(json_data, SignUpDto)
        kwargs['sign_up_dto'] = sign_up_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'sign_up_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("start-o-auth")
def start_o_auth(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Start OAuth"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.o_auth_config_dto import OAuthConfigDto
        o_auth_config_dto = deserialize_request_body(json_data, OAuthConfigDto)
        kwargs['o_auth_config_dto'] = o_auth_config_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'start_o_auth', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("unlink-o-auth-account")
def unlink_o_auth_account(
    ctx: typer.Context,
) -> None:
    """Unlink OAuth account"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'unlink_o_auth_account', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("unlock-auth-session")
def unlock_auth_session(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Unlock auth session"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.session_unlock_dto import SessionUnlockDto
        session_unlock_dto = deserialize_request_body(json_data, SessionUnlockDto)
        kwargs['session_unlock_dto'] = session_unlock_dto
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'unlock_auth_session', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("validate-access-token")
def validate_access_token(
    ctx: typer.Context,
) -> None:
    """Validate access token"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.authentication
    result = run_command(client, api_group, 'validate_access_token', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
