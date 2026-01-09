"""Generated CLI commands for Faces tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='A face is a detected human face within an asset, which can be associated with a person. Faces are normally detected via machine learning, but can also be created via manually.. https://api.immich.app/endpoints/faces', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-face")
def create_face(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create a face"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
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
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Delete a face"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
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
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Re-assign a face to another person"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.face_dto import FaceDto
        face_dto = deserialize_request_body(json_data, FaceDto)
        kwargs['face_dto'] = face_dto
    client = ctx.obj['client']
    api_group = client.faces
    result = run_command(client, api_group, 'reassign_faces_by_id', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
