"""Generated CLI commands for Sessions tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A session represents an authenticated login session for a user. Sessions also appear in the web application as "Authorized devices".\n\nDocs: https://api.immich.app/endpoints/sessions"""
)


@app.command("create-session", deprecated=False, rich_help_panel="API commands")
def create_session(
    ctx: typer.Context,
    device_os: str | None = typer.Option(None, "--device-os", help=""""""),
    device_type: str | None = typer.Option(None, "--device-type", help=""""""),
    duration: float | None = typer.Option(
        None, "--duration", help="""session duration, in seconds""", min=1
    ),
) -> None:  # pragma: no cover
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
    session_create_dto = SessionCreateDto.model_validate(json_data)
    kwargs["session_create_dto"] = session_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sessions, "create_session", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-all-sessions", deprecated=False, rich_help_panel="API commands")
def delete_all_sessions(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Delete all sessions

    Docs: https://api.immich.app/endpoints/sessions/deleteAllSessions
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sessions, "delete_all_sessions", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-session", deprecated=False, rich_help_panel="API commands")
def delete_session(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Delete a session

    Docs: https://api.immich.app/endpoints/sessions/deleteSession
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sessions, "delete_session", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-sessions", deprecated=False, rich_help_panel="API commands")
def get_sessions(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Retrieve sessions

    Docs: https://api.immich.app/endpoints/sessions/getSessions
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sessions, "get_sessions", ctx, **kwargs)
    print_response(result, ctx)


@app.command("lock-session", deprecated=False, rich_help_panel="API commands")
def lock_session(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Lock a session

    Docs: https://api.immich.app/endpoints/sessions/lockSession
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sessions, "lock_session", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-session", deprecated=False, rich_help_panel="API commands")
def update_session(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    is_pending_sync_reset: Literal["true", "false"] | None = typer.Option(
        None, "--is-pending-sync-reset", help=""""""
    ),
) -> None:  # pragma: no cover
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
    session_update_dto = SessionUpdateDto.model_validate(json_data)
    kwargs["session_update_dto"] = session_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sessions, "update_session", ctx, **kwargs)
    print_response(result, ctx)
