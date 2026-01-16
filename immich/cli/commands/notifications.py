"""Generated CLI commands for Notifications tag (auto-generated, do not edit)."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, parse_complex_list, print_response, run_command, set_nested

app = typer.Typer(help="""A notification is a specialized message sent to users to inform them of important events. Currently, these notifications are only shown in the Immich web application.

Docs: https://api.immich.app/endpoints/notifications""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("delete-notification")
def delete_notification(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a notification

Docs: https://api.immich.app/endpoints/notifications/deleteNotification
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    result = run_command(client, client.notifications, 'delete_notification', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-notifications")
def delete_notifications(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Delete notifications

Docs: https://api.immich.app/endpoints/notifications/deleteNotifications
    """
    kwargs = {}
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([ids]):
        json_data = {}
        set_nested(json_data, ['ids'], ids)
        from immich.client.models.notification_delete_all_dto import NotificationDeleteAllDto
        notification_delete_all_dto = deserialize_request_body(json_data, NotificationDeleteAllDto)
        kwargs['notification_delete_all_dto'] = notification_delete_all_dto
    client = ctx.obj['client']
    result = run_command(client, client.notifications, 'delete_notifications', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-notification")
def get_notification(
    ctx: typer.Context,
    id: str,
) -> None:
    """Get a notification

Docs: https://api.immich.app/endpoints/notifications/getNotification
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    result = run_command(client, client.notifications, 'get_notification', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-notifications")
def get_notifications(
    ctx: typer.Context,
    id: str | None = typer.Option(None, "--id"),
    level: str | None = typer.Option(None, "--level"),
    type: str | None = typer.Option(None, "--type"),
    unread: str | None = typer.Option(None, "--unread"),
) -> None:
    """Retrieve notifications

Docs: https://api.immich.app/endpoints/notifications/getNotifications
    """
    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if level is not None:
        kwargs['level'] = level
    if type is not None:
        kwargs['type'] = type
    if unread is not None:
        kwargs['unread'] = unread.lower() == 'true'
    client = ctx.obj['client']
    result = run_command(client, client.notifications, 'get_notifications', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-notification")
def update_notification(
    ctx: typer.Context,
    id: str,
    read_at: datetime | None = typer.Option(None, "--readAt"),
) -> None:
    """Update a notification

Docs: https://api.immich.app/endpoints/notifications/updateNotification
    """
    kwargs = {}
    kwargs['id'] = id
    has_flags = any([read_at])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([read_at]):
        json_data = {}
        if read_at is not None:
            set_nested(json_data, ['readAt'], read_at)
        from immich.client.models.notification_update_dto import NotificationUpdateDto
        notification_update_dto = deserialize_request_body(json_data, NotificationUpdateDto)
        kwargs['notification_update_dto'] = notification_update_dto
    client = ctx.obj['client']
    result = run_command(client, client.notifications, 'update_notification', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-notifications")
def update_notifications(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids"),
    read_at: datetime | None = typer.Option(None, "--readAt"),
) -> None:
    """Update notifications

Docs: https://api.immich.app/endpoints/notifications/updateNotifications
    """
    kwargs = {}
    has_flags = any([ids, read_at])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([ids, read_at]):
        json_data = {}
        set_nested(json_data, ['ids'], ids)
        if read_at is not None:
            set_nested(json_data, ['readAt'], read_at)
        from immich.client.models.notification_update_all_dto import NotificationUpdateAllDto
        notification_update_all_dto = deserialize_request_body(json_data, NotificationUpdateAllDto)
        kwargs['notification_update_all_dto'] = notification_update_all_dto
    client = ctx.obj['client']
    result = run_command(client, client.notifications, 'update_notifications', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
