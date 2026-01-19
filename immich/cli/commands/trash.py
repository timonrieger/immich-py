"""Generated CLI commands for Trash tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Endpoints for managing the trash can, which includes assets that have been discarded. Items in the trash are automatically deleted after a configured amount of time.\n\nDocs: https://api.immich.app/endpoints/trash"""
)


@app.command("empty-trash", deprecated=False, rich_help_panel="API commands")
def empty_trash(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Empty trash

    Docs: https://api.immich.app/endpoints/trash/emptyTrash
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.trash, "empty_trash", ctx, **kwargs)
    print_response(result, ctx)


@app.command("restore-assets", deprecated=False, rich_help_panel="API commands")
def restore_assets(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:  # pragma: no cover
    """Restore assets

    Docs: https://api.immich.app/endpoints/trash/restoreAssets
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.trash, "restore_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("restore-trash", deprecated=False, rich_help_panel="API commands")
def restore_trash(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Restore trash

    Docs: https://api.immich.app/endpoints/trash/restoreTrash
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.trash, "restore_trash", ctx, **kwargs)
    print_response(result, ctx)
