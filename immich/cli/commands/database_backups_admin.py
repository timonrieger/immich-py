"""Generated CLI commands for Database Backups (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Manage backups of the Immich database.\n\n[link=https://api.immich.app/endpoints/database-backups-admin]Immich API documentation[/link]"""
)


@app.command("delete-database-backup", deprecated=False, rich_help_panel="API commands")
def delete_database_backup(
    ctx: typer.Context,
    backups: list[str] = typer.Option(..., "--backups", help=""""""),
) -> None:  # pragma: no cover
    """Delete database backup

    [link=https://api.immich.app/endpoints/database-backups-admin/deleteDatabaseBackup]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["backups"], backups)
    database_backup_delete_dto = DatabaseBackupDeleteDto.model_validate(json_data)
    kwargs["database_backup_delete_dto"] = database_backup_delete_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.database_backups_admin, "delete_database_backup", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "download-database-backup", deprecated=False, rich_help_panel="API commands"
)
def download_database_backup(
    ctx: typer.Context,
    filename: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Download database backup

    [link=https://api.immich.app/endpoints/database-backups-admin/downloadDatabaseBackup]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["filename"] = filename
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.database_backups_admin, "download_database_backup", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("list-database-backups", deprecated=False, rich_help_panel="API commands")
def list_database_backups(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """List database backups

    [link=https://api.immich.app/endpoints/database-backups-admin/listDatabaseBackups]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.database_backups_admin, "list_database_backups", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "start-database-restore-flow", deprecated=False, rich_help_panel="API commands"
)
def start_database_restore_flow(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Start database backup restore flow

    [link=https://api.immich.app/endpoints/database-backups-admin/startDatabaseRestoreFlow]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client,
        client.database_backups_admin,
        "start_database_restore_flow",
        ctx,
        **kwargs,
    )
    print_response(result, ctx)


@app.command("upload-database-backup", deprecated=False, rich_help_panel="API commands")
def upload_database_backup(
    ctx: typer.Context,
    file: Path | None = typer.Option(None, "--file", help="""""", exists=True),
) -> None:  # pragma: no cover
    """Upload database backup

    [link=https://api.immich.app/endpoints/database-backups-admin/uploadDatabaseBackup]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if file is not None:
        set_nested(json_data, ["file"], (file.name, file.read_bytes()))
    database_backup_upload_dto = DatabaseBackupUploadDto.model_validate(json_data)
    kwargs["database_backup_upload_dto"] = database_backup_upload_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.database_backups_admin, "upload_database_backup", ctx, **kwargs
    )
    print_response(result, ctx)
