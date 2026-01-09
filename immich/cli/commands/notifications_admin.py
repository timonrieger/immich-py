"""Generated CLI commands for Notifications (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Notification administrative endpoints.. https://api.immich.app/endpoints/notifications-admin', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-notification")
def create_notification(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create a notification"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
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
    name: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Render email template"""
    kwargs = {}
    kwargs['name'] = name
    if json_str is not None:
        json_data = json.loads(json_str)
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
) -> None:
    """Send test email"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.system_config_smtp_dto import SystemConfigSmtpDto
        system_config_smtp_dto = deserialize_request_body(json_data, SystemConfigSmtpDto)
        kwargs['system_config_smtp_dto'] = system_config_smtp_dto
    client = ctx.obj['client']
    api_group = client.notifications_admin
    result = run_command(client, api_group, 'send_test_email_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
