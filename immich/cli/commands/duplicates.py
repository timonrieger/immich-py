"""Generated CLI commands for Duplicates tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Endpoints for managing and identifying duplicate assets.\n\n[link=https://api.immich.app/endpoints/duplicates]Immich API documentation[/link]"""
)


@app.command("delete-duplicate", deprecated=False, rich_help_panel="API commands")
def delete_duplicate(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a duplicate

    [link=https://api.immich.app/endpoints/duplicates/deleteDuplicate]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.duplicates, "delete_duplicate", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-duplicates", deprecated=False, rich_help_panel="API commands")
def delete_duplicates(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Delete duplicates

    [link=https://api.immich.app/endpoints/duplicates/deleteDuplicates]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.duplicates, "delete_duplicates", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-asset-duplicates", deprecated=False, rich_help_panel="API commands")
def get_asset_duplicates(
    ctx: typer.Context,
) -> None:
    """Retrieve duplicates

    [link=https://api.immich.app/endpoints/duplicates/getAssetDuplicates]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.duplicates, "get_asset_duplicates", ctx, **kwargs
    )
    print_response(result, ctx)
