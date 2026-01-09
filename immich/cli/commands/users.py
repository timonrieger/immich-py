"""Generated CLI commands for Users tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Endpoints for viewing and updating the current users, including product key information, profile picture data, onboarding progress, and more.. https://api.immich.app/endpoints/users', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-profile-image")
def create_profile_image(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON with multipart fields (non-file)"),
    file: Path = typer.Option(..., "--file", help="File to upload for file"),
) -> None:
    """Create user profile image"""
    kwargs = {}
    json_data = json.loads(json_str) if json_str is not None else {}
    missing: list[str] = []
    kwargs['file'] = load_file_bytes(file)
    if missing:
        raise SystemExit("Error: missing required multipart fields: " + ', '.join(missing) + ". Provide them via --json and/or file options.")
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'create_profile_image', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-profile-image")
def delete_profile_image(
    ctx: typer.Context,
) -> None:
    """Delete user profile image"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'delete_profile_image', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-user-license")
def delete_user_license(
    ctx: typer.Context,
) -> None:
    """Delete user product key"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'delete_user_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-user-onboarding")
def delete_user_onboarding(
    ctx: typer.Context,
) -> None:
    """Delete user onboarding"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'delete_user_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-my-preferences")
def get_my_preferences(
    ctx: typer.Context,
) -> None:
    """Get my preferences"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_my_preferences', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-my-user")
def get_my_user(
    ctx: typer.Context,
) -> None:
    """Get current user"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_my_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-profile-image")
def get_profile_image(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve user profile image"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_profile_image', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user")
def get_user(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a user"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user-license")
def get_user_license(
    ctx: typer.Context,
) -> None:
    """Retrieve user product key"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_user_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user-onboarding")
def get_user_onboarding(
    ctx: typer.Context,
) -> None:
    """Retrieve user onboarding"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_user_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-users")
def search_users(
    ctx: typer.Context,
) -> None:
    """Get all users"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'search_users', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("set-user-license")
def set_user_license(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Set user product key"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.license_key_dto import LicenseKeyDto
        license_key_dto = deserialize_request_body(json_data, LicenseKeyDto)
        kwargs['license_key_dto'] = license_key_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'set_user_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("set-user-onboarding")
def set_user_onboarding(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update user onboarding"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.onboarding_dto import OnboardingDto
        onboarding_dto = deserialize_request_body(json_data, OnboardingDto)
        kwargs['onboarding_dto'] = onboarding_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'set_user_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-my-preferences")
def update_my_preferences(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update my preferences"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.user_preferences_update_dto import UserPreferencesUpdateDto
        user_preferences_update_dto = deserialize_request_body(json_data, UserPreferencesUpdateDto)
        kwargs['user_preferences_update_dto'] = user_preferences_update_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'update_my_preferences', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-my-user")
def update_my_user(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update current user"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.user_update_me_dto import UserUpdateMeDto
        user_update_me_dto = deserialize_request_body(json_data, UserUpdateMeDto)
        kwargs['user_update_me_dto'] = user_update_me_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'update_my_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
