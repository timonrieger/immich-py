"""Generated CLI commands for Users (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Users (admin) operations")

@app.command("create-user-admin")
def create_user_admin(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Create a user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.user_admin_create_dto import UserAdminCreateDto
        user_admin_create_dto = deserialize_request_body(json_data, UserAdminCreateDto)
        kwargs['user_admin_create_dto'] = user_admin_create_dto
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'create_user_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-user-admin")
def delete_user_admin(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Delete a user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.user_admin_delete_dto import UserAdminDeleteDto
        user_admin_delete_dto = deserialize_request_body(json_data, UserAdminDeleteDto)
        kwargs['user_admin_delete_dto'] = user_admin_delete_dto
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'delete_user_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user-admin")
def get_user_admin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'get_user_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user-preferences-admin")
def get_user_preferences_admin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve user preferences"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'get_user_preferences_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user-sessions-admin")
def get_user_sessions_admin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve user sessions"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'get_user_sessions_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user-statistics-admin")
def get_user_statistics_admin(
    ctx: typer.Context,
    id: str,
    is_favorite: bool | None = typer.Option(None, "--is-favorite"),
    is_trashed: bool | None = typer.Option(None, "--is-trashed"),
    visibility: str | None = typer.Option(None, "--visibility"),
) -> None:
    """Retrieve user statistics"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if is_favorite is not None:
        kwargs['is_favorite'] = is_favorite
    if is_trashed is not None:
        kwargs['is_trashed'] = is_trashed
    if visibility is not None:
        kwargs['visibility'] = visibility
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'get_user_statistics_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("restore-user-admin")
def restore_user_admin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Restore a deleted user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'restore_user_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-users-admin")
def search_users_admin(
    ctx: typer.Context,
    id: str | None = typer.Option(None, "--id"),
    with_deleted: bool | None = typer.Option(None, "--with-deleted"),
) -> None:
    """Search users"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if with_deleted is not None:
        kwargs['with_deleted'] = with_deleted
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'search_users_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-user-admin")
def update_user_admin(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update a user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.user_admin_update_dto import UserAdminUpdateDto
        user_admin_update_dto = deserialize_request_body(json_data, UserAdminUpdateDto)
        kwargs['user_admin_update_dto'] = user_admin_update_dto
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'update_user_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-user-preferences-admin")
def update_user_preferences_admin(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update user preferences"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.user_preferences_update_dto import UserPreferencesUpdateDto
        user_preferences_update_dto = deserialize_request_body(json_data, UserPreferencesUpdateDto)
        kwargs['user_preferences_update_dto'] = user_preferences_update_dto
    client = ctx.obj['client']
    api_group = client.users_admin
    result = run_command(client, api_group, 'update_user_preferences_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
