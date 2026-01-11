"""Generated CLI commands for Faces tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
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
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    asset_id: str = typer.Option(..., "--assetId", help="""Asset ID"""),
    height: int = typer.Option(..., "--height", help="""Face bounding box height"""),
    image_height: int = typer.Option(
        ..., "--imageHeight", help="""Image height in pixels"""
    ),
    image_width: int = typer.Option(
        ..., "--imageWidth", help="""Image width in pixels"""
    ),
    person_id: str = typer.Option(..., "--personId", help="""Person ID"""),
    width: int = typer.Option(..., "--width", help="""Face bounding box width"""),
    x: int = typer.Option(..., "--x", help="""Face bounding box X coordinate"""),
    y: int = typer.Option(..., "--y", help="""Face bounding box Y coordinate"""),
) -> None:
    """Create a face

    Docs: https://api.immich.app/endpoints/faces/createFace
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any(
        [asset_id, height, image_height, image_width, person_id, width, x, y]
    )
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_face_create_dto import AssetFaceCreateDto

        asset_face_create_dto = deserialize_request_body(json_data, AssetFaceCreateDto)
        kwargs["asset_face_create_dto"] = asset_face_create_dto
    elif any(
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
        # Build body from dotted flags
        json_data = {}
        if asset_id is None:
            raise SystemExit("Error: --assetId is required")
        set_nested(json_data, ["assetId"], asset_id)
        if height is None:
            raise SystemExit("Error: --height is required")
        set_nested(json_data, ["height"], height)
        if image_height is None:
            raise SystemExit("Error: --imageHeight is required")
        set_nested(json_data, ["imageHeight"], image_height)
        if image_width is None:
            raise SystemExit("Error: --imageWidth is required")
        set_nested(json_data, ["imageWidth"], image_width)
        if person_id is None:
            raise SystemExit("Error: --personId is required")
        set_nested(json_data, ["personId"], person_id)
        if width is None:
            raise SystemExit("Error: --width is required")
        set_nested(json_data, ["width"], width)
        if x is None:
            raise SystemExit("Error: --x is required")
        set_nested(json_data, ["x"], x)
        if y is None:
            raise SystemExit("Error: --y is required")
        set_nested(json_data, ["y"], y)
        if json_data:
            from immich.client.models.asset_face_create_dto import AssetFaceCreateDto

            asset_face_create_dto = deserialize_request_body(
                json_data, AssetFaceCreateDto
            )
            kwargs["asset_face_create_dto"] = asset_face_create_dto
    client = ctx.obj["client"]
    api_group = client.faces
    result = run_command(client, api_group, "create_face", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-face")
def delete_face(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Face ID to delete"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    force: bool = typer.Option(
        ..., "--force", help="""Force delete even if person has other faces"""
    ),
) -> None:
    """Delete a face

    Docs: https://api.immich.app/endpoints/faces/deleteFace
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([force])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_face_delete_dto import AssetFaceDeleteDto

        asset_face_delete_dto = deserialize_request_body(json_data, AssetFaceDeleteDto)
        kwargs["asset_face_delete_dto"] = asset_face_delete_dto
    elif any(
        [
            force,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if force is None:
            raise SystemExit("Error: --force is required")
        set_nested(json_data, ["force"], force)
        if json_data:
            from immich.client.models.asset_face_delete_dto import AssetFaceDeleteDto

            asset_face_delete_dto = deserialize_request_body(
                json_data, AssetFaceDeleteDto
            )
            kwargs["asset_face_delete_dto"] = asset_face_delete_dto
    client = ctx.obj["client"]
    api_group = client.faces
    result = run_command(client, api_group, "delete_face", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-faces")
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
    api_group = client.faces
    result = run_command(client, api_group, "get_faces", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("reassign-faces-by-id")
def reassign_faces_by_id(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Person ID to assign the face to"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    body_id: str = typer.Option(..., "--id", help="""Face ID"""),
) -> None:
    """Re-assign a face to another person

    Docs: https://api.immich.app/endpoints/faces/reassignFacesById
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([body_id])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.face_dto import FaceDto

        face_dto = deserialize_request_body(json_data, FaceDto)
        kwargs["face_dto"] = face_dto
    elif any(
        [
            body_id,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if body_id is None:
            raise SystemExit("Error: --id is required")
        set_nested(json_data, ["id"], body_id)
        if json_data:
            from immich.client.models.face_dto import FaceDto

            face_dto = deserialize_request_body(json_data, FaceDto)
            kwargs["face_dto"] = face_dto
    client = ctx.obj["client"]
    api_group = client.faces
    result = run_command(client, api_group, "reassign_faces_by_id", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
