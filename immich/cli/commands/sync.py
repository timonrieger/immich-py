"""Generated CLI commands for Sync tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""A collection of endpoints for the new mobile synchronization implementation.

Docs: https://api.immich.app/endpoints/sync""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("delete-sync-ack")
def delete_sync_ack(
    ctx: typer.Context,
    types: list[str] | None = typer.Option(None, "--types"),
) -> None:
    """Delete acknowledgements

    Docs: https://api.immich.app/endpoints/sync/deleteSyncAck
    """
    kwargs = {}
    has_flags = any([types])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            types,
        ]
    ):
        json_data = {}
        if types is not None:
            set_nested(json_data, ["types"], types)
        from immich.client.models.sync_ack_delete_dto import SyncAckDeleteDto

        sync_ack_delete_dto = deserialize_request_body(json_data, SyncAckDeleteDto)
        kwargs["sync_ack_delete_dto"] = sync_ack_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "delete_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-delta-sync")
def get_delta_sync(
    ctx: typer.Context,
    updated_after: str = typer.Option(..., "--updatedAfter"),
    user_ids: list[str] = typer.Option(..., "--userIds"),
) -> None:
    """Get delta sync for user

    Docs: https://api.immich.app/endpoints/sync/getDeltaSync
    """
    kwargs = {}
    has_flags = any([updated_after, user_ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            updated_after,
            user_ids,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["updatedAfter"], updated_after)
        set_nested(json_data, ["userIds"], user_ids)
        from immich.client.models.asset_delta_sync_dto import AssetDeltaSyncDto

        asset_delta_sync_dto = deserialize_request_body(json_data, AssetDeltaSyncDto)
        kwargs["asset_delta_sync_dto"] = asset_delta_sync_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "get_delta_sync", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-full-sync-for-user")
def get_full_sync_for_user(
    ctx: typer.Context,
    last_id: str | None = typer.Option(None, "--lastId"),
    limit: int = typer.Option(..., "--limit"),
    updated_until: str = typer.Option(..., "--updatedUntil"),
    user_id: str | None = typer.Option(None, "--userId"),
) -> None:
    """Get full sync for user

    Docs: https://api.immich.app/endpoints/sync/getFullSyncForUser
    """
    kwargs = {}
    has_flags = any([last_id, limit, updated_until, user_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            last_id,
            limit,
            updated_until,
            user_id,
        ]
    ):
        json_data = {}
        if last_id is not None:
            set_nested(json_data, ["lastId"], last_id)
        set_nested(json_data, ["limit"], limit)
        set_nested(json_data, ["updatedUntil"], updated_until)
        if user_id is not None:
            set_nested(json_data, ["userId"], user_id)
        from immich.client.models.asset_full_sync_dto import AssetFullSyncDto

        asset_full_sync_dto = deserialize_request_body(json_data, AssetFullSyncDto)
        kwargs["asset_full_sync_dto"] = asset_full_sync_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "get_full_sync_for_user", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-sync-ack")
def get_sync_ack(
    ctx: typer.Context,
) -> None:
    """Retrieve acknowledgements

    Docs: https://api.immich.app/endpoints/sync/getSyncAck
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "get_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-sync-stream")
def get_sync_stream(
    ctx: typer.Context,
    reset: bool | None = typer.Option(None, "--reset"),
    types: list[str] = typer.Option(..., "--types"),
) -> None:
    """Stream sync changes

    Docs: https://api.immich.app/endpoints/sync/getSyncStream
    """
    kwargs = {}
    has_flags = any([reset, types])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            reset,
            types,
        ]
    ):
        json_data = {}
        if reset is not None:
            set_nested(json_data, ["reset"], reset)
        set_nested(json_data, ["types"], types)
        from immich.client.models.sync_stream_dto import SyncStreamDto

        sync_stream_dto = deserialize_request_body(json_data, SyncStreamDto)
        kwargs["sync_stream_dto"] = sync_stream_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "get_sync_stream", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("send-sync-ack")
def send_sync_ack(
    ctx: typer.Context,
    acks: list[str] = typer.Option(..., "--acks"),
) -> None:
    """Acknowledge changes

    Docs: https://api.immich.app/endpoints/sync/sendSyncAck
    """
    kwargs = {}
    has_flags = any([acks])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            acks,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["acks"], acks)
        from immich.client.models.sync_ack_set_dto import SyncAckSetDto

        sync_ack_set_dto = deserialize_request_body(json_data, SyncAckSetDto)
        kwargs["sync_ack_set_dto"] = sync_ack_set_dto
    client = ctx.obj["client"]
    result = run_command(client, client.sync, "send_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
