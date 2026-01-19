"""Generated CLI commands for Stacks tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A stack is a group of related assets. One asset is the "primary" asset, and the rest are "child" assets. On the main timeline, stack parents are included by default, while child assets are hidden.\n\nDocs: https://api.immich.app/endpoints/stacks"""
)


@app.command("create-stack", deprecated=False, rich_help_panel="API commands")
def create_stack(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(
        ..., "--asset-ids", help="""first asset becomes the primary"""
    ),
) -> None:  # pragma: no cover
    """Create a stack

    Docs: https://api.immich.app/endpoints/stacks/createStack
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["asset_ids"], asset_ids)
    stack_create_dto = StackCreateDto.model_validate(json_data)
    kwargs["stack_create_dto"] = stack_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.stacks, "create_stack", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-stack", deprecated=False, rich_help_panel="API commands")
def delete_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Delete a stack

    Docs: https://api.immich.app/endpoints/stacks/deleteStack
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.stacks, "delete_stack", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-stacks", deprecated=False, rich_help_panel="API commands")
def delete_stacks(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:  # pragma: no cover
    """Delete stacks

    Docs: https://api.immich.app/endpoints/stacks/deleteStacks
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.stacks, "delete_stacks", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-stack", deprecated=False, rich_help_panel="API commands")
def get_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Retrieve a stack

    Docs: https://api.immich.app/endpoints/stacks/getStack
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.stacks, "get_stack", ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "remove-asset-from-stack", deprecated=False, rich_help_panel="API commands"
)
def remove_asset_from_stack(
    ctx: typer.Context,
    asset_id: str = typer.Argument(..., help=""""""),
    id: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Remove an asset from a stack

    Docs: https://api.immich.app/endpoints/stacks/removeAssetFromStack
    """
    kwargs = {}
    kwargs["asset_id"] = asset_id
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.stacks, "remove_asset_from_stack", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("search-stacks", deprecated=False, rich_help_panel="API commands")
def search_stacks(
    ctx: typer.Context,
    primary_asset_id: str | None = typer.Option(
        None, "--primary-asset-id", help=""""""
    ),
) -> None:  # pragma: no cover
    """Retrieve stacks

    Docs: https://api.immich.app/endpoints/stacks/searchStacks
    """
    kwargs = {}
    if primary_asset_id is not None:
        kwargs["primary_asset_id"] = primary_asset_id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.stacks, "search_stacks", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-stack", deprecated=False, rich_help_panel="API commands")
def update_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    primary_asset_id: str | None = typer.Option(
        None, "--primary-asset-id", help=""""""
    ),
) -> None:  # pragma: no cover
    """Update a stack

    Docs: https://api.immich.app/endpoints/stacks/updateStack
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if primary_asset_id is not None:
        set_nested(json_data, ["primary_asset_id"], primary_asset_id)
    stack_update_dto = StackUpdateDto.model_validate(json_data)
    kwargs["stack_update_dto"] = stack_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.stacks, "update_stack", ctx, **kwargs)
    print_response(result, ctx)
