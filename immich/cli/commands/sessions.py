"""Generated CLI commands for Sessions tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""A session represents an authenticated login session for a user. Sessions also appear in the web application as "Authorized devices".

Docs: https://api.immich.app/endpoints/sessions""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-session")
def create_session(
    ctx: typer.Context,
    device_os: str | None = typer.Option(None, "--deviceOS"),
    device_type: str | None = typer.Option(None, "--deviceType"),
    duration: float | None = typer.Option(
        None, "--duration", help="""session duration, in seconds"""
    ),
) -> None:
    """Create a session

    Docs: https://api.immich.app/endpoints/sessions/createSession
    """
    kwargs = {}
    has_flags = any([device_os, device_type, duration])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            device_os,
            device_type,
            duration,
        ]
    ):
        json_data = {}
        if device_os is not None:
            set_nested(json_data, ["deviceOS"], device_os)
        if device_type is not None:
            set_nested(json_data, ["deviceType"], device_type)
        if duration is not None:
            set_nested(json_data, ["duration"], duration)
        from immich.client.models.session_create_dto import SessionCreateDto

        session_create_dto = deserialize_request_body(json_data, SessionCreateDto)
        kwargs["session_create_dto"] = session_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "create_session", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-all-sessions")
def delete_all_sessions(
    ctx: typer.Context,
) -> None:
    """Delete all sessions

    Docs: https://api.immich.app/endpoints/sessions/deleteAllSessions
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "delete_all_sessions", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-session")
def delete_session(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a session

    Docs: https://api.immich.app/endpoints/sessions/deleteSession
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "delete_session", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-sessions")
def get_sessions(
    ctx: typer.Context,
) -> None:
    """Retrieve sessions

    Docs: https://api.immich.app/endpoints/sessions/getSessions
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "get_sessions", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("lock-session")
def lock_session(
    ctx: typer.Context,
    id: str,
) -> None:
    """Lock a session

    Docs: https://api.immich.app/endpoints/sessions/lockSession
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "lock_session", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-session")
def update_session(
    ctx: typer.Context,
    id: str,
    is_pending_sync_reset: bool | None = typer.Option(None, "--isPendingSyncReset"),
) -> None:
    """Update a session

    Docs: https://api.immich.app/endpoints/sessions/updateSession
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([is_pending_sync_reset])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            is_pending_sync_reset,
        ]
    ):
        json_data = {}
        if is_pending_sync_reset is not None:
            set_nested(json_data, ["isPendingSyncReset"], is_pending_sync_reset)
        from immich.client.models.session_update_dto import SessionUpdateDto

        session_update_dto = deserialize_request_body(json_data, SessionUpdateDto)
        kwargs["session_update_dto"] = session_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "update_session", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
