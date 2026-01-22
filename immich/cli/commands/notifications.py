"""Generated CLI commands for Notifications tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A notification is a specialized message sent to users to inform them of important events. Currently, these notifications are only shown in the Immich web application.\n\n[link=https://api.immich.app/endpoints/notifications]Immich API documentation[/link]"""
)


@app.command("delete-notification", deprecated=False, rich_help_panel="API commands")
def delete_notification(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a notification

    [link=https://api.immich.app/endpoints/notifications/deleteNotification]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.notifications, "delete_notification", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("delete-notifications", deprecated=False, rich_help_panel="API commands")
def delete_notifications(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Delete notifications

    [link=https://api.immich.app/endpoints/notifications/deleteNotifications]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    notification_delete_all_dto = NotificationDeleteAllDto.model_validate(json_data)
    kwargs["notification_delete_all_dto"] = notification_delete_all_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.notifications, "delete_notifications", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-notification", deprecated=False, rich_help_panel="API commands")
def get_notification(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Get a notification

    [link=https://api.immich.app/endpoints/notifications/getNotification]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.notifications, "get_notification", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-notifications", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/notifications/getNotifications]Immich API documentation[/link]
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
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.notifications, "get_notifications", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("update-notification", deprecated=False, rich_help_panel="API commands")
def update_notification(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    read_at: datetime | None = typer.Option(None, "--read-at", help=""""""),
) -> None:
    """Update a notification

    [link=https://api.immich.app/endpoints/notifications/updateNotification]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if read_at is not None:
        set_nested(json_data, ["read_at"], read_at)
    notification_update_dto = NotificationUpdateDto.model_validate(json_data)
    kwargs["notification_update_dto"] = notification_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.notifications, "update_notification", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("update-notifications", deprecated=False, rich_help_panel="API commands")
def update_notifications(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
    read_at: datetime | None = typer.Option(None, "--read-at", help=""""""),
) -> None:
    """Update notifications

    [link=https://api.immich.app/endpoints/notifications/updateNotifications]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    if read_at is not None:
        set_nested(json_data, ["read_at"], read_at)
    notification_update_all_dto = NotificationUpdateAllDto.model_validate(json_data)
    kwargs["notification_update_all_dto"] = notification_update_all_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.notifications, "update_notifications", ctx, **kwargs
    )
    print_response(result, ctx)
