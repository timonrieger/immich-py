"""Generated CLI commands for Maintenance (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Maintenance mode allows you to put Immich in a read-only state to perform various operations.. https://api.immich.app/endpoints/maintenance-admin', context_settings={'help_option_names': ['-h', '--help']})

@app.command("maintenance-login")
def maintenance_login(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Log into maintenance mode"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.maintenance_login_dto import MaintenanceLoginDto
        maintenance_login_dto = deserialize_request_body(json_data, MaintenanceLoginDto)
        kwargs['maintenance_login_dto'] = maintenance_login_dto
    client = ctx.obj['client']
    api_group = client.maintenance_admin
    result = run_command(client, api_group, 'maintenance_login', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("set-maintenance-mode")
def set_maintenance_mode(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Set maintenance mode"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.set_maintenance_mode_dto import SetMaintenanceModeDto
        set_maintenance_mode_dto = deserialize_request_body(json_data, SetMaintenanceModeDto)
        kwargs['set_maintenance_mode_dto'] = set_maintenance_mode_dto
    client = ctx.obj['client']
    api_group = client.maintenance_admin
    result = run_command(client, api_group, 'set_maintenance_mode', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
