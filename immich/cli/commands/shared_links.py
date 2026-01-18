"""Generated CLI commands for Shared links tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A shared link is a public url that provides access to a specific album, asset, or collection of assets. A shared link can be protected with a password, include a specific slug, allow or disallow downloads, and optionally include an expiration date.\n\nDocs: https://api.immich.app/endpoints/shared-links"""
)


@app.command("add-shared-link-assets", deprecated=False)
def add_shared_link_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Add assets to a shared link

    Docs: https://api.immich.app/endpoints/shared-links/addSharedLinkAssets
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    set_nested(json_data, ["asset_ids"], asset_ids)
    from immich.client.models.asset_ids_dto import AssetIdsDto

    asset_ids_dto = AssetIdsDto.model_validate(json_data)
    kwargs["asset_ids_dto"] = asset_ids_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "add_shared_link_assets", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("create-shared-link", deprecated=False)
def create_shared_link(
    ctx: typer.Context,
    album_id: str | None = typer.Option(None, "--album-id", help=""""""),
    allow_download: Literal["true", "false"] | None = typer.Option(
        None, "--allow-download", help=""""""
    ),
    allow_upload: Literal["true", "false"] | None = typer.Option(
        None, "--allow-upload", help=""""""
    ),
    asset_ids: list[str] | None = typer.Option(None, "--asset-ids", help=""""""),
    description: str | None = typer.Option(None, "--description", help=""""""),
    expires_at: datetime | None = typer.Option(None, "--expires-at", help=""""""),
    password: str | None = typer.Option(None, "--password", help=""""""),
    show_metadata: Literal["true", "false"] | None = typer.Option(
        None, "--show-metadata", help=""""""
    ),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
    type: str = typer.Option(..., "--type", help=""""""),
) -> None:
    """Create a shared link

    Docs: https://api.immich.app/endpoints/shared-links/createSharedLink
    """
    kwargs = {}
    json_data = {}
    if album_id is not None:
        set_nested(json_data, ["album_id"], album_id)
    if allow_download is not None:
        set_nested(json_data, ["allow_download"], allow_download.lower() == "true")
    if allow_upload is not None:
        set_nested(json_data, ["allow_upload"], allow_upload.lower() == "true")
    if asset_ids is not None:
        set_nested(json_data, ["asset_ids"], asset_ids)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if expires_at is not None:
        set_nested(json_data, ["expires_at"], expires_at)
    if password is not None:
        set_nested(json_data, ["password"], password)
    if show_metadata is not None:
        set_nested(json_data, ["show_metadata"], show_metadata.lower() == "true")
    if slug is not None:
        set_nested(json_data, ["slug"], slug)
    set_nested(json_data, ["type"], type)
    from immich.client.models.shared_link_create_dto import SharedLinkCreateDto

    shared_link_create_dto = SharedLinkCreateDto.model_validate(json_data)
    kwargs["shared_link_create_dto"] = shared_link_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.shared_links, "create_shared_link", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-all-shared-links", deprecated=False)
def get_all_shared_links(
    ctx: typer.Context,
    album_id: str | None = typer.Option(None, "--album-id", help=""""""),
) -> None:
    """Retrieve all shared links

    Docs: https://api.immich.app/endpoints/shared-links/getAllSharedLinks
    """
    kwargs = {}
    if album_id is not None:
        kwargs["album_id"] = album_id
    client = ctx.obj["client"]
    result = run_command(client, client.shared_links, "get_all_shared_links", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-my-shared-link", deprecated=False)
def get_my_shared_link(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key", help=""""""),
    password: str | None = typer.Option(None, "--password", help="""password"""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
    token: str | None = typer.Option(None, "--token", help=""""""),
) -> None:
    """Retrieve current shared link

    Docs: https://api.immich.app/endpoints/shared-links/getMySharedLink
    """
    kwargs = {}
    if key is not None:
        kwargs["key"] = key
    if password is not None:
        kwargs["password"] = password
    if slug is not None:
        kwargs["slug"] = slug
    if token is not None:
        kwargs["token"] = token
    client = ctx.obj["client"]
    result = run_command(client, client.shared_links, "get_my_shared_link", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-shared-link-by-id", deprecated=False)
def get_shared_link_by_id(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a shared link

    Docs: https://api.immich.app/endpoints/shared-links/getSharedLinkById
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.shared_links, "get_shared_link_by_id", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("remove-shared-link", deprecated=False)
def remove_shared_link(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a shared link

    Docs: https://api.immich.app/endpoints/shared-links/removeSharedLink
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.shared_links, "remove_shared_link", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("remove-shared-link-assets", deprecated=False)
def remove_shared_link_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Remove assets from a shared link

    Docs: https://api.immich.app/endpoints/shared-links/removeSharedLinkAssets
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    set_nested(json_data, ["asset_ids"], asset_ids)
    from immich.client.models.asset_ids_dto import AssetIdsDto

    asset_ids_dto = AssetIdsDto.model_validate(json_data)
    kwargs["asset_ids_dto"] = asset_ids_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "remove_shared_link_assets", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-shared-link", deprecated=False)
def update_shared_link(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    allow_download: Literal["true", "false"] | None = typer.Option(
        None, "--allow-download", help=""""""
    ),
    allow_upload: Literal["true", "false"] | None = typer.Option(
        None, "--allow-upload", help=""""""
    ),
    change_expiry_time: Literal["true", "false"] | None = typer.Option(
        None,
        "--change-expiry-time",
        help="""Few clients cannot send null to set the expiryTime to never.
Setting this flag and not sending expiryAt is considered as null instead.
Clients that can send null values can ignore this.""",
    ),
    description: str | None = typer.Option(None, "--description", help=""""""),
    expires_at: datetime | None = typer.Option(None, "--expires-at", help=""""""),
    password: str | None = typer.Option(None, "--password", help=""""""),
    show_metadata: Literal["true", "false"] | None = typer.Option(
        None, "--show-metadata", help=""""""
    ),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Update a shared link

    Docs: https://api.immich.app/endpoints/shared-links/updateSharedLink
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if allow_download is not None:
        set_nested(json_data, ["allow_download"], allow_download.lower() == "true")
    if allow_upload is not None:
        set_nested(json_data, ["allow_upload"], allow_upload.lower() == "true")
    if change_expiry_time is not None:
        set_nested(
            json_data, ["change_expiry_time"], change_expiry_time.lower() == "true"
        )
    if description is not None:
        set_nested(json_data, ["description"], description)
    if expires_at is not None:
        set_nested(json_data, ["expires_at"], expires_at)
    if password is not None:
        set_nested(json_data, ["password"], password)
    if show_metadata is not None:
        set_nested(json_data, ["show_metadata"], show_metadata.lower() == "true")
    if slug is not None:
        set_nested(json_data, ["slug"], slug)
    from immich.client.models.shared_link_edit_dto import SharedLinkEditDto

    shared_link_edit_dto = SharedLinkEditDto.model_validate(json_data)
    kwargs["shared_link_edit_dto"] = shared_link_edit_dto
    client = ctx.obj["client"]
    result = run_command(client, client.shared_links, "update_shared_link", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
