"""Generated CLI commands for Notifications tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""A notification is a specialized message sent to users to inform them of important events. Currently, these notifications are only shown in the Immich web application.

Docs: https://api.immich.app/endpoints/notifications""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("delete-notification")
def delete_notification(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Notification ID"""),
) -> None:
    """Delete a notification

Docs: https://api.immich.app/endpoints/notifications/deleteNotification
    """
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
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    ids: list[str] = typer.Option(..., "--ids", help="""Notification IDs to delete"""),
) -> None:
    """Delete notifications

Docs: https://api.immich.app/endpoints/notifications/deleteNotifications
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([ids])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.notification_delete_all_dto import NotificationDeleteAllDto
        notification_delete_all_dto = deserialize_request_body(json_data, NotificationDeleteAllDto)
        kwargs['notification_delete_all_dto'] = notification_delete_all_dto
    elif any([
        ids,
    ]):
        # Build body from dotted flags
        json_data = {}
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ['ids'], ids)
        if json_data:
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
    id: str = typer.Argument(..., help="""Notification ID"""),
) -> None:
    """Get a notification

Docs: https://api.immich.app/endpoints/notifications/getNotification
    """
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
    id: str | None = typer.Option(None, "--id", help="""Filter by notification ID"""),
    level: str | None = typer.Option(None, "--level", help="""Filter by notification level"""),
    type: str | None = typer.Option(None, "--type", help="""Filter by notification type"""),
    unread: bool | None = typer.Option(None, "--unread", help="""Filter by unread status"""),
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
        kwargs['unread'] = unread
    client = ctx.obj['client']
    api_group = client.notifications
    result = run_command(client, api_group, 'get_notifications', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-notification")
def update_notification(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Notification ID"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    read_at: str | None = typer.Option(None, "--readAt", help="""Date when notification was read"""),
) -> None:
    """Update a notification

Docs: https://api.immich.app/endpoints/notifications/updateNotification
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([read_at])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.notification_update_dto import NotificationUpdateDto
        notification_update_dto = deserialize_request_body(json_data, NotificationUpdateDto)
        kwargs['notification_update_dto'] = notification_update_dto
    elif any([
        read_at,
    ]):
        # Build body from dotted flags
        json_data = {}
        if read_at is not None:
            set_nested(json_data, ['readAt'], read_at)
        if json_data:
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
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    ids: list[str] = typer.Option(..., "--ids", help="""Notification IDs to update"""),
    read_at: str | None = typer.Option(None, "--readAt", help="""Date when notifications were read"""),
) -> None:
    """Update notifications

Docs: https://api.immich.app/endpoints/notifications/updateNotifications
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([ids, read_at])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.notification_update_all_dto import NotificationUpdateAllDto
        notification_update_all_dto = deserialize_request_body(json_data, NotificationUpdateAllDto)
        kwargs['notification_update_all_dto'] = notification_update_all_dto
    elif any([
        ids,
        read_at,
    ]):
        # Build body from dotted flags
        json_data = {}
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ['ids'], ids)
        if read_at is not None:
            set_nested(json_data, ['readAt'], read_at)
        if json_data:
            from immich.client.models.notification_update_all_dto import NotificationUpdateAllDto
            notification_update_all_dto = deserialize_request_body(json_data, NotificationUpdateAllDto)
            kwargs['notification_update_all_dto'] = notification_update_all_dto
    client = ctx.obj['client']
    api_group = client.notifications
    result = run_command(client, api_group, 'update_notifications', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
