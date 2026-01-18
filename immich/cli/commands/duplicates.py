"""Generated CLI commands for Duplicates tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Endpoints for managing and identifying duplicate assets.\n\nDocs: https://api.immich.app/endpoints/duplicates"""
)


@app.command("delete-duplicate", deprecated=False)
def delete_duplicate(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a duplicate

    Docs: https://api.immich.app/endpoints/duplicates/deleteDuplicate
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.duplicates, "delete_duplicate", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-duplicates", deprecated=False)
def delete_duplicates(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Delete duplicates

    Docs: https://api.immich.app/endpoints/duplicates/deleteDuplicates
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.duplicates, "delete_duplicates", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-asset-duplicates", deprecated=False)
def get_asset_duplicates(
    ctx: typer.Context,
) -> None:
    """Retrieve duplicates

    Docs: https://api.immich.app/endpoints/duplicates/getAssetDuplicates
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.duplicates, "get_asset_duplicates", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
