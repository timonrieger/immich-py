"""Generated CLI commands for Map tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal

from immich.cli.runtime import print_response, run_command
from immich.client.models import *

app = typer.Typer(
    help="""Map endpoints include supplemental functionality related to geolocation, such as reverse geocoding and retrieving map markers for assets with geolocation data.\n\nDocs: https://api.immich.app/endpoints/map"""
)


@app.command("get-map-markers", deprecated=False)
def get_map_markers(
    ctx: typer.Context,
    file_created_after: datetime | None = typer.Option(
        None, "--file-created-after", help=""""""
    ),
    file_created_before: datetime | None = typer.Option(
        None, "--file-created-before", help=""""""
    ),
    is_archived: Literal["true", "false"] | None = typer.Option(
        None, "--is-archived", help=""""""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=""""""
    ),
    with_partners: Literal["true", "false"] | None = typer.Option(
        None, "--with-partners", help=""""""
    ),
    with_shared_albums: Literal["true", "false"] | None = typer.Option(
        None, "--with-shared-albums", help=""""""
    ),
) -> None:
    """Retrieve map markers

    Docs: https://api.immich.app/endpoints/map/getMapMarkers
    """
    kwargs = {}
    if file_created_after is not None:
        kwargs["file_created_after"] = file_created_after
    if file_created_before is not None:
        kwargs["file_created_before"] = file_created_before
    if is_archived is not None:
        kwargs["is_archived"] = is_archived.lower() == "true"
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite.lower() == "true"
    if with_partners is not None:
        kwargs["with_partners"] = with_partners.lower() == "true"
    if with_shared_albums is not None:
        kwargs["with_shared_albums"] = with_shared_albums.lower() == "true"
    client = ctx.obj["client"]
    result = run_command(client, client.map, "get_map_markers", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("reverse-geocode", deprecated=False)
def reverse_geocode(
    ctx: typer.Context,
    lat: float = typer.Option(..., "--lat", help=""""""),
    lon: float = typer.Option(..., "--lon", help=""""""),
) -> None:
    """Reverse geocode coordinates

    Docs: https://api.immich.app/endpoints/map/reverseGeocode
    """
    kwargs = {}
    kwargs["lat"] = lat
    kwargs["lon"] = lon
    client = ctx.obj["client"]
    result = run_command(client, client.map, "reverse_geocode", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
