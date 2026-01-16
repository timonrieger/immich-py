"""Generated CLI commands for Stacks tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""A stack is a group of related assets. One asset is the "primary" asset, and the rest are "child" assets. On the main timeline, stack parents are included by default, while child assets are hidden.

Docs: https://api.immich.app/endpoints/stacks""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-stack")
def create_stack(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(
        ..., "--assetIds", help="""first asset becomes the primary"""
    ),
) -> None:
    """Create a stack

    Docs: https://api.immich.app/endpoints/stacks/createStack
    """
    kwargs = {}
    has_flags = any([asset_ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            asset_ids,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["assetIds"], asset_ids)
        from immich.client.models.stack_create_dto import StackCreateDto

        stack_create_dto = deserialize_request_body(json_data, StackCreateDto)
        kwargs["stack_create_dto"] = stack_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "create_stack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-stack")
def delete_stack(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a stack

    Docs: https://api.immich.app/endpoints/stacks/deleteStack
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "delete_stack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-stacks")
def delete_stacks(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Delete stacks

    Docs: https://api.immich.app/endpoints/stacks/deleteStacks
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
    result = run_command(client, client.stacks, "delete_stacks", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-stack")
def get_stack(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a stack

    Docs: https://api.immich.app/endpoints/stacks/getStack
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "get_stack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("remove-asset-from-stack")
def remove_asset_from_stack(
    ctx: typer.Context,
    asset_id: str,
    id: str,
) -> None:
    """Remove an asset from a stack

    Docs: https://api.immich.app/endpoints/stacks/removeAssetFromStack
    """
    kwargs = {}
    kwargs["asset_id"] = asset_id
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "remove_asset_from_stack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("search-stacks")
def search_stacks(
    ctx: typer.Context,
    primary_asset_id: str | None = typer.Option(None, "--primary-asset-id"),
) -> None:
    """Retrieve stacks

    Docs: https://api.immich.app/endpoints/stacks/searchStacks
    """
    kwargs = {}
    if primary_asset_id is not None:
        kwargs["primary_asset_id"] = primary_asset_id
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "search_stacks", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-stack")
def update_stack(
    ctx: typer.Context,
    id: str,
    primary_asset_id: str | None = typer.Option(None, "--primaryAssetId"),
) -> None:
    """Update a stack

    Docs: https://api.immich.app/endpoints/stacks/updateStack
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([primary_asset_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            primary_asset_id,
        ]
    ):
        json_data = {}
        if primary_asset_id is not None:
            set_nested(json_data, ["primaryAssetId"], primary_asset_id)
        from immich.client.models.stack_update_dto import StackUpdateDto

        stack_update_dto = deserialize_request_body(json_data, StackUpdateDto)
        kwargs["stack_update_dto"] = stack_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.stacks, "update_stack", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
