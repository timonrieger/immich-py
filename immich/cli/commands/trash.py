"""Generated CLI commands for Trash tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Endpoints for managing the trash can, which includes assets that have been discarded. Items in the trash are automatically deleted after a configured amount of time.\n\nDocs: https://api.immich.app/endpoints/trash"""
)


@app.command("empty-trash", deprecated=False)
def empty_trash(
    ctx: typer.Context,
) -> None:
    """Empty trash

    Docs: https://api.immich.app/endpoints/trash/emptyTrash
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.trash, "empty_trash", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("restore-assets", deprecated=False)
def restore_assets(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Restore assets

    Docs: https://api.immich.app/endpoints/trash/restoreAssets
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.trash, "restore_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("restore-trash", deprecated=False)
def restore_trash(
    ctx: typer.Context,
) -> None:
    """Restore trash

    Docs: https://api.immich.app/endpoints/trash/restoreTrash
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.trash, "restore_trash", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
