"""Generated CLI commands for Notifications tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Notifications operations")

@app.command("delete-notification")
def delete_notification(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a notification"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.notifications
    result = run_command(client, api_group, 'delete_notification', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-notifications")
def delete_notifications(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Delete notifications"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.notification_delete_all_dto import NotificationDeleteAllDto
        notification_delete_all_dto = deserialize_request_body(json_data, NotificationDeleteAllDto)
        kwargs['notification_delete_all_dto'] = notification_delete_all_dto
    client = ctx.obj['client']
    api_group = client.notifications
    result = run_command(client, api_group, 'delete_notifications', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-notification")
def get_notification(
    ctx: typer.Context,
    id: str,
) -> None:
    """Get a notification"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.notifications
    result = run_command(client, api_group, 'get_notification', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-notifications")
def get_notifications(
    ctx: typer.Context,
    id: str | None = typer.Option(None, "--id"),
    level: str | None = typer.Option(None, "--level"),
    type: str | None = typer.Option(None, "--type"),
    unread: bool | None = typer.Option(None, "--unread"),
) -> None:
    """Retrieve notifications"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if level is not None:
        kwargs['level'] = level
    if type is not None:
        kwargs['type'] = type
    if unread is not None:
        kwargs['unread'] = unread
    client = ctx.obj['client']
    api_group = client.notifications
    result = run_command(client, api_group, 'get_notifications', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-notification")
def update_notification(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update a notification"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.notification_update_dto import NotificationUpdateDto
        notification_update_dto = deserialize_request_body(json_data, NotificationUpdateDto)
        kwargs['notification_update_dto'] = notification_update_dto
    client = ctx.obj['client']
    api_group = client.notifications
    result = run_command(client, api_group, 'update_notification', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-notifications")
def update_notifications(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update notifications"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.notification_update_all_dto import NotificationUpdateAllDto
        notification_update_all_dto = deserialize_request_body(json_data, NotificationUpdateAllDto)
        kwargs['notification_update_all_dto'] = notification_update_all_dto
    client = ctx.obj['client']
    api_group = client.notifications
    result = run_command(client, api_group, 'update_notifications', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
