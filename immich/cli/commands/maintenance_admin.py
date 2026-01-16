"""Generated CLI commands for Maintenance (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, parse_complex_list, print_response, run_command, set_nested

app = typer.Typer(help="""Maintenance mode allows you to put Immich in a read-only state to perform various operations.

Docs: https://api.immich.app/endpoints/maintenance-admin""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("maintenance-login")
def maintenance_login(
    ctx: typer.Context,
    token: str | None = typer.Option(None, "--token"),
) -> None:
    """Log into maintenance mode

Docs: https://api.immich.app/endpoints/maintenance-admin/maintenanceLogin
    """
    kwargs = {}
    has_flags = any([token])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([token]):
        json_data = {}
        if token is not None:
            set_nested(json_data, ['token'], token)
        from immich.client.models.maintenance_login_dto import MaintenanceLoginDto
        maintenance_login_dto = deserialize_request_body(json_data, MaintenanceLoginDto)
        kwargs['maintenance_login_dto'] = maintenance_login_dto
    client = ctx.obj['client']
    result = run_command(client, client.maintenance_admin, 'maintenance_login', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("set-maintenance-mode")
def set_maintenance_mode(
    ctx: typer.Context,
    action: str = typer.Option(..., "--action"),
) -> None:
    """Set maintenance mode

Docs: https://api.immich.app/endpoints/maintenance-admin/setMaintenanceMode
    """
    kwargs = {}
    has_flags = any([action])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([action]):
        json_data = {}
        set_nested(json_data, ['action'], action)
        from immich.client.models.set_maintenance_mode_dto import SetMaintenanceModeDto
        set_maintenance_mode_dto = deserialize_request_body(json_data, SetMaintenanceModeDto)
        kwargs['set_maintenance_mode_dto'] = set_maintenance_mode_dto
    client = ctx.obj['client']
    result = run_command(client, client.maintenance_admin, 'set_maintenance_mode', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
