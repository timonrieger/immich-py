"""Generated CLI commands for Notifications (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
import json
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Notification administrative endpoints.\n\n[link=https://api.immich.app/endpoints/notifications-admin]Immich API documentation[/link]"""
)


@app.command("create-notification", deprecated=False, rich_help_panel="API commands")
def create_notification(
    ctx: typer.Context,
    data: str | None = typer.Option(None, "--data", help="""As a JSON string"""),
    description: str | None = typer.Option(None, "--description", help=""""""),
    level: str | None = typer.Option(None, "--level", help=""""""),
    read_at: datetime | None = typer.Option(None, "--read-at", help=""""""),
    title: str = typer.Option(..., "--title", help=""""""),
    type: str | None = typer.Option(None, "--type", help=""""""),
    user_id: str = typer.Option(..., "--user-id", help=""""""),
) -> None:
    """Create a notification

    [link=https://api.immich.app/endpoints/notifications-admin/createNotification]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if data is not None:
        value_data = [json.loads(i) for i in data]
        set_nested(json_data, ["data"], value_data)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if level is not None:
        set_nested(json_data, ["level"], level)
    if read_at is not None:
        set_nested(json_data, ["read_at"], read_at)
    set_nested(json_data, ["title"], title)
    if type is not None:
        set_nested(json_data, ["type"], type)
    set_nested(json_data, ["user_id"], user_id)
    notification_create_dto = NotificationCreateDto.model_validate(json_data)
    kwargs["notification_create_dto"] = notification_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.notifications_admin, "create_notification", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "get-notification-template-admin", deprecated=False, rich_help_panel="API commands"
)
def get_notification_template_admin(
    ctx: typer.Context,
    name: str = typer.Argument(..., help=""""""),
    template: str = typer.Option(..., "--template", help=""""""),
) -> None:
    """Render email template

    [link=https://api.immich.app/endpoints/notifications-admin/getNotificationTemplateAdmin]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["name"] = name
    set_nested(json_data, ["template"], template)
    template_dto = TemplateDto.model_validate(json_data)
    kwargs["template_dto"] = template_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client,
        client.notifications_admin,
        "get_notification_template_admin",
        ctx,
        **kwargs,
    )
    print_response(result, ctx)


@app.command("send-test-email-admin", deprecated=False, rich_help_panel="API commands")
def send_test_email_admin(
    ctx: typer.Context,
    enabled: bool = typer.Option(..., "--enabled", help=""""""),
    from_: str = typer.Option(..., "--from", help=""""""),
    reply_to: str = typer.Option(..., "--reply-to", help=""""""),
    transport_host: str = typer.Option(..., "--transport-host", help=""""""),
    transport_ignore_cert: bool = typer.Option(
        ..., "--transport-ignore-cert", help=""""""
    ),
    transport_password: str = typer.Option(..., "--transport-password", help=""""""),
    transport_port: float = typer.Option(
        ..., "--transport-port", help="""""", min=0, max=65535
    ),
    transport_secure: bool = typer.Option(..., "--transport-secure", help=""""""),
    transport_username: str = typer.Option(..., "--transport-username", help=""""""),
) -> None:
    """Send test email

    [link=https://api.immich.app/endpoints/notifications-admin/sendTestEmailAdmin]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["enabled"], enabled)
    set_nested(json_data, ["from_"], from_)
    set_nested(json_data, ["reply_to"], reply_to)
    set_nested(json_data, ["transport_host"], transport_host)
    set_nested(json_data, ["transport_ignore_cert"], transport_ignore_cert)
    set_nested(json_data, ["transport_password"], transport_password)
    set_nested(json_data, ["transport_port"], transport_port)
    set_nested(json_data, ["transport_secure"], transport_secure)
    set_nested(json_data, ["transport_username"], transport_username)
    system_config_smtp_dto = SystemConfigSmtpDto.model_validate(json_data)
    kwargs["system_config_smtp_dto"] = system_config_smtp_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.notifications_admin, "send_test_email_admin", ctx, **kwargs
    )
    print_response(result, ctx)
