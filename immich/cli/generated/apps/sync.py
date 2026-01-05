"""Generated CLI commands for Sync tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Sync operations")

@app.command("delete-sync-ack")
def delete_sync_ack(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Delete acknowledgements"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.sync_ack_delete_dto import SyncAckDeleteDto
        sync_ack_delete_dto = deserialize_request_body(json_data, SyncAckDeleteDto)
        kwargs['sync_ack_delete_dto'] = sync_ack_delete_dto
    client = ctx.obj['client']
    api_group = client.sync
    result = run_command(client, api_group, 'delete_sync_ack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-delta-sync")
def get_delta_sync(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Get delta sync for user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.asset_delta_sync_dto import AssetDeltaSyncDto
        asset_delta_sync_dto = deserialize_request_body(json_data, AssetDeltaSyncDto)
        kwargs['asset_delta_sync_dto'] = asset_delta_sync_dto
    client = ctx.obj['client']
    api_group = client.sync
    result = run_command(client, api_group, 'get_delta_sync', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-full-sync-for-user")
def get_full_sync_for_user(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Get full sync for user"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.asset_full_sync_dto import AssetFullSyncDto
        asset_full_sync_dto = deserialize_request_body(json_data, AssetFullSyncDto)
        kwargs['asset_full_sync_dto'] = asset_full_sync_dto
    client = ctx.obj['client']
    api_group = client.sync
    result = run_command(client, api_group, 'get_full_sync_for_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-sync-ack")
def get_sync_ack(
    ctx: typer.Context,
) -> None:
    """Retrieve acknowledgements"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.sync
    result = run_command(client, api_group, 'get_sync_ack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-sync-stream")
def get_sync_stream(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Stream sync changes"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.sync_stream_dto import SyncStreamDto
        sync_stream_dto = deserialize_request_body(json_data, SyncStreamDto)
        kwargs['sync_stream_dto'] = sync_stream_dto
    client = ctx.obj['client']
    api_group = client.sync
    result = run_command(client, api_group, 'get_sync_stream', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("send-sync-ack")
def send_sync_ack(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Acknowledge changes"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.sync_ack_set_dto import SyncAckSetDto
        sync_ack_set_dto = deserialize_request_body(json_data, SyncAckSetDto)
        kwargs['sync_ack_set_dto'] = sync_ack_set_dto
    client = ctx.obj['client']
    api_group = client.sync
    result = run_command(client, api_group, 'send_sync_ack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
