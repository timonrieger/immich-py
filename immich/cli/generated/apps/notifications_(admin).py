"""Generated CLI commands for Notifications (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Notifications (admin) operations")

@app.command("create-notification")
def create_notification(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Create a notification"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.notification_create_dto import NotificationCreateDto
        notification_create_dto = deserialize_request_body(json_data, NotificationCreateDto)
        kwargs['notification_create_dto'] = notification_create_dto
    client = ctx.obj['client']
    api_group = client.notifications_(admin)
    result = run_command(client, api_group, 'create_notification', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-notification-template-admin")
def get_notification_template_admin(
    name: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Render email template"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['name'] = name
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.template_dto import TemplateDto
        template_dto = deserialize_request_body(json_data, TemplateDto)
        kwargs['template_dto'] = template_dto
    client = ctx.obj['client']
    api_group = client.notifications_(admin)
    result = run_command(client, api_group, 'get_notification_template_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("send-test-email-admin")
def send_test_email_admin(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Send test email"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.system_config_smtp_dto import SystemConfigSmtpDto
        system_config_smtp_dto = deserialize_request_body(json_data, SystemConfigSmtpDto)
        kwargs['system_config_smtp_dto'] = system_config_smtp_dto
    client = ctx.obj['client']
    api_group = client.notifications_(admin)
    result = run_command(client, api_group, 'send_test_email_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
