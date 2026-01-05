"""Generated CLI commands for Maintenance (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Maintenance (admin) operations")

@app.command("maintenance-login")
def maintenance_login(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Log into maintenance mode"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Set maintenance mode"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.set_maintenance_mode_dto import SetMaintenanceModeDto
        set_maintenance_mode_dto = deserialize_request_body(json_data, SetMaintenanceModeDto)
        kwargs['set_maintenance_mode_dto'] = set_maintenance_mode_dto
    client = ctx.obj['client']
    api_group = client.maintenance_admin
    result = run_command(client, api_group, 'set_maintenance_mode', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
