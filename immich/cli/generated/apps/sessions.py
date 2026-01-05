"""Generated CLI commands for Sessions tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Sessions operations")

@app.command("create-session")
def create_session(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Create a session"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update a session"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.session_update_dto import SessionUpdateDto
        session_update_dto = deserialize_request_body(json_data, SessionUpdateDto)
        kwargs['session_update_dto'] = session_update_dto
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'update_session', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
