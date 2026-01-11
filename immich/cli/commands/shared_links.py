"""Generated CLI commands for Shared links tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""A shared link is a public url that provides access to a specific album, asset, or collection of assets. A shared link can be protected with a password, include a specific slug, allow or disallow downloads, and optionally include an expiration date.

Docs: https://api.immich.app/endpoints/shared-links""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("add-shared-link-assets")
def add_shared_link_assets(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    asset_ids: list[str] = typer.Option(..., "--assetIds"),
) -> None:
    """Add assets to a shared link

Docs: https://api.immich.app/endpoints/shared-links/addSharedLinkAssets
    """
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([asset_ids])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_ids_dto import AssetIdsDto
        asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
        kwargs['asset_ids_dto'] = asset_ids_dto
    elif any([
        asset_ids,
    ]):
        # Build body from dotted flags
        json_data = {}
        if asset_ids is None:
            raise SystemExit("Error: --assetIds is required")
        set_nested(json_data, ['assetIds'], asset_ids)
        if json_data:
            from immich.client.models.asset_ids_dto import AssetIdsDto
            asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
            kwargs['asset_ids_dto'] = asset_ids_dto
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'add_shared_link_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("create-shared-link")
def create_shared_link(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    album_id: str | None = typer.Option(None, "--albumId"),
    allow_download: bool | None = typer.Option(None, "--allowDownload"),
    allow_upload: bool | None = typer.Option(None, "--allowUpload"),
    asset_ids: list[str] | None = typer.Option(None, "--assetIds"),
    description: str | None = typer.Option(None, "--description"),
    expires_at: str | None = typer.Option(None, "--expiresAt"),
    password: str | None = typer.Option(None, "--password"),
    show_metadata: bool | None = typer.Option(None, "--showMetadata"),
    slug: str | None = typer.Option(None, "--slug"),
    type: str = typer.Option(..., "--type"),
) -> None:
    """Create a shared link

Docs: https://api.immich.app/endpoints/shared-links/createSharedLink
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([album_id, allow_download, allow_upload, asset_ids, description, expires_at, password, show_metadata, slug, type])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.shared_link_create_dto import SharedLinkCreateDto
        shared_link_create_dto = deserialize_request_body(json_data, SharedLinkCreateDto)
        kwargs['shared_link_create_dto'] = shared_link_create_dto
    elif any([
        album_id,
        allow_download,
        allow_upload,
        asset_ids,
        description,
        expires_at,
        password,
        show_metadata,
        slug,
        type,
    ]):
        # Build body from dotted flags
        json_data = {}
        if album_id is not None:
            set_nested(json_data, ['albumId'], album_id)
        if allow_download is not None:
            set_nested(json_data, ['allowDownload'], allow_download)
        if allow_upload is not None:
            set_nested(json_data, ['allowUpload'], allow_upload)
        if asset_ids is not None:
            set_nested(json_data, ['assetIds'], asset_ids)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if expires_at is not None:
            set_nested(json_data, ['expiresAt'], expires_at)
        if password is not None:
            set_nested(json_data, ['password'], password)
        if show_metadata is not None:
            set_nested(json_data, ['showMetadata'], show_metadata)
        if slug is not None:
            set_nested(json_data, ['slug'], slug)
        if type is None:
            raise SystemExit("Error: --type is required")
        set_nested(json_data, ['type'], type)
        if json_data:
            from immich.client.models.shared_link_create_dto import SharedLinkCreateDto
            shared_link_create_dto = deserialize_request_body(json_data, SharedLinkCreateDto)
            kwargs['shared_link_create_dto'] = shared_link_create_dto
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'create_shared_link', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-shared-links")
def get_all_shared_links(
    ctx: typer.Context,
    album_id: str | None = typer.Option(None, "--album-id"),
    id: str | None = typer.Option(None, "--id"),
) -> None:
    """Retrieve all shared links

Docs: https://api.immich.app/endpoints/shared-links/getAllSharedLinks
    """
    kwargs = {}
    if album_id is not None:
        kwargs['album_id'] = album_id
    if id is not None:
        kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'get_all_shared_links', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-my-shared-link")
def get_my_shared_link(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    password: str | None = typer.Option(None, "--password"),
    slug: str | None = typer.Option(None, "--slug"),
    token: str | None = typer.Option(None, "--token"),
) -> None:
    """Retrieve current shared link

Docs: https://api.immich.app/endpoints/shared-links/getMySharedLink
    """
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if password is not None:
        kwargs['password'] = password
    if slug is not None:
        kwargs['slug'] = slug
    if token is not None:
        kwargs['token'] = token
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'get_my_shared_link', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-shared-link-by-id")
def get_shared_link_by_id(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a shared link

Docs: https://api.immich.app/endpoints/shared-links/getSharedLinkById
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'get_shared_link_by_id', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-shared-link")
def remove_shared_link(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a shared link

Docs: https://api.immich.app/endpoints/shared-links/removeSharedLink
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'remove_shared_link', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-shared-link-assets")
def remove_shared_link_assets(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    asset_ids: list[str] = typer.Option(..., "--assetIds"),
) -> None:
    """Remove assets from a shared link

Docs: https://api.immich.app/endpoints/shared-links/removeSharedLinkAssets
    """
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([asset_ids])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_ids_dto import AssetIdsDto
        asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
        kwargs['asset_ids_dto'] = asset_ids_dto
    elif any([
        asset_ids,
    ]):
        # Build body from dotted flags
        json_data = {}
        if asset_ids is None:
            raise SystemExit("Error: --assetIds is required")
        set_nested(json_data, ['assetIds'], asset_ids)
        if json_data:
            from immich.client.models.asset_ids_dto import AssetIdsDto
            asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
            kwargs['asset_ids_dto'] = asset_ids_dto
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'remove_shared_link_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-shared-link")
def update_shared_link(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    allow_download: bool | None = typer.Option(None, "--allowDownload"),
    allow_upload: bool | None = typer.Option(None, "--allowUpload"),
    change_expiry_time: bool | None = typer.Option(None, "--changeExpiryTime"),
    description: str | None = typer.Option(None, "--description"),
    expires_at: str | None = typer.Option(None, "--expiresAt"),
    password: str | None = typer.Option(None, "--password"),
    show_metadata: bool | None = typer.Option(None, "--showMetadata"),
    slug: str | None = typer.Option(None, "--slug"),
) -> None:
    """Update a shared link

Docs: https://api.immich.app/endpoints/shared-links/updateSharedLink
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([allow_download, allow_upload, change_expiry_time, description, expires_at, password, show_metadata, slug])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.shared_link_edit_dto import SharedLinkEditDto
        shared_link_edit_dto = deserialize_request_body(json_data, SharedLinkEditDto)
        kwargs['shared_link_edit_dto'] = shared_link_edit_dto
    elif any([
        allow_download,
        allow_upload,
        change_expiry_time,
        description,
        expires_at,
        password,
        show_metadata,
        slug,
    ]):
        # Build body from dotted flags
        json_data = {}
        if allow_download is not None:
            set_nested(json_data, ['allowDownload'], allow_download)
        if allow_upload is not None:
            set_nested(json_data, ['allowUpload'], allow_upload)
        if change_expiry_time is not None:
            set_nested(json_data, ['changeExpiryTime'], change_expiry_time)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if expires_at is not None:
            set_nested(json_data, ['expiresAt'], expires_at)
        if password is not None:
            set_nested(json_data, ['password'], password)
        if show_metadata is not None:
            set_nested(json_data, ['showMetadata'], show_metadata)
        if slug is not None:
            set_nested(json_data, ['slug'], slug)
        if json_data:
            from immich.client.models.shared_link_edit_dto import SharedLinkEditDto
            shared_link_edit_dto = deserialize_request_body(json_data, SharedLinkEditDto)
            kwargs['shared_link_edit_dto'] = shared_link_edit_dto
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'update_shared_link', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
