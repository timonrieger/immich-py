"""Generated CLI commands for Sync tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A collection of endpoints for the new mobile synchronization implementation.\n\nDocs: https://api.immich.app/endpoints/sync"""
)


@app.command("delete-sync-ack", deprecated=False)
def delete_sync_ack(
    ctx: typer.Context,
    types: list[SyncEntityType] | None = typer.Option(None, "--types", help=""""""),
) -> None:
    """Delete acknowledgements

    Docs: https://api.immich.app/endpoints/sync/deleteSyncAck
    """
    kwargs = {}
    json_data = {}
    if types is not None:
        set_nested(json_data, ["types"], types)
    from immich.client.models.sync_ack_delete_dto import SyncAckDeleteDto

    sync_ack_delete_dto = SyncAckDeleteDto.model_validate(json_data)
    kwargs["sync_ack_delete_dto"] = sync_ack_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "delete_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-delta-sync", deprecated=True)
def get_delta_sync(
    ctx: typer.Context,
    updated_after: datetime = typer.Option(..., "--updated-after", help=""""""),
    user_ids: list[str] = typer.Option(..., "--user-ids", help=""""""),
) -> None:
    """Get delta sync for user

    Docs: https://api.immich.app/endpoints/sync/getDeltaSync
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["updated_after"], updated_after)
    set_nested(json_data, ["user_ids"], user_ids)
    from immich.client.models.asset_delta_sync_dto import AssetDeltaSyncDto

    asset_delta_sync_dto = AssetDeltaSyncDto.model_validate(json_data)
    kwargs["asset_delta_sync_dto"] = asset_delta_sync_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "get_delta_sync", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-full-sync-for-user", deprecated=True)
def get_full_sync_for_user(
    ctx: typer.Context,
    last_id: str | None = typer.Option(None, "--last-id", help=""""""),
    limit: int = typer.Option(..., "--limit", help="""""", min=1),
    updated_until: datetime = typer.Option(..., "--updated-until", help=""""""),
    user_id: str | None = typer.Option(None, "--user-id", help=""""""),
) -> None:
    """Get full sync for user

    Docs: https://api.immich.app/endpoints/sync/getFullSyncForUser
    """
    kwargs = {}
    json_data = {}
    if last_id is not None:
        set_nested(json_data, ["last_id"], last_id)
    set_nested(json_data, ["limit"], limit)
    set_nested(json_data, ["updated_until"], updated_until)
    if user_id is not None:
        set_nested(json_data, ["user_id"], user_id)
    from immich.client.models.asset_full_sync_dto import AssetFullSyncDto

    asset_full_sync_dto = AssetFullSyncDto.model_validate(json_data)
    kwargs["asset_full_sync_dto"] = asset_full_sync_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "get_full_sync_for_user", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-sync-ack", deprecated=False)
def get_sync_ack(
    ctx: typer.Context,
) -> None:
    """Retrieve acknowledgements

    Docs: https://api.immich.app/endpoints/sync/getSyncAck
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "get_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-sync-stream", deprecated=False)
def get_sync_stream(
    ctx: typer.Context,
    reset: Literal["true", "false"] | None = typer.Option(None, "--reset", help=""""""),
    types: list[SyncRequestType] = typer.Option(..., "--types", help=""""""),
) -> None:
    """Stream sync changes

    Docs: https://api.immich.app/endpoints/sync/getSyncStream
    """
    kwargs = {}
    json_data = {}
    if reset is not None:
        set_nested(json_data, ["reset"], reset.lower() == "true")
    set_nested(json_data, ["types"], types)
    from immich.client.models.sync_stream_dto import SyncStreamDto

    sync_stream_dto = SyncStreamDto.model_validate(json_data)
    kwargs["sync_stream_dto"] = sync_stream_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "get_sync_stream", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("send-sync-ack", deprecated=False)
def send_sync_ack(
    ctx: typer.Context,
    acks: list[str] = typer.Option(..., "--acks", help=""""""),
) -> None:
    """Acknowledge changes

    Docs: https://api.immich.app/endpoints/sync/sendSyncAck
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["acks"], acks)
    from immich.client.models.sync_ack_set_dto import SyncAckSetDto

    sync_ack_set_dto = SyncAckSetDto.model_validate(json_data)
    kwargs["sync_ack_set_dto"] = sync_ack_set_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "send_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
