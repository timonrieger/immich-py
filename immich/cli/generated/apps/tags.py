"""Generated CLI commands for Tags tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Tags operations")

@app.command("bulk-tag-assets")
def bulk_tag_assets(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Tag assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.tag_bulk_assets_dto import TagBulkAssetsDto
        tag_bulk_assets_dto = deserialize_request_body(json_data, TagBulkAssetsDto)
        kwargs['tag_bulk_assets_dto'] = tag_bulk_assets_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'bulk_tag_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("create-tag")
def create_tag(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Create a tag"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.tag_create_dto import TagCreateDto
        tag_create_dto = deserialize_request_body(json_data, TagCreateDto)
        kwargs['tag_create_dto'] = tag_create_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'create_tag', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-tag")
def delete_tag(
    id: str,
    ctx: typer.Context,
) -> None:
    """Delete a tag"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'delete_tag', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-tags")
def get_all_tags(
    ctx: typer.Context,
) -> None:
    """Retrieve tags"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'get_all_tags', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-tag-by-id")
def get_tag_by_id(
    id: str,
    ctx: typer.Context,
) -> None:
    """Retrieve a tag"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'get_tag_by_id', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("tag-assets")
def tag_assets(
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Tag assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'tag_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("untag-assets")
def untag_assets(
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Untag assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'untag_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-tag")
def update_tag(
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Update a tag"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.tag_update_dto import TagUpdateDto
        tag_update_dto = deserialize_request_body(json_data, TagUpdateDto)
        kwargs['tag_update_dto'] = tag_update_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'update_tag', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("upsert-tags")
def upsert_tags(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Upsert tags"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.tag_upsert_dto import TagUpsertDto
        tag_upsert_dto = deserialize_request_body(json_data, TagUpsertDto)
        kwargs['tag_upsert_dto'] = tag_upsert_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'upsert_tags', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
