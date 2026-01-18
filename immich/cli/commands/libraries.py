"""Generated CLI commands for Libraries tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""An external library is made up of input file paths or expressions that are scanned for asset files. Discovered files are automatically imported. Assets much be unique within a library, but can be duplicated across libraries. Each user has a default upload library, and can have one or more external libraries.\n\nDocs: https://api.immich.app/endpoints/libraries"""
)


@app.command("create-library", deprecated=False)
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

    Docs: https://api.immich.app/endpoints/libraries/createLibrary
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
    from immich.client.models.create_library_dto import CreateLibraryDto

    create_library_dto = CreateLibraryDto.model_validate(json_data)
    kwargs["create_library_dto"] = create_library_dto
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "create_library", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-library", deprecated=False)
def delete_library(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a library

    Docs: https://api.immich.app/endpoints/libraries/deleteLibrary
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "delete_library", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-all-libraries", deprecated=False)
def get_all_libraries(
    ctx: typer.Context,
) -> None:
    """Retrieve libraries

    Docs: https://api.immich.app/endpoints/libraries/getAllLibraries
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "get_all_libraries", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-library", deprecated=False)
def get_library(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a library

    Docs: https://api.immich.app/endpoints/libraries/getLibrary
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "get_library", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-library-statistics", deprecated=False)
def get_library_statistics(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve library statistics

    Docs: https://api.immich.app/endpoints/libraries/getLibraryStatistics
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "get_library_statistics", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("scan-library", deprecated=False)
def scan_library(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Scan a library

    Docs: https://api.immich.app/endpoints/libraries/scanLibrary
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "scan_library", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-library", deprecated=False)
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

    Docs: https://api.immich.app/endpoints/libraries/updateLibrary
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
    from immich.client.models.update_library_dto import UpdateLibraryDto

    update_library_dto = UpdateLibraryDto.model_validate(json_data)
    kwargs["update_library_dto"] = update_library_dto
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "update_library", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("validate", deprecated=False)
def validate(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    exclusion_patterns: list[str] | None = typer.Option(
        None, "--exclusion-patterns", help=""""""
    ),
    import_paths: list[str] | None = typer.Option(None, "--import-paths", help=""""""),
) -> None:
    """Validate library settings

    Docs: https://api.immich.app/endpoints/libraries/validate
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if exclusion_patterns is not None:
        set_nested(json_data, ["exclusion_patterns"], exclusion_patterns)
    if import_paths is not None:
        set_nested(json_data, ["import_paths"], import_paths)
    from immich.client.models.validate_library_dto import ValidateLibraryDto

    validate_library_dto = ValidateLibraryDto.model_validate(json_data)
    kwargs["validate_library_dto"] = validate_library_dto
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "validate", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
