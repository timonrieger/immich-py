"""Generated CLI commands for Authentication tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Endpoints related to user authentication, including OAuth.\n\nDocs: https://api.immich.app/endpoints/authentication"""
)


@app.command("change-password", deprecated=False)
def change_password(
    ctx: typer.Context,
    invalidate_sessions: Literal["true", "false"] | None = typer.Option(
        None, "--invalidate-sessions", help=""""""
    ),
    new_password: str = typer.Option(
        ..., "--new-password", help="""Example: password"""
    ),
    password: str = typer.Option(..., "--password", help="""Example: password"""),
) -> None:
    """Change password

    Docs: https://api.immich.app/endpoints/authentication/changePassword
    """
    kwargs = {}
    json_data = {}
    if invalidate_sessions is not None:
        set_nested(
            json_data, ["invalidate_sessions"], invalidate_sessions.lower() == "true"
        )
    set_nested(json_data, ["new_password"], new_password)
    set_nested(json_data, ["password"], password)
    from immich.client.models.change_password_dto import ChangePasswordDto

    change_password_dto = ChangePasswordDto.model_validate(json_data)
    kwargs["change_password_dto"] = change_password_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "change_password", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("change-pin-code", deprecated=False)
def change_pin_code(
    ctx: typer.Context,
    new_pin_code: str = typer.Option(..., "--new-pin-code", help="""Example: 123456"""),
    password: str | None = typer.Option(None, "--password", help=""""""),
    pin_code: str | None = typer.Option(None, "--pin-code", help="""Example: 123456"""),
) -> None:
    """Change pin code

    Docs: https://api.immich.app/endpoints/authentication/changePinCode
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["new_pin_code"], new_pin_code)
    if password is not None:
        set_nested(json_data, ["password"], password)
    if pin_code is not None:
        set_nested(json_data, ["pin_code"], pin_code)
    from immich.client.models.pin_code_change_dto import PinCodeChangeDto

    pin_code_change_dto = PinCodeChangeDto.model_validate(json_data)
    kwargs["pin_code_change_dto"] = pin_code_change_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "change_pin_code", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("finish-o-auth", deprecated=False)
def finish_o_auth(
    ctx: typer.Context,
    code_verifier: str | None = typer.Option(None, "--code-verifier", help=""""""),
    state: str | None = typer.Option(None, "--state", help=""""""),
    url: str = typer.Option(..., "--url", help=""""""),
) -> None:
    """Finish OAuth

    Docs: https://api.immich.app/endpoints/authentication/finishOAuth
    """
    kwargs = {}
    json_data = {}
    if code_verifier is not None:
        set_nested(json_data, ["code_verifier"], code_verifier)
    if state is not None:
        set_nested(json_data, ["state"], state)
    set_nested(json_data, ["url"], url)
    from immich.client.models.o_auth_callback_dto import OAuthCallbackDto

    o_auth_callback_dto = OAuthCallbackDto.model_validate(json_data)
    kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "finish_o_auth", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-auth-status", deprecated=False)
def get_auth_status(
    ctx: typer.Context,
) -> None:
    """Retrieve auth status

    Docs: https://api.immich.app/endpoints/authentication/getAuthStatus
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "get_auth_status", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("link-o-auth-account", deprecated=False)
def link_o_auth_account(
    ctx: typer.Context,
    code_verifier: str | None = typer.Option(None, "--code-verifier", help=""""""),
    state: str | None = typer.Option(None, "--state", help=""""""),
    url: str = typer.Option(..., "--url", help=""""""),
) -> None:
    """Link OAuth account

    Docs: https://api.immich.app/endpoints/authentication/linkOAuthAccount
    """
    kwargs = {}
    json_data = {}
    if code_verifier is not None:
        set_nested(json_data, ["code_verifier"], code_verifier)
    if state is not None:
        set_nested(json_data, ["state"], state)
    set_nested(json_data, ["url"], url)
    from immich.client.models.o_auth_callback_dto import OAuthCallbackDto

    o_auth_callback_dto = OAuthCallbackDto.model_validate(json_data)
    kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "link_o_auth_account", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("lock-auth-session", deprecated=False)
def lock_auth_session(
    ctx: typer.Context,
) -> None:
    """Lock auth session

    Docs: https://api.immich.app/endpoints/authentication/lockAuthSession
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "lock_auth_session", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("login", deprecated=False)
def login(
    ctx: typer.Context,
    email: str = typer.Option(..., "--email", help="""Example: testuser@email.com"""),
    password: str = typer.Option(..., "--password", help="""Example: password"""),
) -> None:
    """Login

    Docs: https://api.immich.app/endpoints/authentication/login
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["email"], email)
    set_nested(json_data, ["password"], password)
    from immich.client.models.login_credential_dto import LoginCredentialDto

    login_credential_dto = LoginCredentialDto.model_validate(json_data)
    kwargs["login_credential_dto"] = login_credential_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "login", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("logout", deprecated=False)
def logout(
    ctx: typer.Context,
) -> None:
    """Logout

    Docs: https://api.immich.app/endpoints/authentication/logout
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "logout", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("redirect-o-auth-to-mobile", deprecated=False)
def redirect_o_auth_to_mobile(
    ctx: typer.Context,
) -> None:
    """Redirect OAuth to mobile

    Docs: https://api.immich.app/endpoints/authentication/redirectOAuthToMobile
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(
        client, client.authentication, "redirect_o_auth_to_mobile", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("reset-pin-code", deprecated=False)
def reset_pin_code(
    ctx: typer.Context,
    password: str | None = typer.Option(None, "--password", help=""""""),
    pin_code: str | None = typer.Option(None, "--pin-code", help="""Example: 123456"""),
) -> None:
    """Reset pin code

    Docs: https://api.immich.app/endpoints/authentication/resetPinCode
    """
    kwargs = {}
    json_data = {}
    if password is not None:
        set_nested(json_data, ["password"], password)
    if pin_code is not None:
        set_nested(json_data, ["pin_code"], pin_code)
    from immich.client.models.pin_code_reset_dto import PinCodeResetDto

    pin_code_reset_dto = PinCodeResetDto.model_validate(json_data)
    kwargs["pin_code_reset_dto"] = pin_code_reset_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "reset_pin_code", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("setup-pin-code", deprecated=False)
def setup_pin_code(
    ctx: typer.Context,
    pin_code: str = typer.Option(..., "--pin-code", help="""Example: 123456"""),
) -> None:
    """Setup pin code

    Docs: https://api.immich.app/endpoints/authentication/setupPinCode
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["pin_code"], pin_code)
    from immich.client.models.pin_code_setup_dto import PinCodeSetupDto

    pin_code_setup_dto = PinCodeSetupDto.model_validate(json_data)
    kwargs["pin_code_setup_dto"] = pin_code_setup_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "setup_pin_code", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("sign-up-admin", deprecated=False)
def sign_up_admin(
    ctx: typer.Context,
    email: str = typer.Option(..., "--email", help="""Example: testuser@email.com"""),
    name: str = typer.Option(..., "--name", help="""Example: Admin"""),
    password: str = typer.Option(..., "--password", help="""Example: password"""),
) -> None:
    """Register admin

    Docs: https://api.immich.app/endpoints/authentication/signUpAdmin
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["email"], email)
    set_nested(json_data, ["name"], name)
    set_nested(json_data, ["password"], password)
    from immich.client.models.sign_up_dto import SignUpDto

    sign_up_dto = SignUpDto.model_validate(json_data)
    kwargs["sign_up_dto"] = sign_up_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "sign_up_admin", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("start-o-auth", deprecated=False)
def start_o_auth(
    ctx: typer.Context,
    code_challenge: str | None = typer.Option(None, "--code-challenge", help=""""""),
    redirect_uri: str = typer.Option(..., "--redirect-uri", help=""""""),
    state: str | None = typer.Option(None, "--state", help=""""""),
) -> None:
    """Start OAuth

    Docs: https://api.immich.app/endpoints/authentication/startOAuth
    """
    kwargs = {}
    json_data = {}
    if code_challenge is not None:
        set_nested(json_data, ["code_challenge"], code_challenge)
    set_nested(json_data, ["redirect_uri"], redirect_uri)
    if state is not None:
        set_nested(json_data, ["state"], state)
    from immich.client.models.o_auth_config_dto import OAuthConfigDto

    o_auth_config_dto = OAuthConfigDto.model_validate(json_data)
    kwargs["o_auth_config_dto"] = o_auth_config_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "start_o_auth", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("unlink-o-auth-account", deprecated=False)
def unlink_o_auth_account(
    ctx: typer.Context,
) -> None:
    """Unlink OAuth account

    Docs: https://api.immich.app/endpoints/authentication/unlinkOAuthAccount
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(
        client, client.authentication, "unlink_o_auth_account", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("unlock-auth-session", deprecated=False)
def unlock_auth_session(
    ctx: typer.Context,
    password: str | None = typer.Option(None, "--password", help=""""""),
    pin_code: str | None = typer.Option(None, "--pin-code", help="""Example: 123456"""),
) -> None:
    """Unlock auth session

    Docs: https://api.immich.app/endpoints/authentication/unlockAuthSession
    """
    kwargs = {}
    json_data = {}
    if password is not None:
        set_nested(json_data, ["password"], password)
    if pin_code is not None:
        set_nested(json_data, ["pin_code"], pin_code)
    from immich.client.models.session_unlock_dto import SessionUnlockDto

    session_unlock_dto = SessionUnlockDto.model_validate(json_data)
    kwargs["session_unlock_dto"] = session_unlock_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "unlock_auth_session", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("validate-access-token", deprecated=False)
def validate_access_token(
    ctx: typer.Context,
) -> None:
    """Validate access token

    Docs: https://api.immich.app/endpoints/authentication/validateAccessToken
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(
        client, client.authentication, "validate_access_token", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
