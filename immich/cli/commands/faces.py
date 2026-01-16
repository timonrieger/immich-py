"""Generated CLI commands for Faces tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""A face is a detected human face within an asset, which can be associated with a person. Faces are normally detected via machine learning, but can also be created via manually.

Docs: https://api.immich.app/endpoints/faces""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-face")
def create_face(
    ctx: typer.Context,
    asset_id: str = typer.Option(..., "--assetId"),
    height: int = typer.Option(..., "--height"),
    image_height: int = typer.Option(..., "--imageHeight"),
    image_width: int = typer.Option(..., "--imageWidth"),
    person_id: str = typer.Option(..., "--personId"),
    width: int = typer.Option(..., "--width"),
    x: int = typer.Option(..., "--x"),
    y: int = typer.Option(..., "--y"),
) -> None:
    """Create a face

    Docs: https://api.immich.app/endpoints/faces/createFace
    """
    kwargs = {}
    has_flags = any(
        [asset_id, height, image_height, image_width, person_id, width, x, y]
    )
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            asset_id,
            height,
            image_height,
            image_width,
            person_id,
            width,
            x,
            y,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["assetId"], asset_id)
        set_nested(json_data, ["height"], height)
        set_nested(json_data, ["imageHeight"], image_height)
        set_nested(json_data, ["imageWidth"], image_width)
        set_nested(json_data, ["personId"], person_id)
        set_nested(json_data, ["width"], width)
        set_nested(json_data, ["x"], x)
        set_nested(json_data, ["y"], y)
        from immich.client.models.asset_face_create_dto import AssetFaceCreateDto

        asset_face_create_dto = deserialize_request_body(json_data, AssetFaceCreateDto)
        kwargs["asset_face_create_dto"] = asset_face_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.faces, "create_face", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-face")
def delete_face(
    ctx: typer.Context,
    id: str,
    force: bool = typer.Option(..., "--force"),
) -> None:
    """Delete a face

    Docs: https://api.immich.app/endpoints/faces/deleteFace
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([force])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            force,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["force"], force)
        from immich.client.models.asset_face_delete_dto import AssetFaceDeleteDto

        asset_face_delete_dto = deserialize_request_body(json_data, AssetFaceDeleteDto)
        kwargs["asset_face_delete_dto"] = asset_face_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.faces, "delete_face", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-faces")
def get_faces(
    ctx: typer.Context,
    id: str = typer.Option(..., "--id"),
) -> None:
    """Retrieve faces for asset

    Docs: https://api.immich.app/endpoints/faces/getFaces
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.faces, "get_faces", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("reassign-faces-by-id")
def reassign_faces_by_id(
    ctx: typer.Context,
    id: str,
    body_id: str = typer.Option(..., "--id"),
) -> None:
    """Re-assign a face to another person

    Docs: https://api.immich.app/endpoints/faces/reassignFacesById
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([body_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            body_id,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["id"], body_id)
        from immich.client.models.face_dto import FaceDto

        face_dto = deserialize_request_body(json_data, FaceDto)
        kwargs["face_dto"] = face_dto
    client = ctx.obj["client"]
    result = run_command(client, client.faces, "reassign_faces_by_id", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
