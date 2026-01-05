"""Generated CLI commands for Faces tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Faces operations")

@app.command("create-face")
def create_face(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Create a face"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.asset_face_create_dto import AssetFaceCreateDto
        asset_face_create_dto = deserialize_request_body(json_data, AssetFaceCreateDto)
        kwargs['asset_face_create_dto'] = asset_face_create_dto
    client = ctx.obj['client']
    api_group = client.faces
    result = run_command(client, api_group, 'create_face', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-face")
def delete_face(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Delete a face"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.asset_face_delete_dto import AssetFaceDeleteDto
        asset_face_delete_dto = deserialize_request_body(json_data, AssetFaceDeleteDto)
        kwargs['asset_face_delete_dto'] = asset_face_delete_dto
    client = ctx.obj['client']
    api_group = client.faces
    result = run_command(client, api_group, 'delete_face', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-faces")
def get_faces(
    ctx: typer.Context,
    id: str = typer.Option(..., "--id"),
) -> None:
    """Retrieve faces for asset"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.faces
    result = run_command(client, api_group, 'get_faces', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("reassign-faces-by-id")
def reassign_faces_by_id(
    ctx: typer.Context,
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Re-assign a face to another person"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.face_dto import FaceDto
        face_dto = deserialize_request_body(json_data, FaceDto)
        kwargs['face_dto'] = face_dto
    client = ctx.obj['client']
    api_group = client.faces
    result = run_command(client, api_group, 'reassign_faces_by_id', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
