"""Generated CLI commands for Users tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Users operations")

@app.command("create-profile-image")
def create_profile_image(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with multipart fields (non-file)"),
    file: Path = typer.Option(..., "--file", help="File to upload for file"),
    ctx: typer.Context,
) -> None:
    """Create user profile image"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    json_data = load_json_file(json_path) if json_path is not None else {}
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_my_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-profile-image")
def get_profile_image(
    id: str,
    ctx: typer.Context,
) -> None:
    """Retrieve user profile image"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_profile_image', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user")
def get_user(
    id: str,
    ctx: typer.Context,
) -> None:
    """Retrieve a user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'search_users', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("set-user-license")
def set_user_license(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Set user product key"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Update user onboarding"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Update my preferences"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Update current user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.user_update_me_dto import UserUpdateMeDto
        user_update_me_dto = deserialize_request_body(json_data, UserUpdateMeDto)
        kwargs['user_update_me_dto'] = user_update_me_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'update_my_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
