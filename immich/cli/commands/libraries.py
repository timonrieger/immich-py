"""Generated CLI commands for Libraries tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""An external library is made up of input file paths or expressions that are scanned for asset files. Discovered files are automatically imported. Assets much be unique within a library, but can be duplicated across libraries. Each user has a default upload library, and can have one or more external libraries.

Docs: https://api.immich.app/endpoints/libraries""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-library")
def create_library(
    ctx: typer.Context,
    exclusion_patterns: list[str] | None = typer.Option(None, "--exclusionPatterns"),
    import_paths: list[str] | None = typer.Option(None, "--importPaths"),
    name: str | None = typer.Option(None, "--name"),
    owner_id: str = typer.Option(..., "--ownerId"),
) -> None:
    """Create a library

    Docs: https://api.immich.app/endpoints/libraries/createLibrary
    """
    kwargs = {}
    has_flags = any([exclusion_patterns, import_paths, name, owner_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([exclusion_patterns, import_paths, name, owner_id]):
        json_data = {}
        if exclusion_patterns is not None:
            set_nested(json_data, ["exclusionPatterns"], exclusion_patterns)
        if import_paths is not None:
            set_nested(json_data, ["importPaths"], import_paths)
        if name is not None:
            set_nested(json_data, ["name"], name)
        set_nested(json_data, ["ownerId"], owner_id)
        from immich.client.models.create_library_dto import CreateLibraryDto

        create_library_dto = deserialize_request_body(json_data, CreateLibraryDto)
        kwargs["create_library_dto"] = create_library_dto
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "create_library", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-library")
def delete_library(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a library

    Docs: https://api.immich.app/endpoints/libraries/deleteLibrary
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "delete_library", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-all-libraries")
def get_all_libraries(
    ctx: typer.Context,
) -> None:
    """Retrieve libraries

    Docs: https://api.immich.app/endpoints/libraries/getAllLibraries
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "get_all_libraries", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-library")
def get_library(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a library

    Docs: https://api.immich.app/endpoints/libraries/getLibrary
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "get_library", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-library-statistics")
def get_library_statistics(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve library statistics

    Docs: https://api.immich.app/endpoints/libraries/getLibraryStatistics
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "get_library_statistics", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("scan-library")
def scan_library(
    ctx: typer.Context,
    id: str,
) -> None:
    """Scan a library

    Docs: https://api.immich.app/endpoints/libraries/scanLibrary
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "scan_library", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-library")
def update_library(
    ctx: typer.Context,
    id: str,
    exclusion_patterns: list[str] | None = typer.Option(None, "--exclusionPatterns"),
    import_paths: list[str] | None = typer.Option(None, "--importPaths"),
    name: str | None = typer.Option(None, "--name"),
) -> None:
    """Update a library

    Docs: https://api.immich.app/endpoints/libraries/updateLibrary
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([exclusion_patterns, import_paths, name])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([exclusion_patterns, import_paths, name]):
        json_data = {}
        if exclusion_patterns is not None:
            set_nested(json_data, ["exclusionPatterns"], exclusion_patterns)
        if import_paths is not None:
            set_nested(json_data, ["importPaths"], import_paths)
        if name is not None:
            set_nested(json_data, ["name"], name)
        from immich.client.models.update_library_dto import UpdateLibraryDto

        update_library_dto = deserialize_request_body(json_data, UpdateLibraryDto)
        kwargs["update_library_dto"] = update_library_dto
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "update_library", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("validate")
def validate(
    ctx: typer.Context,
    id: str,
    exclusion_patterns: list[str] | None = typer.Option(None, "--exclusionPatterns"),
    import_paths: list[str] | None = typer.Option(None, "--importPaths"),
) -> None:
    """Validate library settings

    Docs: https://api.immich.app/endpoints/libraries/validate
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([exclusion_patterns, import_paths])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([exclusion_patterns, import_paths]):
        json_data = {}
        if exclusion_patterns is not None:
            set_nested(json_data, ["exclusionPatterns"], exclusion_patterns)
        if import_paths is not None:
            set_nested(json_data, ["importPaths"], import_paths)
        from immich.client.models.validate_library_dto import ValidateLibraryDto

        validate_library_dto = deserialize_request_body(json_data, ValidateLibraryDto)
        kwargs["validate_library_dto"] = validate_library_dto
    client = ctx.obj["client"]
    result = run_command(client, client.libraries, "validate", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
