"""Generated CLI commands for Libraries tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""An external library is made up of input file paths or expressions that are scanned for asset files. Discovered files are automatically imported. Assets much be unique within a library, but can be duplicated across libraries. Each user has a default upload library, and can have one or more external libraries.\n\n[link=https://api.immich.app/endpoints/libraries]Immich API documentation[/link]"""
)


@app.command("create-library", deprecated=False, rich_help_panel="API commands")
def create_library(
    ctx: typer.Context,
    exclusion_patterns: list[str] | None = typer.Option(
        None, "--exclusion-patterns", help=""""""
    ),
    import_paths: list[str] | None = typer.Option(None, "--import-paths", help=""""""),
    name: str | None = typer.Option(None, "--name", help=""""""),
    owner_id: str = typer.Option(..., "--owner-id", help=""""""),
) -> None:
    """Create a library

    [link=https://api.immich.app/endpoints/libraries/createLibrary]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if exclusion_patterns is not None:
        set_nested(json_data, ["exclusion_patterns"], exclusion_patterns)
    if import_paths is not None:
        set_nested(json_data, ["import_paths"], import_paths)
    if name is not None:
        set_nested(json_data, ["name"], name)
    set_nested(json_data, ["owner_id"], owner_id)
    create_library_dto = CreateLibraryDto.model_validate(json_data)
    kwargs["create_library_dto"] = create_library_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.libraries, "create_library", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-library", deprecated=False, rich_help_panel="API commands")
def delete_library(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a library

    [link=https://api.immich.app/endpoints/libraries/deleteLibrary]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.libraries, "delete_library", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-all-libraries", deprecated=False, rich_help_panel="API commands")
def get_all_libraries(
    ctx: typer.Context,
) -> None:
    """Retrieve libraries

    [link=https://api.immich.app/endpoints/libraries/getAllLibraries]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.libraries, "get_all_libraries", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-library", deprecated=False, rich_help_panel="API commands")
def get_library(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a library

    [link=https://api.immich.app/endpoints/libraries/getLibrary]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.libraries, "get_library", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-library-statistics", deprecated=False, rich_help_panel="API commands")
def get_library_statistics(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve library statistics

    [link=https://api.immich.app/endpoints/libraries/getLibraryStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.libraries, "get_library_statistics", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("scan-library", deprecated=False, rich_help_panel="API commands")
def scan_library(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Scan a library

    [link=https://api.immich.app/endpoints/libraries/scanLibrary]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.libraries, "scan_library", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-library", deprecated=False, rich_help_panel="API commands")
def update_library(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    exclusion_patterns: list[str] | None = typer.Option(
        None, "--exclusion-patterns", help=""""""
    ),
    import_paths: list[str] | None = typer.Option(None, "--import-paths", help=""""""),
    name: str | None = typer.Option(None, "--name", help=""""""),
) -> None:
    """Update a library

    [link=https://api.immich.app/endpoints/libraries/updateLibrary]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if exclusion_patterns is not None:
        set_nested(json_data, ["exclusion_patterns"], exclusion_patterns)
    if import_paths is not None:
        set_nested(json_data, ["import_paths"], import_paths)
    if name is not None:
        set_nested(json_data, ["name"], name)
    update_library_dto = UpdateLibraryDto.model_validate(json_data)
    kwargs["update_library_dto"] = update_library_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.libraries, "update_library", ctx, **kwargs)
    print_response(result, ctx)


@app.command("validate", deprecated=False, rich_help_panel="API commands")
def validate(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    exclusion_patterns: list[str] | None = typer.Option(
        None, "--exclusion-patterns", help=""""""
    ),
    import_paths: list[str] | None = typer.Option(None, "--import-paths", help=""""""),
) -> None:
    """Validate library settings

    [link=https://api.immich.app/endpoints/libraries/validate]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if exclusion_patterns is not None:
        set_nested(json_data, ["exclusion_patterns"], exclusion_patterns)
    if import_paths is not None:
        set_nested(json_data, ["import_paths"], import_paths)
    validate_library_dto = ValidateLibraryDto.model_validate(json_data)
    kwargs["validate_library_dto"] = validate_library_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.libraries, "validate", ctx, **kwargs)
    print_response(result, ctx)
