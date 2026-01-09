"""Generated CLI commands for Sessions tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='A session represents an authenticated login session for a user. Sessions also appear in the web application as "Authorized devices".. https://api.immich.app/endpoints/sessions', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-session")
def create_session(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create a session"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.session_create_dto import SessionCreateDto
        session_create_dto = deserialize_request_body(json_data, SessionCreateDto)
        kwargs['session_create_dto'] = session_create_dto
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'create_session', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-all-sessions")
def delete_all_sessions(
    ctx: typer.Context,
) -> None:
    """Delete all sessions"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'delete_all_sessions', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-session")
def delete_session(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a session"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'delete_session', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-sessions")
def get_sessions(
    ctx: typer.Context,
) -> None:
    """Retrieve sessions"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'get_sessions', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("lock-session")
def lock_session(
    ctx: typer.Context,
    id: str,
) -> None:
    """Lock a session"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'lock_session', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-session")
def update_session(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update a session"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.session_update_dto import SessionUpdateDto
        session_update_dto = deserialize_request_body(json_data, SessionUpdateDto)
        kwargs['session_update_dto'] = session_update_dto
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'update_session', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
