"""Generated CLI commands for Trash tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Endpoints for managing the trash can, which includes assets that have been discarded. Items in the trash are automatically deleted after a configured amount of time.

Docs: https://api.immich.app/endpoints/trash""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("empty-trash")
def empty_trash(
    ctx: typer.Context,
) -> None:
    """Empty trash

    Docs: https://api.immich.app/endpoints/trash/emptyTrash
    """
    kwargs = {}
    client = ctx.obj["client"]
    api_group = client.trash
    result = run_command(client, api_group, "empty_trash", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("restore-assets")
def restore_assets(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Restore assets

    Docs: https://api.immich.app/endpoints/trash/restoreAssets
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([ids])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    elif any(
        [
            ids,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ["ids"], ids)
        if json_data:
            from immich.client.models.bulk_ids_dto import BulkIdsDto

            bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
            kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    api_group = client.trash
    result = run_command(client, api_group, "restore_assets", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("restore-trash")
def restore_trash(
    ctx: typer.Context,
) -> None:
    """Restore trash

    Docs: https://api.immich.app/endpoints/trash/restoreTrash
    """
    kwargs = {}
    client = ctx.obj["client"]
    api_group = client.trash
    result = run_command(client, api_group, "restore_trash", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
