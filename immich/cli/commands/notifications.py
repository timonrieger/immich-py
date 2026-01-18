"""Generated CLI commands for Notifications tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A notification is a specialized message sent to users to inform them of important events. Currently, these notifications are only shown in the Immich web application.\n\nDocs: https://api.immich.app/endpoints/notifications"""
)


@app.command("delete-notification", deprecated=False)
def delete_notification(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a notification

    Docs: https://api.immich.app/endpoints/notifications/deleteNotification
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.notifications, "delete_notification", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-notifications", deprecated=False)
def delete_notifications(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Delete notifications

    Docs: https://api.immich.app/endpoints/notifications/deleteNotifications
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.notification_delete_all_dto import (
        NotificationDeleteAllDto,
    )

    notification_delete_all_dto = NotificationDeleteAllDto.model_validate(json_data)
    kwargs["notification_delete_all_dto"] = notification_delete_all_dto
    client = ctx.obj["client"]
    result = run_command(client, client.notifications, "delete_notifications", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-notification", deprecated=False)
def get_notification(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Get a notification

    Docs: https://api.immich.app/endpoints/notifications/getNotification
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.notifications, "get_notification", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-notifications", deprecated=False)
def get_notifications(
    ctx: typer.Context,
    id: str | None = typer.Option(None, "--id", help=""""""),
    level: NotificationLevel | None = typer.Option(None, "--level", help=""""""),
    type: NotificationType | None = typer.Option(None, "--type", help=""""""),
    unread: Literal["true", "false"] | None = typer.Option(
        None, "--unread", help=""""""
    ),
) -> None:
    """Retrieve notifications

    Docs: https://api.immich.app/endpoints/notifications/getNotifications
    """
    kwargs = {}
    if id is not None:
        kwargs["id"] = id
    if level is not None:
        kwargs["level"] = level
    if type is not None:
        kwargs["type"] = type
    if unread is not None:
        kwargs["unread"] = unread.lower() == "true"
    client = ctx.obj["client"]
    result = run_command(client, client.notifications, "get_notifications", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-notification", deprecated=False)
def update_notification(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    read_at: datetime | None = typer.Option(None, "--read-at", help=""""""),
) -> None:
    """Update a notification

    Docs: https://api.immich.app/endpoints/notifications/updateNotification
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if read_at is not None:
        set_nested(json_data, ["read_at"], read_at)
    from immich.client.models.notification_update_dto import NotificationUpdateDto

    notification_update_dto = NotificationUpdateDto.model_validate(json_data)
    kwargs["notification_update_dto"] = notification_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.notifications, "update_notification", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-notifications", deprecated=False)
def update_notifications(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
    read_at: datetime | None = typer.Option(None, "--read-at", help=""""""),
) -> None:
    """Update notifications

    Docs: https://api.immich.app/endpoints/notifications/updateNotifications
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    if read_at is not None:
        set_nested(json_data, ["read_at"], read_at)
    from immich.client.models.notification_update_all_dto import (
        NotificationUpdateAllDto,
    )

    notification_update_all_dto = NotificationUpdateAllDto.model_validate(json_data)
    kwargs["notification_update_all_dto"] = notification_update_all_dto
    client = ctx.obj["client"]
    result = run_command(client, client.notifications, "update_notifications", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
