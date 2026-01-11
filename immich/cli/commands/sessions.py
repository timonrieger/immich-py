"""Generated CLI commands for Sessions tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""A session represents an authenticated login session for a user. Sessions also appear in the web application as "Authorized devices".

Docs: https://api.immich.app/endpoints/sessions""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-session")
def create_session(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    device_os: str | None = typer.Option(None, "--deviceOS", help="""Device OS"""),
    device_type: str | None = typer.Option(None, "--deviceType", help="""Device type"""),
    duration: float | None = typer.Option(None, "--duration", help="""Session duration in seconds"""),
) -> None:
    """Create a session

Docs: https://api.immich.app/endpoints/sessions/createSession
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([device_os, device_type, duration])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.session_create_dto import SessionCreateDto
        session_create_dto = deserialize_request_body(json_data, SessionCreateDto)
        kwargs['session_create_dto'] = session_create_dto
    elif any([
        device_os,
        device_type,
        duration,
    ]):
        # Build body from dotted flags
        json_data = {}
        if device_os is not None:
            set_nested(json_data, ['deviceOS'], device_os)
        if device_type is not None:
            set_nested(json_data, ['deviceType'], device_type)
        if duration is not None:
            set_nested(json_data, ['duration'], duration)
        if json_data:
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
    """Delete all sessions

Docs: https://api.immich.app/endpoints/sessions/deleteAllSessions
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'delete_all_sessions', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-session")
def delete_session(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Session ID"""),
) -> None:
    """Delete a session

Docs: https://api.immich.app/endpoints/sessions/deleteSession
    """
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
    """Retrieve sessions

Docs: https://api.immich.app/endpoints/sessions/getSessions
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'get_sessions', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("lock-session")
def lock_session(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Session ID"""),
) -> None:
    """Lock a session

Docs: https://api.immich.app/endpoints/sessions/lockSession
    """
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
    id: str = typer.Argument(..., help="""Session ID"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    is_pending_sync_reset: bool | None = typer.Option(None, "--isPendingSyncReset", help="""Reset pending sync state"""),
) -> None:
    """Update a session

Docs: https://api.immich.app/endpoints/sessions/updateSession
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([is_pending_sync_reset])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.session_update_dto import SessionUpdateDto
        session_update_dto = deserialize_request_body(json_data, SessionUpdateDto)
        kwargs['session_update_dto'] = session_update_dto
    elif any([
        is_pending_sync_reset,
    ]):
        # Build body from dotted flags
        json_data = {}
        if is_pending_sync_reset is not None:
            set_nested(json_data, ['isPendingSyncReset'], is_pending_sync_reset)
        if json_data:
            from immich.client.models.session_update_dto import SessionUpdateDto
            session_update_dto = deserialize_request_body(json_data, SessionUpdateDto)
            kwargs['session_update_dto'] = session_update_dto
    client = ctx.obj['client']
    api_group = client.sessions
    result = run_command(client, api_group, 'update_session', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
