"""Generated CLI commands for Notifications (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""Notification administrative endpoints.

Docs: https://api.immich.app/endpoints/notifications-admin""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-notification")
def create_notification(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    data: str | None = typer.Option(None, "--data", help="""Additional notification data"""),
    description: str | None = typer.Option(None, "--description", help="""Notification description"""),
    level: str | None = typer.Option(None, "--level", help="""Notification level"""),
    read_at: str | None = typer.Option(None, "--readAt", help="""Date when notification was read"""),
    title: str = typer.Option(..., "--title", help="""Notification title"""),
    type: str | None = typer.Option(None, "--type", help="""Notification type"""),
    user_id: str = typer.Option(..., "--userId", help="""User ID to send notification to"""),
) -> None:
    """Create a notification

Docs: https://api.immich.app/endpoints/notifications-admin/createNotification
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([data, description, level, read_at, title, type, user_id])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.notification_create_dto import NotificationCreateDto
        notification_create_dto = deserialize_request_body(json_data, NotificationCreateDto)
        kwargs['notification_create_dto'] = notification_create_dto
    elif any([
        data,
        description,
        level,
        read_at,
        title,
        type,
        user_id,
    ]):
        # Build body from dotted flags
        json_data = {}
        if data is not None:
            value_data = json.loads(data)
            set_nested(json_data, ['data'], value_data)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if level is not None:
            set_nested(json_data, ['level'], level)
        if read_at is not None:
            set_nested(json_data, ['readAt'], read_at)
        if title is None:
            raise SystemExit("Error: --title is required")
        set_nested(json_data, ['title'], title)
        if type is not None:
            set_nested(json_data, ['type'], type)
        if user_id is None:
            raise SystemExit("Error: --userId is required")
        set_nested(json_data, ['userId'], user_id)
        if json_data:
            from immich.client.models.notification_create_dto import NotificationCreateDto
            notification_create_dto = deserialize_request_body(json_data, NotificationCreateDto)
            kwargs['notification_create_dto'] = notification_create_dto
    client = ctx.obj['client']
    api_group = client.notifications_admin
    result = run_command(client, api_group, 'create_notification', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-notification-template-admin")
def get_notification_template_admin(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="""Email template name"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    template: str = typer.Option(..., "--template", help="""Template name"""),
) -> None:
    """Render email template

Docs: https://api.immich.app/endpoints/notifications-admin/getNotificationTemplateAdmin
    """
    kwargs = {}
    kwargs['name'] = name
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([template])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.template_dto import TemplateDto
        template_dto = deserialize_request_body(json_data, TemplateDto)
        kwargs['template_dto'] = template_dto
    elif any([
        template,
    ]):
        # Build body from dotted flags
        json_data = {}
        if template is None:
            raise SystemExit("Error: --template is required")
        set_nested(json_data, ['template'], template)
        if json_data:
            from immich.client.models.template_dto import TemplateDto
            template_dto = deserialize_request_body(json_data, TemplateDto)
            kwargs['template_dto'] = template_dto
    client = ctx.obj['client']
    api_group = client.notifications_admin
    result = run_command(client, api_group, 'get_notification_template_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("send-test-email-admin")
def send_test_email_admin(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    enabled: bool = typer.Option(..., "--enabled", help="""Whether SMTP email notifications are enabled"""),
    from_: str = typer.Option(..., "--from", help="""Email address to send from"""),
    reply_to: str = typer.Option(..., "--replyTo", help="""Email address for replies"""),
    transport_host: str = typer.Option(..., "--transport.host", help="""SMTP server hostname"""),
    transport_ignore_cert: bool = typer.Option(..., "--transport.ignoreCert", help="""Whether to ignore SSL certificate errors"""),
    transport_password: str = typer.Option(..., "--transport.password", help="""SMTP password"""),
    transport_port: float = typer.Option(..., "--transport.port", help="""SMTP server port"""),
    transport_secure: bool = typer.Option(..., "--transport.secure", help="""Whether to use secure connection (TLS/SSL)"""),
    transport_username: str = typer.Option(..., "--transport.username", help="""SMTP username"""),
) -> None:
    """Send test email

Docs: https://api.immich.app/endpoints/notifications-admin/sendTestEmailAdmin
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([enabled, from_, reply_to, transport_host, transport_ignore_cert, transport_password, transport_port, transport_secure, transport_username])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.system_config_smtp_dto import SystemConfigSmtpDto
        system_config_smtp_dto = deserialize_request_body(json_data, SystemConfigSmtpDto)
        kwargs['system_config_smtp_dto'] = system_config_smtp_dto
    elif any([
        enabled,
        from_,
        reply_to,
        transport_host,
        transport_ignore_cert,
        transport_password,
        transport_port,
        transport_secure,
        transport_username,
    ]):
        # Build body from dotted flags
        json_data = {}
        if enabled is None:
            raise SystemExit("Error: --enabled is required")
        set_nested(json_data, ['enabled'], enabled)
        if from_ is None:
            raise SystemExit("Error: --from is required")
        set_nested(json_data, ['from'], from_)
        if reply_to is None:
            raise SystemExit("Error: --replyTo is required")
        set_nested(json_data, ['replyTo'], reply_to)
        if transport_host is None:
            raise SystemExit("Error: --transport.host is required")
        set_nested(json_data, ['transport', 'host'], transport_host)
        if transport_ignore_cert is None:
            raise SystemExit("Error: --transport.ignoreCert is required")
        set_nested(json_data, ['transport', 'ignoreCert'], transport_ignore_cert)
        if transport_password is None:
            raise SystemExit("Error: --transport.password is required")
        set_nested(json_data, ['transport', 'password'], transport_password)
        if transport_port is None:
            raise SystemExit("Error: --transport.port is required")
        set_nested(json_data, ['transport', 'port'], transport_port)
        if transport_secure is None:
            raise SystemExit("Error: --transport.secure is required")
        set_nested(json_data, ['transport', 'secure'], transport_secure)
        if transport_username is None:
            raise SystemExit("Error: --transport.username is required")
        set_nested(json_data, ['transport', 'username'], transport_username)
        if json_data:
            from immich.client.models.system_config_smtp_dto import SystemConfigSmtpDto
            system_config_smtp_dto = deserialize_request_body(json_data, SystemConfigSmtpDto)
            kwargs['system_config_smtp_dto'] = system_config_smtp_dto
    client = ctx.obj['client']
    api_group = client.notifications_admin
    result = run_command(client, api_group, 'send_test_email_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
