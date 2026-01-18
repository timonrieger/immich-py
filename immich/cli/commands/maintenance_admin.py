"""Generated CLI commands for Maintenance (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Maintenance mode allows you to put Immich in a read-only state to perform various operations.\n\nDocs: https://api.immich.app/endpoints/maintenance-admin"""
)


@app.command("maintenance-login", deprecated=False)
def maintenance_login(
    ctx: typer.Context,
    token: str | None = typer.Option(None, "--token", help=""""""),
) -> None:
    """Log into maintenance mode

    Docs: https://api.immich.app/endpoints/maintenance-admin/maintenanceLogin
    """
    kwargs = {}
    json_data = {}
    if token is not None:
        set_nested(json_data, ["token"], token)
    from immich.client.models.maintenance_login_dto import MaintenanceLoginDto

    maintenance_login_dto = MaintenanceLoginDto.model_validate(json_data)
    kwargs["maintenance_login_dto"] = maintenance_login_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.maintenance_admin, "maintenance_login", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("set-maintenance-mode", deprecated=False)
def set_maintenance_mode(
    ctx: typer.Context,
    action: str = typer.Option(..., "--action", help=""""""),
) -> None:
    """Set maintenance mode

    Docs: https://api.immich.app/endpoints/maintenance-admin/setMaintenanceMode
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["action"], action)
    from immich.client.models.set_maintenance_mode_dto import SetMaintenanceModeDto

    set_maintenance_mode_dto = SetMaintenanceModeDto.model_validate(json_data)
    kwargs["set_maintenance_mode_dto"] = set_maintenance_mode_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.maintenance_admin, "set_maintenance_mode", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
