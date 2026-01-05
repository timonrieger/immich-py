"""Generated CLI commands for Libraries tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Libraries operations")

@app.command("create-library")
def create_library(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Create a library"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.create_library_dto import CreateLibraryDto
        create_library_dto = deserialize_request_body(json_data, CreateLibraryDto)
        kwargs['create_library_dto'] = create_library_dto
    client = ctx.obj['client']
    api_group = client.libraries
    result = run_command(client, api_group, 'create_library', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-library")
def delete_library(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a library"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.libraries
    result = run_command(client, api_group, 'delete_library', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-libraries")
def get_all_libraries(
    ctx: typer.Context,
) -> None:
    """Retrieve libraries"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.libraries
    result = run_command(client, api_group, 'get_all_libraries', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-library")
def get_library(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a library"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.libraries
    result = run_command(client, api_group, 'get_library', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-library-statistics")
def get_library_statistics(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve library statistics"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.libraries
    result = run_command(client, api_group, 'get_library_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("scan-library")
def scan_library(
    ctx: typer.Context,
    id: str,
) -> None:
    """Scan a library"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.libraries
    result = run_command(client, api_group, 'scan_library', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-library")
def update_library(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update a library"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.update_library_dto import UpdateLibraryDto
        update_library_dto = deserialize_request_body(json_data, UpdateLibraryDto)
        kwargs['update_library_dto'] = update_library_dto
    client = ctx.obj['client']
    api_group = client.libraries
    result = run_command(client, api_group, 'update_library', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("validate")
def validate(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Validate library settings"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.validate_library_dto import ValidateLibraryDto
        validate_library_dto = deserialize_request_body(json_data, ValidateLibraryDto)
        kwargs['validate_library_dto'] = validate_library_dto
    client = ctx.obj['client']
    api_group = client.libraries
    result = run_command(client, api_group, 'validate', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
