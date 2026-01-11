"""Generated CLI commands for Sync tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
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
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    types: list[str] | None = typer.Option(
        None, "--types", help="""Sync entity types to delete acks for"""
    ),
) -> None:
    """Delete acknowledgements

    Docs: https://api.immich.app/endpoints/sync/deleteSyncAck
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([types])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.sync_ack_delete_dto import SyncAckDeleteDto

        sync_ack_delete_dto = deserialize_request_body(json_data, SyncAckDeleteDto)
        kwargs["sync_ack_delete_dto"] = sync_ack_delete_dto
    elif any(
        [
            types,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if types is not None:
            value_types = json.loads(types)
            set_nested(json_data, ["types"], value_types)
        if json_data:
            from immich.client.models.sync_ack_delete_dto import SyncAckDeleteDto

            sync_ack_delete_dto = deserialize_request_body(json_data, SyncAckDeleteDto)
            kwargs["sync_ack_delete_dto"] = sync_ack_delete_dto
    client = ctx.obj["client"]
    api_group = client.sync
    result = run_command(client, api_group, "delete_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-delta-sync")
def get_delta_sync(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    updated_after: str = typer.Option(
        ..., "--updatedAfter", help="""Sync assets updated after this date"""
    ),
    user_ids: list[str] = typer.Option(..., "--userIds", help="""User IDs to sync"""),
) -> None:
    """Get delta sync for user

    Docs: https://api.immich.app/endpoints/sync/getDeltaSync
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([updated_after, user_ids])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_delta_sync_dto import AssetDeltaSyncDto

        asset_delta_sync_dto = deserialize_request_body(json_data, AssetDeltaSyncDto)
        kwargs["asset_delta_sync_dto"] = asset_delta_sync_dto
    elif any(
        [
            updated_after,
            user_ids,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if updated_after is None:
            raise SystemExit("Error: --updatedAfter is required")
        set_nested(json_data, ["updatedAfter"], updated_after)
        if user_ids is None:
            raise SystemExit("Error: --userIds is required")
        set_nested(json_data, ["userIds"], user_ids)
        if json_data:
            from immich.client.models.asset_delta_sync_dto import AssetDeltaSyncDto

            asset_delta_sync_dto = deserialize_request_body(
                json_data, AssetDeltaSyncDto
            )
            kwargs["asset_delta_sync_dto"] = asset_delta_sync_dto
    client = ctx.obj["client"]
    api_group = client.sync
    result = run_command(client, api_group, "get_delta_sync", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-full-sync-for-user")
def get_full_sync_for_user(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    last_id: str | None = typer.Option(
        None, "--lastId", help="""Last asset ID (pagination)"""
    ),
    limit: int = typer.Option(
        ..., "--limit", help="""Maximum number of assets to return"""
    ),
    updated_until: str = typer.Option(
        ..., "--updatedUntil", help="""Sync assets updated until this date"""
    ),
    user_id: str | None = typer.Option(None, "--userId", help="""Filter by user ID"""),
) -> None:
    """Get full sync for user

    Docs: https://api.immich.app/endpoints/sync/getFullSyncForUser
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([last_id, limit, updated_until, user_id])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_full_sync_dto import AssetFullSyncDto

        asset_full_sync_dto = deserialize_request_body(json_data, AssetFullSyncDto)
        kwargs["asset_full_sync_dto"] = asset_full_sync_dto
    elif any(
        [
            last_id,
            limit,
            updated_until,
            user_id,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if last_id is not None:
            set_nested(json_data, ["lastId"], last_id)
        if limit is None:
            raise SystemExit("Error: --limit is required")
        set_nested(json_data, ["limit"], limit)
        if updated_until is None:
            raise SystemExit("Error: --updatedUntil is required")
        set_nested(json_data, ["updatedUntil"], updated_until)
        if user_id is not None:
            set_nested(json_data, ["userId"], user_id)
        if json_data:
            from immich.client.models.asset_full_sync_dto import AssetFullSyncDto

            asset_full_sync_dto = deserialize_request_body(json_data, AssetFullSyncDto)
            kwargs["asset_full_sync_dto"] = asset_full_sync_dto
    client = ctx.obj["client"]
    api_group = client.sync
    result = run_command(client, api_group, "get_full_sync_for_user", **kwargs)
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
    api_group = client.sync
    result = run_command(client, api_group, "get_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-sync-stream")
def get_sync_stream(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    reset: bool | None = typer.Option(None, "--reset", help="""Reset sync state"""),
    types: list[str] = typer.Option(..., "--types", help="""Sync request types"""),
) -> None:
    """Stream sync changes

    Docs: https://api.immich.app/endpoints/sync/getSyncStream
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([reset, types])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.sync_stream_dto import SyncStreamDto

        sync_stream_dto = deserialize_request_body(json_data, SyncStreamDto)
        kwargs["sync_stream_dto"] = sync_stream_dto
    elif any(
        [
            reset,
            types,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if reset is not None:
            set_nested(json_data, ["reset"], reset)
        if types is None:
            raise SystemExit("Error: --types is required")
        value_types = json.loads(types)
        set_nested(json_data, ["types"], value_types)
        if json_data:
            from immich.client.models.sync_stream_dto import SyncStreamDto

            sync_stream_dto = deserialize_request_body(json_data, SyncStreamDto)
            kwargs["sync_stream_dto"] = sync_stream_dto
    client = ctx.obj["client"]
    api_group = client.sync
    result = run_command(client, api_group, "get_sync_stream", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("send-sync-ack")
def send_sync_ack(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    acks: list[str] = typer.Option(
        ..., "--acks", help="""Acknowledgment IDs (max 1000)"""
    ),
) -> None:
    """Acknowledge changes

    Docs: https://api.immich.app/endpoints/sync/sendSyncAck
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([acks])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.sync_ack_set_dto import SyncAckSetDto

        sync_ack_set_dto = deserialize_request_body(json_data, SyncAckSetDto)
        kwargs["sync_ack_set_dto"] = sync_ack_set_dto
    elif any(
        [
            acks,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if acks is None:
            raise SystemExit("Error: --acks is required")
        set_nested(json_data, ["acks"], acks)
        if json_data:
            from immich.client.models.sync_ack_set_dto import SyncAckSetDto

            sync_ack_set_dto = deserialize_request_body(json_data, SyncAckSetDto)
            kwargs["sync_ack_set_dto"] = sync_ack_set_dto
    client = ctx.obj["client"]
    api_group = client.sync
    result = run_command(client, api_group, "send_sync_ack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
