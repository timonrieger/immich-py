"""Generated CLI commands for Activities tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Activities operations")

@app.command("create-activity")
def create_activity(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Create an activity"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    id: str,
    ctx: typer.Context,
) -> None:
    """Delete an activity"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.activities
    result = run_command(client, api_group, 'delete_activity', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-activities")
def get_activities(
    album_id: str = typer.Option(..., "--album-id"),
    asset_id: str | None = typer.Option(None, "--asset-id"),
    level: ReactionLevel | None = typer.Option(None, "--level"),
    type: ReactionType | None = typer.Option(None, "--type"),
    user_id: str | None = typer.Option(None, "--user-id"),
    ctx: typer.Context,
) -> None:
    """List all activities"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    album_id: str = typer.Option(..., "--album-id"),
    asset_id: str | None = typer.Option(None, "--asset-id"),
    ctx: typer.Context,
) -> None:
    """Retrieve activity statistics"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['album_id'] = album_id
    if asset_id is not None:
        kwargs['asset_id'] = asset_id
    client = ctx.obj['client']
    api_group = client.activities
    result = run_command(client, api_group, 'get_activity_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
