"""Generated CLI commands for Notifications (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    parse_complex_list,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Notification administrative endpoints.

Docs: https://api.immich.app/endpoints/notifications-admin""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-notification")
def create_notification(
    ctx: typer.Context,
    data: str | None = typer.Option(
        None,
        "--data",
        help="key=value pairs (repeatable); e.g. key1=value1,key2=value2",
    ),
    description: str | None = typer.Option(None, "--description"),
    level: str | None = typer.Option(None, "--level"),
    read_at: str | None = typer.Option(None, "--readAt"),
    title: str = typer.Option(..., "--title"),
    type: str | None = typer.Option(None, "--type"),
    user_id: str = typer.Option(..., "--userId"),
) -> None:
    """Create a notification

    Docs: https://api.immich.app/endpoints/notifications-admin/createNotification
    """
    kwargs = {}
    has_flags = any([data, description, level, read_at, title, type, user_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            data,
            description,
            level,
            read_at,
            title,
            type,
            user_id,
        ]
    ):
        json_data = {}
        if data is not None:
            value_data = parse_complex_list(data)
            set_nested(json_data, ["data"], value_data)
        if description is not None:
            set_nested(json_data, ["description"], description)
        if level is not None:
            set_nested(json_data, ["level"], level)
        if read_at is not None:
            set_nested(json_data, ["readAt"], read_at)
        set_nested(json_data, ["title"], title)
        if type is not None:
            set_nested(json_data, ["type"], type)
        set_nested(json_data, ["userId"], user_id)
        from immich.client.models.notification_create_dto import NotificationCreateDto

        notification_create_dto = deserialize_request_body(
            json_data, NotificationCreateDto
        )
        kwargs["notification_create_dto"] = notification_create_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.notifications_admin, "create_notification", **kwargs
    )
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-notification-template-admin")
def get_notification_template_admin(
    ctx: typer.Context,
    name: str,
    template: str = typer.Option(..., "--template"),
) -> None:
    """Render email template

    Docs: https://api.immich.app/endpoints/notifications-admin/getNotificationTemplateAdmin
    """
    kwargs = {}
    kwargs["name"] = name
    has_flags = any([template])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            template,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["template"], template)
        from immich.client.models.template_dto import TemplateDto

        template_dto = deserialize_request_body(json_data, TemplateDto)
        kwargs["template_dto"] = template_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.notifications_admin, "get_notification_template_admin", **kwargs
    )
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("send-test-email-admin")
def send_test_email_admin(
    ctx: typer.Context,
    enabled: bool = typer.Option(..., "--enabled"),
    from_: str = typer.Option(..., "--from"),
    reply_to: str = typer.Option(..., "--replyTo"),
    transport_host: str = typer.Option(..., "--transport.host"),
    transport_ignore_cert: bool = typer.Option(..., "--transport.ignoreCert"),
    transport_password: str = typer.Option(..., "--transport.password"),
    transport_port: float = typer.Option(..., "--transport.port"),
    transport_secure: bool = typer.Option(..., "--transport.secure"),
    transport_username: str = typer.Option(..., "--transport.username"),
) -> None:
    """Send test email

    Docs: https://api.immich.app/endpoints/notifications-admin/sendTestEmailAdmin
    """
    kwargs = {}
    has_flags = any(
        [
            enabled,
            from_,
            reply_to,
            transport_host,
            transport_ignore_cert,
            transport_password,
            transport_port,
            transport_secure,
            transport_username,
        ]
    )
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            enabled,
            from_,
            reply_to,
            transport_host,
            transport_ignore_cert,
            transport_password,
            transport_port,
            transport_secure,
            transport_username,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["enabled"], enabled)
        set_nested(json_data, ["from"], from_)
        set_nested(json_data, ["replyTo"], reply_to)
        set_nested(json_data, ["transport", "host"], transport_host)
        set_nested(json_data, ["transport", "ignoreCert"], transport_ignore_cert)
        set_nested(json_data, ["transport", "password"], transport_password)
        set_nested(json_data, ["transport", "port"], transport_port)
        set_nested(json_data, ["transport", "secure"], transport_secure)
        set_nested(json_data, ["transport", "username"], transport_username)
        from immich.client.models.system_config_smtp_dto import SystemConfigSmtpDto

        system_config_smtp_dto = deserialize_request_body(
            json_data, SystemConfigSmtpDto
        )
        kwargs["system_config_smtp_dto"] = system_config_smtp_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.notifications_admin, "send_test_email_admin", **kwargs
    )
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
