"""Generated CLI commands for Activities tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='An activity is a like or a comment made by a user on an asset or album.. https://api.immich.app/endpoints/activities', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-activity")
def create_activity(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create an activity"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.activity_create_dto import ActivityCreateDto
        activity_create_dto = deserialize_request_body(json_data, ActivityCreateDto)
        kwargs['activity_create_dto'] = activity_create_dto
    client = ctx.obj['client']
    api_group = client.activities
    result = run_command(client, api_group, 'create_activity', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-activity")
def delete_activity(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete an activity"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.activities
    result = run_command(client, api_group, 'delete_activity', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-activities")
def get_activities(
    ctx: typer.Context,
    album_id: str = typer.Option(..., "--album-id"),
    asset_id: str | None = typer.Option(None, "--asset-id"),
    level: str | None = typer.Option(None, "--level"),
    type: str | None = typer.Option(None, "--type"),
    user_id: str | None = typer.Option(None, "--user-id"),
) -> None:
    """List all activities"""
    kwargs = {}
    kwargs['album_id'] = album_id
    if asset_id is not None:
        kwargs['asset_id'] = asset_id
    if level is not None:
        kwargs['level'] = level
    if type is not None:
        kwargs['type'] = type
    if user_id is not None:
        kwargs['user_id'] = user_id
    client = ctx.obj['client']
    api_group = client.activities
    result = run_command(client, api_group, 'get_activities', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-activity-statistics")
def get_activity_statistics(
    ctx: typer.Context,
    album_id: str = typer.Option(..., "--album-id"),
    asset_id: str | None = typer.Option(None, "--asset-id"),
) -> None:
    """Retrieve activity statistics"""
    kwargs = {}
    kwargs['album_id'] = album_id
    if asset_id is not None:
        kwargs['asset_id'] = asset_id
    client = ctx.obj['client']
    api_group = client.activities
    result = run_command(client, api_group, 'get_activity_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
