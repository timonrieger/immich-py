"""Generated CLI commands for Maintenance (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""Maintenance mode allows you to put Immich in a read-only state to perform various operations.

Docs: https://api.immich.app/endpoints/maintenance-admin""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("maintenance-login")
def maintenance_login(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    token: str | None = typer.Option(None, "--token"),
) -> None:
    """Log into maintenance mode

Docs: https://api.immich.app/endpoints/maintenance-admin/maintenanceLogin
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([token])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.maintenance_login_dto import MaintenanceLoginDto
        maintenance_login_dto = deserialize_request_body(json_data, MaintenanceLoginDto)
        kwargs['maintenance_login_dto'] = maintenance_login_dto
    elif any([
        token,
    ]):
        # Build body from dotted flags
        json_data = {}
        if token is not None:
            set_nested(json_data, ['token'], token)
        if json_data:
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
    action: str = typer.Option(..., "--action"),
) -> None:
    """Set maintenance mode

Docs: https://api.immich.app/endpoints/maintenance-admin/setMaintenanceMode
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([action])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.set_maintenance_mode_dto import SetMaintenanceModeDto
        set_maintenance_mode_dto = deserialize_request_body(json_data, SetMaintenanceModeDto)
        kwargs['set_maintenance_mode_dto'] = set_maintenance_mode_dto
    elif any([
        action,
    ]):
        # Build body from dotted flags
        json_data = {}
        if action is None:
            raise SystemExit("Error: --action is required")
        set_nested(json_data, ['action'], action)
        if json_data:
            from immich.client.models.set_maintenance_mode_dto import SetMaintenanceModeDto
            set_maintenance_mode_dto = deserialize_request_body(json_data, SetMaintenanceModeDto)
            kwargs['set_maintenance_mode_dto'] = set_maintenance_mode_dto
    client = ctx.obj['client']
    api_group = client.maintenance_admin
    result = run_command(client, api_group, 'set_maintenance_mode', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
