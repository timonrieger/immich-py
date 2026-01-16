"""Generated CLI commands for Duplicates tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Endpoints for managing and identifying duplicate assets.

Docs: https://api.immich.app/endpoints/duplicates""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("delete-duplicate")
def delete_duplicate(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a duplicate

    Docs: https://api.immich.app/endpoints/duplicates/deleteDuplicate
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.duplicates, "delete_duplicate", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-duplicates")
def delete_duplicates(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Delete duplicates

    Docs: https://api.immich.app/endpoints/duplicates/deleteDuplicates
    """
    kwargs = {}
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            ids,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["ids"], ids)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.duplicates, "delete_duplicates", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-asset-duplicates")
def get_asset_duplicates(
    ctx: typer.Context,
) -> None:
    """Retrieve duplicates

    Docs: https://api.immich.app/endpoints/duplicates/getAssetDuplicates
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.duplicates, "get_asset_duplicates", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
