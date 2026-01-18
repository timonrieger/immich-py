"""Generated CLI commands for Stacks tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A stack is a group of related assets. One asset is the "primary" asset, and the rest are "child" assets. On the main timeline, stack parents are included by default, while child assets are hidden.\n\nDocs: https://api.immich.app/endpoints/stacks"""
)


@app.command("create-stack", deprecated=False)
def create_stack(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(
        ..., "--asset-ids", help="""first asset becomes the primary"""
    ),
) -> None:
    """Create a stack

    Docs: https://api.immich.app/endpoints/stacks/createStack
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["asset_ids"], asset_ids)
    from immich.client.models.stack_create_dto import StackCreateDto

    stack_create_dto = StackCreateDto.model_validate(json_data)
    kwargs["stack_create_dto"] = stack_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "create_stack", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-stack", deprecated=False)
def delete_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a stack

    Docs: https://api.immich.app/endpoints/stacks/deleteStack
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "delete_stack", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-stacks", deprecated=False)
def delete_stacks(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Delete stacks

    Docs: https://api.immich.app/endpoints/stacks/deleteStacks
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "delete_stacks", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-stack", deprecated=False)
def get_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a stack

    Docs: https://api.immich.app/endpoints/stacks/getStack
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "get_stack", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("remove-asset-from-stack", deprecated=False)
def remove_asset_from_stack(
    ctx: typer.Context,
    asset_id: str = typer.Argument(..., help=""""""),
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Remove an asset from a stack

    Docs: https://api.immich.app/endpoints/stacks/removeAssetFromStack
    """
    kwargs = {}
    kwargs["asset_id"] = asset_id
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "remove_asset_from_stack", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("search-stacks", deprecated=False)
def search_stacks(
    ctx: typer.Context,
    primary_asset_id: str | None = typer.Option(
        None, "--primary-asset-id", help=""""""
    ),
) -> None:
    """Retrieve stacks

    Docs: https://api.immich.app/endpoints/stacks/searchStacks
    """
    kwargs = {}
    if primary_asset_id is not None:
        kwargs["primary_asset_id"] = primary_asset_id
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "search_stacks", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-stack", deprecated=False)
def update_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    primary_asset_id: str | None = typer.Option(
        None, "--primary-asset-id", help=""""""
    ),
) -> None:
    """Update a stack

    Docs: https://api.immich.app/endpoints/stacks/updateStack
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if primary_asset_id is not None:
        set_nested(json_data, ["primary_asset_id"], primary_asset_id)
    from immich.client.models.stack_update_dto import StackUpdateDto

    stack_update_dto = StackUpdateDto.model_validate(json_data)
    kwargs["stack_update_dto"] = stack_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "update_stack", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
