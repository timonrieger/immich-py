"""Generated CLI commands for Map tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Map endpoints include supplemental functionality related to geolocation, such as reverse geocoding and retrieving map markers for assets with geolocation data.. https://api.immich.app/endpoints/map', context_settings={'help_option_names': ['-h', '--help']})

@app.command("get-map-markers")
def get_map_markers(
    ctx: typer.Context,
    file_created_after: str | None = typer.Option(None, "--file-created-after"),
    file_created_before: str | None = typer.Option(None, "--file-created-before"),
    is_archived: bool | None = typer.Option(None, "--is-archived"),
    is_favorite: bool | None = typer.Option(None, "--is-favorite"),
    with_partners: bool | None = typer.Option(None, "--with-partners"),
    with_shared_albums: bool | None = typer.Option(None, "--with-shared-albums"),
) -> None:
    """Retrieve map markers"""
    kwargs = {}
    if file_created_after is not None:
        kwargs['file_created_after'] = file_created_after
    if file_created_before is not None:
        kwargs['file_created_before'] = file_created_before
    if is_archived is not None:
        kwargs['is_archived'] = is_archived
    if is_favorite is not None:
        kwargs['is_favorite'] = is_favorite
    if with_partners is not None:
        kwargs['with_partners'] = with_partners
    if with_shared_albums is not None:
        kwargs['with_shared_albums'] = with_shared_albums
    client = ctx.obj['client']
    api_group = client.map
    result = run_command(client, api_group, 'get_map_markers', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("reverse-geocode")
def reverse_geocode(
    ctx: typer.Context,
    lat: float = typer.Option(..., "--lat"),
    lon: float = typer.Option(..., "--lon"),
) -> None:
    """Reverse geocode coordinates"""
    kwargs = {}
    kwargs['lat'] = lat
    kwargs['lon'] = lon
    client = ctx.obj['client']
    api_group = client.map
    result = run_command(client, api_group, 'reverse_geocode', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
