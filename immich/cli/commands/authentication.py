"""Generated CLI commands for Authentication tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Endpoints related to user authentication, including OAuth.

Docs: https://api.immich.app/endpoints/authentication""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("change-password")
def change_password(
    ctx: typer.Context,
    invalidate_sessions: bool | None = typer.Option(None, "--invalidateSessions"),
    new_password: str = typer.Option(..., "--newPassword"),
    password: str = typer.Option(..., "--password"),
) -> None:
    """Change password

    Docs: https://api.immich.app/endpoints/authentication/changePassword
    """
    kwargs = {}
    has_flags = any([invalidate_sessions, new_password, password])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            invalidate_sessions,
            new_password,
            password,
        ]
    ):
        json_data = {}
        if invalidate_sessions is not None:
            set_nested(json_data, ["invalidateSessions"], invalidate_sessions)
        set_nested(json_data, ["newPassword"], new_password)
        set_nested(json_data, ["password"], password)
        from immich.client.models.change_password_dto import ChangePasswordDto

        change_password_dto = deserialize_request_body(json_data, ChangePasswordDto)
        kwargs["change_password_dto"] = change_password_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "change_password", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("change-pin-code")
def change_pin_code(
    ctx: typer.Context,
    new_pin_code: str = typer.Option(..., "--newPinCode"),
    password: str | None = typer.Option(None, "--password"),
    pin_code: str | None = typer.Option(None, "--pinCode"),
) -> None:
    """Change pin code

    Docs: https://api.immich.app/endpoints/authentication/changePinCode
    """
    kwargs = {}
    has_flags = any([new_pin_code, password, pin_code])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            new_pin_code,
            password,
            pin_code,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["newPinCode"], new_pin_code)
        if password is not None:
            set_nested(json_data, ["password"], password)
        if pin_code is not None:
            set_nested(json_data, ["pinCode"], pin_code)
        from immich.client.models.pin_code_change_dto import PinCodeChangeDto

        pin_code_change_dto = deserialize_request_body(json_data, PinCodeChangeDto)
        kwargs["pin_code_change_dto"] = pin_code_change_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "change_pin_code", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("finish-o-auth")
def finish_o_auth(
    ctx: typer.Context,
    code_verifier: str | None = typer.Option(None, "--codeVerifier"),
    state: str | None = typer.Option(None, "--state"),
    url: str = typer.Option(..., "--url"),
) -> None:
    """Finish OAuth

    Docs: https://api.immich.app/endpoints/authentication/finishOAuth
    """
    kwargs = {}
    has_flags = any([code_verifier, state, url])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            code_verifier,
            state,
            url,
        ]
    ):
        json_data = {}
        if code_verifier is not None:
            set_nested(json_data, ["codeVerifier"], code_verifier)
        if state is not None:
            set_nested(json_data, ["state"], state)
        set_nested(json_data, ["url"], url)
        from immich.client.models.o_auth_callback_dto import OAuthCallbackDto

        o_auth_callback_dto = deserialize_request_body(json_data, OAuthCallbackDto)
        kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "finish_o_auth", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-auth-status")
def get_auth_status(
    ctx: typer.Context,
) -> None:
    """Retrieve auth status

    Docs: https://api.immich.app/endpoints/authentication/getAuthStatus
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "get_auth_status", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("link-o-auth-account")
def link_o_auth_account(
    ctx: typer.Context,
    code_verifier: str | None = typer.Option(None, "--codeVerifier"),
    state: str | None = typer.Option(None, "--state"),
    url: str = typer.Option(..., "--url"),
) -> None:
    """Link OAuth account

    Docs: https://api.immich.app/endpoints/authentication/linkOAuthAccount
    """
    kwargs = {}
    has_flags = any([code_verifier, state, url])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            code_verifier,
            state,
            url,
        ]
    ):
        json_data = {}
        if code_verifier is not None:
            set_nested(json_data, ["codeVerifier"], code_verifier)
        if state is not None:
            set_nested(json_data, ["state"], state)
        set_nested(json_data, ["url"], url)
        from immich.client.models.o_auth_callback_dto import OAuthCallbackDto

        o_auth_callback_dto = deserialize_request_body(json_data, OAuthCallbackDto)
        kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "link_o_auth_account", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("lock-auth-session")
def lock_auth_session(
    ctx: typer.Context,
) -> None:
    """Lock auth session

    Docs: https://api.immich.app/endpoints/authentication/lockAuthSession
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "lock_auth_session", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("login")
def login(
    ctx: typer.Context,
    email: str = typer.Option(..., "--email"),
    password: str = typer.Option(..., "--password"),
) -> None:
    """Login

    Docs: https://api.immich.app/endpoints/authentication/login
    """
    kwargs = {}
    has_flags = any([email, password])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            email,
            password,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["email"], email)
        set_nested(json_data, ["password"], password)
        from immich.client.models.login_credential_dto import LoginCredentialDto

        login_credential_dto = deserialize_request_body(json_data, LoginCredentialDto)
        kwargs["login_credential_dto"] = login_credential_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "login", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("logout")
def logout(
    ctx: typer.Context,
) -> None:
    """Logout

    Docs: https://api.immich.app/endpoints/authentication/logout
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "logout", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("redirect-o-auth-to-mobile")
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("reset-pin-code")
def reset_pin_code(
    ctx: typer.Context,
    password: str | None = typer.Option(None, "--password"),
    pin_code: str | None = typer.Option(None, "--pinCode"),
) -> None:
    """Reset pin code

    Docs: https://api.immich.app/endpoints/authentication/resetPinCode
    """
    kwargs = {}
    has_flags = any([password, pin_code])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            password,
            pin_code,
        ]
    ):
        json_data = {}
        if password is not None:
            set_nested(json_data, ["password"], password)
        if pin_code is not None:
            set_nested(json_data, ["pinCode"], pin_code)
        from immich.client.models.pin_code_reset_dto import PinCodeResetDto

        pin_code_reset_dto = deserialize_request_body(json_data, PinCodeResetDto)
        kwargs["pin_code_reset_dto"] = pin_code_reset_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "reset_pin_code", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("setup-pin-code")
def setup_pin_code(
    ctx: typer.Context,
    pin_code: str = typer.Option(..., "--pinCode"),
) -> None:
    """Setup pin code

    Docs: https://api.immich.app/endpoints/authentication/setupPinCode
    """
    kwargs = {}
    has_flags = any([pin_code])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            pin_code,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["pinCode"], pin_code)
        from immich.client.models.pin_code_setup_dto import PinCodeSetupDto

        pin_code_setup_dto = deserialize_request_body(json_data, PinCodeSetupDto)
        kwargs["pin_code_setup_dto"] = pin_code_setup_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "setup_pin_code", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("sign-up-admin")
def sign_up_admin(
    ctx: typer.Context,
    email: str = typer.Option(..., "--email"),
    name: str = typer.Option(..., "--name"),
    password: str = typer.Option(..., "--password"),
) -> None:
    """Register admin

    Docs: https://api.immich.app/endpoints/authentication/signUpAdmin
    """
    kwargs = {}
    has_flags = any([email, name, password])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            email,
            name,
            password,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["email"], email)
        set_nested(json_data, ["name"], name)
        set_nested(json_data, ["password"], password)
        from immich.client.models.sign_up_dto import SignUpDto

        sign_up_dto = deserialize_request_body(json_data, SignUpDto)
        kwargs["sign_up_dto"] = sign_up_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "sign_up_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("start-o-auth")
def start_o_auth(
    ctx: typer.Context,
    code_challenge: str | None = typer.Option(None, "--codeChallenge"),
    redirect_uri: str = typer.Option(..., "--redirectUri"),
    state: str | None = typer.Option(None, "--state"),
) -> None:
    """Start OAuth

    Docs: https://api.immich.app/endpoints/authentication/startOAuth
    """
    kwargs = {}
    has_flags = any([code_challenge, redirect_uri, state])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            code_challenge,
            redirect_uri,
            state,
        ]
    ):
        json_data = {}
        if code_challenge is not None:
            set_nested(json_data, ["codeChallenge"], code_challenge)
        set_nested(json_data, ["redirectUri"], redirect_uri)
        if state is not None:
            set_nested(json_data, ["state"], state)
        from immich.client.models.o_auth_config_dto import OAuthConfigDto

        o_auth_config_dto = deserialize_request_body(json_data, OAuthConfigDto)
        kwargs["o_auth_config_dto"] = o_auth_config_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "start_o_auth", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("unlink-o-auth-account")
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("unlock-auth-session")
def unlock_auth_session(
    ctx: typer.Context,
    password: str | None = typer.Option(None, "--password"),
    pin_code: str | None = typer.Option(None, "--pinCode"),
) -> None:
    """Unlock auth session

    Docs: https://api.immich.app/endpoints/authentication/unlockAuthSession
    """
    kwargs = {}
    has_flags = any([password, pin_code])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            password,
            pin_code,
        ]
    ):
        json_data = {}
        if password is not None:
            set_nested(json_data, ["password"], password)
        if pin_code is not None:
            set_nested(json_data, ["pinCode"], pin_code)
        from immich.client.models.session_unlock_dto import SessionUnlockDto

        session_unlock_dto = deserialize_request_body(json_data, SessionUnlockDto)
        kwargs["session_unlock_dto"] = session_unlock_dto
    client = ctx.obj["client"]
    result = run_command(client, client.authentication, "unlock_auth_session", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("validate-access-token")
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
