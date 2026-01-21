"""Generated CLI commands for Maintenance (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Maintenance mode allows you to put Immich in a read-only state to perform various operations.\n\n[link=https://api.immich.app/endpoints/maintenance-admin]Immich API documentation[/link]"""
)


@app.command("detect-prior-install", deprecated=False, rich_help_panel="API commands")
def detect_prior_install(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Detect existing install

    [link=https://api.immich.app/endpoints/maintenance-admin/detectPriorInstall]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.maintenance_admin, "detect_prior_install", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-maintenance-status", deprecated=False, rich_help_panel="API commands")
def get_maintenance_status(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get maintenance mode status

    [link=https://api.immich.app/endpoints/maintenance-admin/getMaintenanceStatus]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.maintenance_admin, "get_maintenance_status", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("maintenance-login", deprecated=False, rich_help_panel="API commands")
def maintenance_login(
    ctx: typer.Context,
    token: str | None = typer.Option(None, "--token", help=""""""),
) -> None:  # pragma: no cover
    """Log into maintenance mode

    [link=https://api.immich.app/endpoints/maintenance-admin/maintenanceLogin]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if token is not None:
        set_nested(json_data, ["token"], token)
    maintenance_login_dto = MaintenanceLoginDto.model_validate(json_data)
    kwargs["maintenance_login_dto"] = maintenance_login_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.maintenance_admin, "maintenance_login", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("set-maintenance-mode", deprecated=False, rich_help_panel="API commands")
def set_maintenance_mode(
    ctx: typer.Context,
    action: str = typer.Option(..., "--action", help=""""""),
    restore_backup_filename: str | None = typer.Option(
        None, "--restore-backup-filename", help=""""""
    ),
) -> None:  # pragma: no cover
    """Set maintenance mode

    [link=https://api.immich.app/endpoints/maintenance-admin/setMaintenanceMode]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["action"], action)
    if restore_backup_filename is not None:
        set_nested(json_data, ["restore_backup_filename"], restore_backup_filename)
    set_maintenance_mode_dto = SetMaintenanceModeDto.model_validate(json_data)
    kwargs["set_maintenance_mode_dto"] = set_maintenance_mode_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.maintenance_admin, "set_maintenance_mode", ctx, **kwargs
    )
    print_response(result, ctx)
