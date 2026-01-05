"""Generated CLI commands for People tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="People operations")

@app.command("create-person")
def create_person(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Create a person"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.person_create_dto import PersonCreateDto
        person_create_dto = deserialize_request_body(json_data, PersonCreateDto)
        kwargs['person_create_dto'] = person_create_dto
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'create_person', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-people")
def delete_people(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Delete people"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'delete_people', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-person")
def delete_person(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete person"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'delete_person', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-people")
def get_all_people(
    ctx: typer.Context,
    closest_asset_id: str | None = typer.Option(None, "--closest-asset-id"),
    closest_person_id: str | None = typer.Option(None, "--closest-person-id"),
    page: float | None = typer.Option(None, "--page"),
    size: float | None = typer.Option(None, "--size"),
    with_hidden: bool | None = typer.Option(None, "--with-hidden"),
) -> None:
    """Get all people"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if closest_asset_id is not None:
        kwargs['closest_asset_id'] = closest_asset_id
    if closest_person_id is not None:
        kwargs['closest_person_id'] = closest_person_id
    if page is not None:
        kwargs['page'] = page
    if size is not None:
        kwargs['size'] = size
    if with_hidden is not None:
        kwargs['with_hidden'] = with_hidden
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'get_all_people', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-person")
def get_person(
    ctx: typer.Context,
    id: str,
) -> None:
    """Get a person"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'get_person', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-person-statistics")
def get_person_statistics(
    ctx: typer.Context,
    id: str,
) -> None:
    """Get person statistics"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'get_person_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-person-thumbnail")
def get_person_thumbnail(
    ctx: typer.Context,
    id: str,
) -> None:
    """Get person thumbnail"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'get_person_thumbnail', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("merge-person")
def merge_person(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Merge people"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.merge_person_dto import MergePersonDto
        merge_person_dto = deserialize_request_body(json_data, MergePersonDto)
        kwargs['merge_person_dto'] = merge_person_dto
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'merge_person', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("reassign-faces")
def reassign_faces(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Reassign faces"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.asset_face_update_dto import AssetFaceUpdateDto
        asset_face_update_dto = deserialize_request_body(json_data, AssetFaceUpdateDto)
        kwargs['asset_face_update_dto'] = asset_face_update_dto
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'reassign_faces', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-people")
def update_people(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update people"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.people_update_dto import PeopleUpdateDto
        people_update_dto = deserialize_request_body(json_data, PeopleUpdateDto)
        kwargs['people_update_dto'] = people_update_dto
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'update_people', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-person")
def update_person(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update person"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.person_update_dto import PersonUpdateDto
        person_update_dto = deserialize_request_body(json_data, PersonUpdateDto)
        kwargs['person_update_dto'] = person_update_dto
    client = ctx.obj['client']
    api_group = client.people
    result = run_command(client, api_group, 'update_person', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
