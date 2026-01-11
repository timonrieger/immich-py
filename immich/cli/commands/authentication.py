"""Generated CLI commands for Authentication tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
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
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    invalidate_sessions: bool | None = typer.Option(
        None, "--invalidateSessions", help="""Invalidate all other sessions"""
    ),
    new_password: str = typer.Option(
        ..., "--newPassword", help="""New password (min 8 characters)"""
    ),
    password: str = typer.Option(..., "--password", help="""Current password"""),
) -> None:
    """Change password

    Docs: https://api.immich.app/endpoints/authentication/changePassword
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([invalidate_sessions, new_password, password])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.change_password_dto import ChangePasswordDto

        change_password_dto = deserialize_request_body(json_data, ChangePasswordDto)
        kwargs["change_password_dto"] = change_password_dto
    elif any(
        [
            invalidate_sessions,
            new_password,
            password,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if invalidate_sessions is not None:
            set_nested(json_data, ["invalidateSessions"], invalidate_sessions)
        if new_password is None:
            raise SystemExit("Error: --newPassword is required")
        set_nested(json_data, ["newPassword"], new_password)
        if password is None:
            raise SystemExit("Error: --password is required")
        set_nested(json_data, ["password"], password)
        if json_data:
            from immich.client.models.change_password_dto import ChangePasswordDto

            change_password_dto = deserialize_request_body(json_data, ChangePasswordDto)
            kwargs["change_password_dto"] = change_password_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "change_password", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("change-pin-code")
def change_pin_code(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    new_pin_code: str = typer.Option(
        ..., "--newPinCode", help="""New PIN code (4-6 digits)"""
    ),
    password: str | None = typer.Option(
        None,
        "--password",
        help="""User password (required if PIN code is not provided)""",
    ),
    pin_code: str | None = typer.Option(
        None, "--pinCode", help="""New PIN code (4-6 digits)"""
    ),
) -> None:
    """Change pin code

    Docs: https://api.immich.app/endpoints/authentication/changePinCode
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([new_pin_code, password, pin_code])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.pin_code_change_dto import PinCodeChangeDto

        pin_code_change_dto = deserialize_request_body(json_data, PinCodeChangeDto)
        kwargs["pin_code_change_dto"] = pin_code_change_dto
    elif any(
        [
            new_pin_code,
            password,
            pin_code,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if new_pin_code is None:
            raise SystemExit("Error: --newPinCode is required")
        set_nested(json_data, ["newPinCode"], new_pin_code)
        if password is not None:
            set_nested(json_data, ["password"], password)
        if pin_code is not None:
            set_nested(json_data, ["pinCode"], pin_code)
        if json_data:
            from immich.client.models.pin_code_change_dto import PinCodeChangeDto

            pin_code_change_dto = deserialize_request_body(json_data, PinCodeChangeDto)
            kwargs["pin_code_change_dto"] = pin_code_change_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "change_pin_code", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("finish-o-auth")
def finish_o_auth(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    code_verifier: str | None = typer.Option(
        None, "--codeVerifier", help="""OAuth code verifier (PKCE)"""
    ),
    state: str | None = typer.Option(None, "--state", help="""OAuth state parameter"""),
    url: str = typer.Option(..., "--url", help="""OAuth callback URL"""),
) -> None:
    """Finish OAuth

    Docs: https://api.immich.app/endpoints/authentication/finishOAuth
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([code_verifier, state, url])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.o_auth_callback_dto import OAuthCallbackDto

        o_auth_callback_dto = deserialize_request_body(json_data, OAuthCallbackDto)
        kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    elif any(
        [
            code_verifier,
            state,
            url,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if code_verifier is not None:
            set_nested(json_data, ["codeVerifier"], code_verifier)
        if state is not None:
            set_nested(json_data, ["state"], state)
        if url is None:
            raise SystemExit("Error: --url is required")
        set_nested(json_data, ["url"], url)
        if json_data:
            from immich.client.models.o_auth_callback_dto import OAuthCallbackDto

            o_auth_callback_dto = deserialize_request_body(json_data, OAuthCallbackDto)
            kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "finish_o_auth", **kwargs)
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
    api_group = client.authentication
    result = run_command(client, api_group, "get_auth_status", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("link-o-auth-account")
def link_o_auth_account(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    code_verifier: str | None = typer.Option(
        None, "--codeVerifier", help="""OAuth code verifier (PKCE)"""
    ),
    state: str | None = typer.Option(None, "--state", help="""OAuth state parameter"""),
    url: str = typer.Option(..., "--url", help="""OAuth callback URL"""),
) -> None:
    """Link OAuth account

    Docs: https://api.immich.app/endpoints/authentication/linkOAuthAccount
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([code_verifier, state, url])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.o_auth_callback_dto import OAuthCallbackDto

        o_auth_callback_dto = deserialize_request_body(json_data, OAuthCallbackDto)
        kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    elif any(
        [
            code_verifier,
            state,
            url,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if code_verifier is not None:
            set_nested(json_data, ["codeVerifier"], code_verifier)
        if state is not None:
            set_nested(json_data, ["state"], state)
        if url is None:
            raise SystemExit("Error: --url is required")
        set_nested(json_data, ["url"], url)
        if json_data:
            from immich.client.models.o_auth_callback_dto import OAuthCallbackDto

            o_auth_callback_dto = deserialize_request_body(json_data, OAuthCallbackDto)
            kwargs["o_auth_callback_dto"] = o_auth_callback_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "link_o_auth_account", **kwargs)
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
    api_group = client.authentication
    result = run_command(client, api_group, "lock_auth_session", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("login")
def login(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    email: str = typer.Option(..., "--email", help="""User email"""),
    password: str = typer.Option(..., "--password", help="""User password"""),
) -> None:
    """Login

    Docs: https://api.immich.app/endpoints/authentication/login
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([email, password])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.login_credential_dto import LoginCredentialDto

        login_credential_dto = deserialize_request_body(json_data, LoginCredentialDto)
        kwargs["login_credential_dto"] = login_credential_dto
    elif any(
        [
            email,
            password,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if email is None:
            raise SystemExit("Error: --email is required")
        set_nested(json_data, ["email"], email)
        if password is None:
            raise SystemExit("Error: --password is required")
        set_nested(json_data, ["password"], password)
        if json_data:
            from immich.client.models.login_credential_dto import LoginCredentialDto

            login_credential_dto = deserialize_request_body(
                json_data, LoginCredentialDto
            )
            kwargs["login_credential_dto"] = login_credential_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "login", **kwargs)
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
    api_group = client.authentication
    result = run_command(client, api_group, "logout", **kwargs)
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
    api_group = client.authentication
    result = run_command(client, api_group, "redirect_o_auth_to_mobile", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("reset-pin-code")
def reset_pin_code(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    password: str | None = typer.Option(
        None,
        "--password",
        help="""User password (required if PIN code is not provided)""",
    ),
    pin_code: str | None = typer.Option(
        None, "--pinCode", help="""New PIN code (4-6 digits)"""
    ),
) -> None:
    """Reset pin code

    Docs: https://api.immich.app/endpoints/authentication/resetPinCode
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([password, pin_code])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.pin_code_reset_dto import PinCodeResetDto

        pin_code_reset_dto = deserialize_request_body(json_data, PinCodeResetDto)
        kwargs["pin_code_reset_dto"] = pin_code_reset_dto
    elif any(
        [
            password,
            pin_code,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if password is not None:
            set_nested(json_data, ["password"], password)
        if pin_code is not None:
            set_nested(json_data, ["pinCode"], pin_code)
        if json_data:
            from immich.client.models.pin_code_reset_dto import PinCodeResetDto

            pin_code_reset_dto = deserialize_request_body(json_data, PinCodeResetDto)
            kwargs["pin_code_reset_dto"] = pin_code_reset_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "reset_pin_code", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("setup-pin-code")
def setup_pin_code(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    pin_code: str = typer.Option(..., "--pinCode", help="""PIN code (4-6 digits)"""),
) -> None:
    """Setup pin code

    Docs: https://api.immich.app/endpoints/authentication/setupPinCode
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([pin_code])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.pin_code_setup_dto import PinCodeSetupDto

        pin_code_setup_dto = deserialize_request_body(json_data, PinCodeSetupDto)
        kwargs["pin_code_setup_dto"] = pin_code_setup_dto
    elif any(
        [
            pin_code,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if pin_code is None:
            raise SystemExit("Error: --pinCode is required")
        set_nested(json_data, ["pinCode"], pin_code)
        if json_data:
            from immich.client.models.pin_code_setup_dto import PinCodeSetupDto

            pin_code_setup_dto = deserialize_request_body(json_data, PinCodeSetupDto)
            kwargs["pin_code_setup_dto"] = pin_code_setup_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "setup_pin_code", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("sign-up-admin")
def sign_up_admin(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    email: str = typer.Option(..., "--email", help="""User email"""),
    name: str = typer.Option(..., "--name", help="""User name"""),
    password: str = typer.Option(..., "--password", help="""User password"""),
) -> None:
    """Register admin

    Docs: https://api.immich.app/endpoints/authentication/signUpAdmin
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([email, name, password])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.sign_up_dto import SignUpDto

        sign_up_dto = deserialize_request_body(json_data, SignUpDto)
        kwargs["sign_up_dto"] = sign_up_dto
    elif any(
        [
            email,
            name,
            password,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if email is None:
            raise SystemExit("Error: --email is required")
        set_nested(json_data, ["email"], email)
        if name is None:
            raise SystemExit("Error: --name is required")
        set_nested(json_data, ["name"], name)
        if password is None:
            raise SystemExit("Error: --password is required")
        set_nested(json_data, ["password"], password)
        if json_data:
            from immich.client.models.sign_up_dto import SignUpDto

            sign_up_dto = deserialize_request_body(json_data, SignUpDto)
            kwargs["sign_up_dto"] = sign_up_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "sign_up_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("start-o-auth")
def start_o_auth(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    code_challenge: str | None = typer.Option(
        None, "--codeChallenge", help="""OAuth code challenge (PKCE)"""
    ),
    redirect_uri: str = typer.Option(
        ..., "--redirectUri", help="""OAuth redirect URI"""
    ),
    state: str | None = typer.Option(None, "--state", help="""OAuth state parameter"""),
) -> None:
    """Start OAuth

    Docs: https://api.immich.app/endpoints/authentication/startOAuth
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([code_challenge, redirect_uri, state])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.o_auth_config_dto import OAuthConfigDto

        o_auth_config_dto = deserialize_request_body(json_data, OAuthConfigDto)
        kwargs["o_auth_config_dto"] = o_auth_config_dto
    elif any(
        [
            code_challenge,
            redirect_uri,
            state,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if code_challenge is not None:
            set_nested(json_data, ["codeChallenge"], code_challenge)
        if redirect_uri is None:
            raise SystemExit("Error: --redirectUri is required")
        set_nested(json_data, ["redirectUri"], redirect_uri)
        if state is not None:
            set_nested(json_data, ["state"], state)
        if json_data:
            from immich.client.models.o_auth_config_dto import OAuthConfigDto

            o_auth_config_dto = deserialize_request_body(json_data, OAuthConfigDto)
            kwargs["o_auth_config_dto"] = o_auth_config_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "start_o_auth", **kwargs)
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
    api_group = client.authentication
    result = run_command(client, api_group, "unlink_o_auth_account", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("unlock-auth-session")
def unlock_auth_session(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    password: str | None = typer.Option(
        None,
        "--password",
        help="""User password (required if PIN code is not provided)""",
    ),
    pin_code: str | None = typer.Option(
        None, "--pinCode", help="""New PIN code (4-6 digits)"""
    ),
) -> None:
    """Unlock auth session

    Docs: https://api.immich.app/endpoints/authentication/unlockAuthSession
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([password, pin_code])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.session_unlock_dto import SessionUnlockDto

        session_unlock_dto = deserialize_request_body(json_data, SessionUnlockDto)
        kwargs["session_unlock_dto"] = session_unlock_dto
    elif any(
        [
            password,
            pin_code,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if password is not None:
            set_nested(json_data, ["password"], password)
        if pin_code is not None:
            set_nested(json_data, ["pinCode"], pin_code)
        if json_data:
            from immich.client.models.session_unlock_dto import SessionUnlockDto

            session_unlock_dto = deserialize_request_body(json_data, SessionUnlockDto)
            kwargs["session_unlock_dto"] = session_unlock_dto
    client = ctx.obj["client"]
    api_group = client.authentication
    result = run_command(client, api_group, "unlock_auth_session", **kwargs)
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
    api_group = client.authentication
    result = run_command(client, api_group, "validate_access_token", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
