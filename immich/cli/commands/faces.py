"""Generated CLI commands for Faces tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A face is a detected human face within an asset, which can be associated with a person. Faces are normally detected via machine learning, but can also be created via manually.

Docs: https://api.immich.app/endpoints/faces"""
)


@app.command("create-face", deprecated=False)
def create_face(
    ctx: typer.Context,
    asset_id: str = typer.Option(..., "--asset-id", help="""Asset ID"""),
    height: int = typer.Option(..., "--height", help="""Face bounding box height"""),
    image_height: int = typer.Option(
        ..., "--image-height", help="""Image height in pixels"""
    ),
    image_width: int = typer.Option(
        ..., "--image-width", help="""Image width in pixels"""
    ),
    person_id: str = typer.Option(..., "--person-id", help="""Person ID"""),
    width: int = typer.Option(..., "--width", help="""Face bounding box width"""),
    x: int = typer.Option(..., "--x", help="""Face bounding box X coordinate"""),
    y: int = typer.Option(..., "--y", help="""Face bounding box Y coordinate"""),
) -> None:
    """Create a face

    Docs: https://api.immich.app/endpoints/faces/createFace
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["asset_id"], asset_id)
    set_nested(json_data, ["height"], height)
    set_nested(json_data, ["image_height"], image_height)
    set_nested(json_data, ["image_width"], image_width)
    set_nested(json_data, ["person_id"], person_id)
    set_nested(json_data, ["width"], width)
    set_nested(json_data, ["x"], x)
    set_nested(json_data, ["y"], y)
    from immich.client.models.asset_face_create_dto import AssetFaceCreateDto

    asset_face_create_dto = AssetFaceCreateDto.model_validate(json_data)
    kwargs["asset_face_create_dto"] = asset_face_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.faces, "create_face", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-face", deprecated=False)
def delete_face(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Face ID to delete"""),
    force: Literal["true", "false"] = typer.Option(
        ..., "--force", help="""Force delete even if person has other faces"""
    ),
) -> None:
    """Delete a face

    Docs: https://api.immich.app/endpoints/faces/deleteFace
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["force"], force.lower() == "true")
    from immich.client.models.asset_face_delete_dto import AssetFaceDeleteDto

    asset_face_delete_dto = AssetFaceDeleteDto.model_validate(json_data)
    kwargs["asset_face_delete_dto"] = asset_face_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.faces, "delete_face", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-faces", deprecated=False)
def get_faces(
    ctx: typer.Context,
    id: str = typer.Option(..., "--id", help="""Asset ID to retrieve faces for"""),
) -> None:
    """Retrieve faces for asset

    Docs: https://api.immich.app/endpoints/faces/getFaces
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.faces, "get_faces", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("reassign-faces-by-id", deprecated=False)
def reassign_faces_by_id(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Person ID to assign the face to"""),
    body_id: str = typer.Option(..., "--body-id", help="""Face ID"""),
) -> None:
    """Re-assign a face to another person

    Docs: https://api.immich.app/endpoints/faces/reassignFacesById
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["body_id"], body_id)
    from immich.client.models.face_dto import FaceDto

    face_dto = FaceDto.model_validate(json_data)
    kwargs["face_dto"] = face_dto
    client = ctx.obj["client"]
    result = run_command(client, client.faces, "reassign_faces_by_id", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
