"""Generated CLI commands for Sync tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A collection of endpoints for the new mobile synchronization implementation.\n\n[link=https://api.immich.app/endpoints/sync]Immich API documentation[/link]"""
)


@app.command("delete-sync-ack", deprecated=False, rich_help_panel="API commands")
def delete_sync_ack(
    ctx: typer.Context,
    types: list[SyncEntityType] | None = typer.Option(None, "--types", help=""""""),
) -> None:
    """Delete acknowledgements

    [link=https://api.immich.app/endpoints/sync/deleteSyncAck]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if types is not None:
        set_nested(json_data, ["types"], types)
    sync_ack_delete_dto = SyncAckDeleteDto.model_validate(json_data)
    kwargs["sync_ack_delete_dto"] = sync_ack_delete_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sync, "delete_sync_ack", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-delta-sync", deprecated=True, rich_help_panel="API commands")
def get_delta_sync(
    ctx: typer.Context,
    updated_after: datetime = typer.Option(..., "--updated-after", help=""""""),
    user_ids: list[str] = typer.Option(..., "--user-ids", help=""""""),
) -> None:
    """Get delta sync for user

    [link=https://api.immich.app/endpoints/sync/getDeltaSync]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["updated_after"], updated_after)
    set_nested(json_data, ["user_ids"], user_ids)
    asset_delta_sync_dto = AssetDeltaSyncDto.model_validate(json_data)
    kwargs["asset_delta_sync_dto"] = asset_delta_sync_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sync, "get_delta_sync", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-full-sync-for-user", deprecated=True, rich_help_panel="API commands")
def get_full_sync_for_user(
    ctx: typer.Context,
    last_id: str | None = typer.Option(None, "--last-id", help=""""""),
    limit: int = typer.Option(..., "--limit", help="""""", min=1),
    updated_until: datetime = typer.Option(..., "--updated-until", help=""""""),
    user_id: str | None = typer.Option(None, "--user-id", help=""""""),
) -> None:
    """Get full sync for user

    [link=https://api.immich.app/endpoints/sync/getFullSyncForUser]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if last_id is not None:
        set_nested(json_data, ["last_id"], last_id)
    set_nested(json_data, ["limit"], limit)
    set_nested(json_data, ["updated_until"], updated_until)
    if user_id is not None:
        set_nested(json_data, ["user_id"], user_id)
    asset_full_sync_dto = AssetFullSyncDto.model_validate(json_data)
    kwargs["asset_full_sync_dto"] = asset_full_sync_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sync, "get_full_sync_for_user", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-sync-ack", deprecated=False, rich_help_panel="API commands")
def get_sync_ack(
    ctx: typer.Context,
) -> None:
    """Retrieve acknowledgements

    [link=https://api.immich.app/endpoints/sync/getSyncAck]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sync, "get_sync_ack", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-sync-stream", deprecated=False, rich_help_panel="API commands")
def get_sync_stream(
    ctx: typer.Context,
    reset: Literal["true", "false"] | None = typer.Option(None, "--reset", help=""""""),
    types: list[SyncRequestType] = typer.Option(..., "--types", help=""""""),
) -> None:
    """Stream sync changes

    [link=https://api.immich.app/endpoints/sync/getSyncStream]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if reset is not None:
        set_nested(json_data, ["reset"], reset.lower() == "true")
    set_nested(json_data, ["types"], types)
    sync_stream_dto = SyncStreamDto.model_validate(json_data)
    kwargs["sync_stream_dto"] = sync_stream_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sync, "get_sync_stream", ctx, **kwargs)
    print_response(result, ctx)


@app.command("send-sync-ack", deprecated=False, rich_help_panel="API commands")
def send_sync_ack(
    ctx: typer.Context,
    acks: list[str] = typer.Option(..., "--acks", help=""""""),
) -> None:
    """Acknowledge changes

    [link=https://api.immich.app/endpoints/sync/sendSyncAck]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["acks"], acks)
    sync_ack_set_dto = SyncAckSetDto.model_validate(json_data)
    kwargs["sync_ack_set_dto"] = sync_ack_set_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.sync, "send_sync_ack", ctx, **kwargs)
    print_response(result, ctx)
