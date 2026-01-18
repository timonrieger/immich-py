"""Generated CLI commands for Sessions tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A session represents an authenticated login session for a user. Sessions also appear in the web application as "Authorized devices".\n\nDocs: https://api.immich.app/endpoints/sessions"""
)


@app.command("create-session", deprecated=False)
def create_session(
    ctx: typer.Context,
    device_os: str | None = typer.Option(None, "--device-os", help=""""""),
    device_type: str | None = typer.Option(None, "--device-type", help=""""""),
    duration: float | None = typer.Option(
        None, "--duration", help="""session duration, in seconds""", min=1
    ),
) -> None:
    """Create a session

    Docs: https://api.immich.app/endpoints/sessions/createSession
    """
    kwargs = {}
    json_data = {}
    if device_os is not None:
        set_nested(json_data, ["device_os"], device_os)
    if device_type is not None:
        set_nested(json_data, ["device_type"], device_type)
    if duration is not None:
        set_nested(json_data, ["duration"], duration)
    from immich.client.models.session_create_dto import SessionCreateDto

    session_create_dto = SessionCreateDto.model_validate(json_data)
    kwargs["session_create_dto"] = session_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "create_session", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-all-sessions", deprecated=False)
def delete_all_sessions(
    ctx: typer.Context,
) -> None:
    """Delete all sessions

    Docs: https://api.immich.app/endpoints/sessions/deleteAllSessions
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "delete_all_sessions", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-session", deprecated=False)
def delete_session(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a session

    Docs: https://api.immich.app/endpoints/sessions/deleteSession
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "delete_session", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-sessions", deprecated=False)
def get_sessions(
    ctx: typer.Context,
) -> None:
    """Retrieve sessions

    Docs: https://api.immich.app/endpoints/sessions/getSessions
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "get_sessions", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("lock-session", deprecated=False)
def lock_session(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Lock a session

    Docs: https://api.immich.app/endpoints/sessions/lockSession
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "lock_session", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-session", deprecated=False)
def update_session(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    is_pending_sync_reset: Literal["true", "false"] | None = typer.Option(
        None, "--is-pending-sync-reset", help=""""""
    ),
) -> None:
    """Update a session

    Docs: https://api.immich.app/endpoints/sessions/updateSession
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if is_pending_sync_reset is not None:
        set_nested(
            json_data,
            ["is_pending_sync_reset"],
            is_pending_sync_reset.lower() == "true",
        )
    from immich.client.models.session_update_dto import SessionUpdateDto

    session_update_dto = SessionUpdateDto.model_validate(json_data)
    kwargs["session_update_dto"] = session_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sessions, "update_session", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
