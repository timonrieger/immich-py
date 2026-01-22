"""Generated CLI commands for Authentication tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Endpoints related to user authentication, including OAuth.\n\n[link=https://api.immich.app/endpoints/authentication]Immich API documentation[/link]"""
)


@app.command("change-password", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/authentication/changePassword]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if invalidate_sessions is not None:
        set_nested(
            json_data, ["invalidate_sessions"], invalidate_sessions.lower() == "true"
        )
    set_nested(json_data, ["new_password"], new_password)
    set_nested(json_data, ["password"], password)
    change_password_dto = ChangePasswordDto.model_validate(json_data)
    kwargs["change_password_dto"] = change_password_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "change_password", ctx, **kwargs)
    print_response(result, ctx)


@app.command("change-pin-code", deprecated=False, rich_help_panel="API commands")
def change_pin_code(
    ctx: typer.Context,
    new_pin_code: str = typer.Option(..., "--new-pin-code", help="""Example: 123456"""),
    password: str | None = typer.Option(None, "--password", help=""""""),
    pin_code: str | None = typer.Option(None, "--pin-code", help="""Example: 123456"""),
) -> None:
    """Change pin code

    [link=https://api.immich.app/endpoints/authentication/changePinCode]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["new_pin_code"], new_pin_code)
    if password is not None:
        set_nested(json_data, ["password"], password)
    if pin_code is not None:
        set_nested(json_data, ["pin_code"], pin_code)
    pin_code_change_dto = PinCodeChangeDto.model_validate(json_data)
    kwargs["pin_code_change_dto"] = pin_code_change_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "change_pin_code", ctx, **kwargs)
    print_response(result, ctx)


@app.command("finish-o-auth", deprecated=False, rich_help_panel="API commands")
def finish_o_auth(
    ctx: typer.Context,
    code_verifier: str | None = typer.Option(None, "--code-verifier", help=""""""),
    state: str | None = typer.Option(None, "--state", help=""""""),
    url: str = typer.Option(..., "--url", help=""""""),
) -> None:
    """Finish OAuth

    [link=https://api.immich.app/endpoints/authentication/finishOAuth]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if code_verifier is not None:
        set_nested(json_data, ["code_verifier"], code_verifier)
    if state is not None:
        set_nested(json_data, ["state"], state)
    set_nested(json_data, ["url"], url)
    o_auth_callback_dto = OAuthCallbackDto.model_validate(json_data)
    kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "finish_o_auth", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-auth-status", deprecated=False, rich_help_panel="API commands")
def get_auth_status(
    ctx: typer.Context,
) -> None:
    """Retrieve auth status

    [link=https://api.immich.app/endpoints/authentication/getAuthStatus]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "get_auth_status", ctx, **kwargs)
    print_response(result, ctx)


@app.command("link-o-auth-account", deprecated=False, rich_help_panel="API commands")
def link_o_auth_account(
    ctx: typer.Context,
    code_verifier: str | None = typer.Option(None, "--code-verifier", help=""""""),
    state: str | None = typer.Option(None, "--state", help=""""""),
    url: str = typer.Option(..., "--url", help=""""""),
) -> None:
    """Link OAuth account

    [link=https://api.immich.app/endpoints/authentication/linkOAuthAccount]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if code_verifier is not None:
        set_nested(json_data, ["code_verifier"], code_verifier)
    if state is not None:
        set_nested(json_data, ["state"], state)
    set_nested(json_data, ["url"], url)
    o_auth_callback_dto = OAuthCallbackDto.model_validate(json_data)
    kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "link_o_auth_account", ctx, **kwargs)
    print_response(result, ctx)


@app.command("lock-auth-session", deprecated=False, rich_help_panel="API commands")
def lock_auth_session(
    ctx: typer.Context,
) -> None:
    """Lock auth session

    [link=https://api.immich.app/endpoints/authentication/lockAuthSession]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "lock_auth_session", ctx, **kwargs)
    print_response(result, ctx)


@app.command("login", deprecated=False, rich_help_panel="API commands")
def login(
    ctx: typer.Context,
    email: str = typer.Option(..., "--email", help="""Example: testuser@email.com"""),
    password: str = typer.Option(..., "--password", help="""Example: password"""),
) -> None:
    """Login

    [link=https://api.immich.app/endpoints/authentication/login]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["email"], email)
    set_nested(json_data, ["password"], password)
    login_credential_dto = LoginCredentialDto.model_validate(json_data)
    kwargs["login_credential_dto"] = login_credential_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "login", ctx, **kwargs)
    print_response(result, ctx)


@app.command("logout", deprecated=False, rich_help_panel="API commands")
def logout(
    ctx: typer.Context,
) -> None:
    """Logout

    [link=https://api.immich.app/endpoints/authentication/logout]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "logout", ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "redirect-o-auth-to-mobile", deprecated=False, rich_help_panel="API commands"
)
def redirect_o_auth_to_mobile(
    ctx: typer.Context,
) -> None:
    """Redirect OAuth to mobile

    [link=https://api.immich.app/endpoints/authentication/redirectOAuthToMobile]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.auth, "redirect_o_auth_to_mobile", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("reset-pin-code", deprecated=False, rich_help_panel="API commands")
def reset_pin_code(
    ctx: typer.Context,
    password: str | None = typer.Option(None, "--password", help=""""""),
    pin_code: str | None = typer.Option(None, "--pin-code", help="""Example: 123456"""),
) -> None:
    """Reset pin code

    [link=https://api.immich.app/endpoints/authentication/resetPinCode]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if password is not None:
        set_nested(json_data, ["password"], password)
    if pin_code is not None:
        set_nested(json_data, ["pin_code"], pin_code)
    pin_code_reset_dto = PinCodeResetDto.model_validate(json_data)
    kwargs["pin_code_reset_dto"] = pin_code_reset_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "reset_pin_code", ctx, **kwargs)
    print_response(result, ctx)


@app.command("setup-pin-code", deprecated=False, rich_help_panel="API commands")
def setup_pin_code(
    ctx: typer.Context,
    pin_code: str = typer.Option(..., "--pin-code", help="""Example: 123456"""),
) -> None:
    """Setup pin code

    [link=https://api.immich.app/endpoints/authentication/setupPinCode]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["pin_code"], pin_code)
    pin_code_setup_dto = PinCodeSetupDto.model_validate(json_data)
    kwargs["pin_code_setup_dto"] = pin_code_setup_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "setup_pin_code", ctx, **kwargs)
    print_response(result, ctx)


@app.command("sign-up-admin", deprecated=False, rich_help_panel="API commands")
def sign_up_admin(
    ctx: typer.Context,
    email: str = typer.Option(..., "--email", help="""Example: testuser@email.com"""),
    name: str = typer.Option(..., "--name", help="""Example: Admin"""),
    password: str = typer.Option(..., "--password", help="""Example: password"""),
) -> None:
    """Register admin

    [link=https://api.immich.app/endpoints/authentication/signUpAdmin]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["email"], email)
    set_nested(json_data, ["name"], name)
    set_nested(json_data, ["password"], password)
    sign_up_dto = SignUpDto.model_validate(json_data)
    kwargs["sign_up_dto"] = sign_up_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "sign_up_admin", ctx, **kwargs)
    print_response(result, ctx)


@app.command("start-o-auth", deprecated=False, rich_help_panel="API commands")
def start_o_auth(
    ctx: typer.Context,
    code_challenge: str | None = typer.Option(None, "--code-challenge", help=""""""),
    redirect_uri: str = typer.Option(..., "--redirect-uri", help=""""""),
    state: str | None = typer.Option(None, "--state", help=""""""),
) -> None:
    """Start OAuth

    [link=https://api.immich.app/endpoints/authentication/startOAuth]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if code_challenge is not None:
        set_nested(json_data, ["code_challenge"], code_challenge)
    set_nested(json_data, ["redirect_uri"], redirect_uri)
    if state is not None:
        set_nested(json_data, ["state"], state)
    o_auth_config_dto = OAuthConfigDto.model_validate(json_data)
    kwargs["o_auth_config_dto"] = o_auth_config_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "start_o_auth", ctx, **kwargs)
    print_response(result, ctx)


@app.command("unlink-o-auth-account", deprecated=False, rich_help_panel="API commands")
def unlink_o_auth_account(
    ctx: typer.Context,
) -> None:
    """Unlink OAuth account

    [link=https://api.immich.app/endpoints/authentication/unlinkOAuthAccount]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "unlink_o_auth_account", ctx, **kwargs)
    print_response(result, ctx)


@app.command("unlock-auth-session", deprecated=False, rich_help_panel="API commands")
def unlock_auth_session(
    ctx: typer.Context,
    password: str | None = typer.Option(None, "--password", help=""""""),
    pin_code: str | None = typer.Option(None, "--pin-code", help="""Example: 123456"""),
) -> None:
    """Unlock auth session

    [link=https://api.immich.app/endpoints/authentication/unlockAuthSession]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if password is not None:
        set_nested(json_data, ["password"], password)
    if pin_code is not None:
        set_nested(json_data, ["pin_code"], pin_code)
    session_unlock_dto = SessionUnlockDto.model_validate(json_data)
    kwargs["session_unlock_dto"] = session_unlock_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "unlock_auth_session", ctx, **kwargs)
    print_response(result, ctx)


@app.command("validate-access-token", deprecated=False, rich_help_panel="API commands")
def validate_access_token(
    ctx: typer.Context,
) -> None:
    """Validate access token

    [link=https://api.immich.app/endpoints/authentication/validateAccessToken]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.auth, "validate_access_token", ctx, **kwargs)
    print_response(result, ctx)
