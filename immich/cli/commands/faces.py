"""Generated CLI commands for Faces tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A face is a detected human face within an asset, which can be associated with a person. Faces are normally detected via machine learning, but can also be created via manually.\n\n[link=https://api.immich.app/endpoints/faces]Immich API documentation[/link]"""
)


@app.command("create-face", deprecated=False, rich_help_panel="API commands")
def create_face(
    ctx: typer.Context,
    asset_id: str = typer.Option(..., "--asset-id", help=""""""),
    height: int = typer.Option(..., "--height", help=""""""),
    image_height: int = typer.Option(..., "--image-height", help=""""""),
    image_width: int = typer.Option(..., "--image-width", help=""""""),
    person_id: str = typer.Option(..., "--person-id", help=""""""),
    width: int = typer.Option(..., "--width", help=""""""),
    x: int = typer.Option(..., "--x", help=""""""),
    y: int = typer.Option(..., "--y", help=""""""),
) -> None:
    """Create a face

    [link=https://api.immich.app/endpoints/faces/createFace]Immich API documentation[/link]
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
    asset_face_create_dto = AssetFaceCreateDto.model_validate(json_data)
    kwargs["asset_face_create_dto"] = asset_face_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.faces, "create_face", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-face", deprecated=False, rich_help_panel="API commands")
def delete_face(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    force: bool = typer.Option(..., "--force", help=""""""),
) -> None:
    """Delete a face

    [link=https://api.immich.app/endpoints/faces/deleteFace]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["force"], force)
    asset_face_delete_dto = AssetFaceDeleteDto.model_validate(json_data)
    kwargs["asset_face_delete_dto"] = asset_face_delete_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.faces, "delete_face", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-faces", deprecated=False, rich_help_panel="API commands")
def get_faces(
    ctx: typer.Context,
    id: str = typer.Option(..., "--id", help=""""""),
) -> None:
    """Retrieve faces for asset

    [link=https://api.immich.app/endpoints/faces/getFaces]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.faces, "get_faces", ctx, **kwargs)
    print_response(result, ctx)


@app.command("reassign-faces-by-id", deprecated=False, rich_help_panel="API commands")
def reassign_faces_by_id(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    body_id: str = typer.Option(..., "--body-id", help=""""""),
) -> None:
    """Re-assign a face to another person

    [link=https://api.immich.app/endpoints/faces/reassignFacesById]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["body_id"], body_id)
    face_dto = FaceDto.model_validate(json_data)
    kwargs["face_dto"] = face_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.faces, "reassign_faces_by_id", ctx, **kwargs)
    print_response(result, ctx)
