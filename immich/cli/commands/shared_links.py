"""Generated CLI commands for Shared links tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A shared link is a public url that provides access to a specific album, asset, or collection of assets. A shared link can be protected with a password, include a specific slug, allow or disallow downloads, and optionally include an expiration date.\n\n[link=https://api.immich.app/endpoints/shared-links]Immich API documentation[/link]"""
)


@app.command("add-shared-link-assets", deprecated=False, rich_help_panel="API commands")
def add_shared_link_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Add assets to a shared link

    [link=https://api.immich.app/endpoints/shared-links/addSharedLinkAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    set_nested(json_data, ["asset_ids"], asset_ids)
    asset_ids_dto = AssetIdsDto.model_validate(json_data)
    kwargs["asset_ids_dto"] = asset_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "add_shared_link_assets", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("create-shared-link", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/shared-links/createSharedLink]Immich API documentation[/link]
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
    shared_link_create_dto = SharedLinkCreateDto.model_validate(json_data)
    kwargs["shared_link_create_dto"] = shared_link_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "create_shared_link", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-all-shared-links", deprecated=False, rich_help_panel="API commands")
def get_all_shared_links(
    ctx: typer.Context,
    album_id: str | None = typer.Option(None, "--album-id", help=""""""),
) -> None:
    """Retrieve all shared links

    [link=https://api.immich.app/endpoints/shared-links/getAllSharedLinks]Immich API documentation[/link]
    """
    kwargs = {}
    if album_id is not None:
        kwargs["album_id"] = album_id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "get_all_shared_links", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-my-shared-link", deprecated=False, rich_help_panel="API commands")
def get_my_shared_link(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key", help=""""""),
    password: str | None = typer.Option(None, "--password", help="""password"""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
    token: str | None = typer.Option(None, "--token", help=""""""),
) -> None:
    """Retrieve current shared link

    [link=https://api.immich.app/endpoints/shared-links/getMySharedLink]Immich API documentation[/link]
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
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "get_my_shared_link", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-shared-link-by-id", deprecated=False, rich_help_panel="API commands")
def get_shared_link_by_id(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a shared link

    [link=https://api.immich.app/endpoints/shared-links/getSharedLinkById]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "get_shared_link_by_id", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("remove-shared-link", deprecated=False, rich_help_panel="API commands")
def remove_shared_link(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a shared link

    [link=https://api.immich.app/endpoints/shared-links/removeSharedLink]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "remove_shared_link", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "remove-shared-link-assets", deprecated=False, rich_help_panel="API commands"
)
def remove_shared_link_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Remove assets from a shared link

    [link=https://api.immich.app/endpoints/shared-links/removeSharedLinkAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    set_nested(json_data, ["asset_ids"], asset_ids)
    asset_ids_dto = AssetIdsDto.model_validate(json_data)
    kwargs["asset_ids_dto"] = asset_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "remove_shared_link_assets", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("update-shared-link", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/shared-links/updateSharedLink]Immich API documentation[/link]
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
    shared_link_edit_dto = SharedLinkEditDto.model_validate(json_data)
    kwargs["shared_link_edit_dto"] = shared_link_edit_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.shared_links, "update_shared_link", ctx, **kwargs
    )
    print_response(result, ctx)
