"""Generated CLI commands for Map tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command

app = typer.Typer(
    help="""Map endpoints include supplemental functionality related to geolocation, such as reverse geocoding and retrieving map markers for assets with geolocation data.

Docs: https://api.immich.app/endpoints/map""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("get-map-markers")
def get_map_markers(
    ctx: typer.Context,
    file_created_after: str | None = typer.Option(
        None, "--file-created-after", help="""Filter assets created after this date"""
    ),
    file_created_before: str | None = typer.Option(
        None, "--file-created-before", help="""Filter assets created before this date"""
    ),
    is_archived: bool | None = typer.Option(
        None, "--is-archived", help="""Filter by archived status"""
    ),
    is_favorite: bool | None = typer.Option(
        None, "--is-favorite", help="""Filter by favorite status"""
    ),
    with_partners: bool | None = typer.Option(
        None, "--with-partners", help="""Include partner assets"""
    ),
    with_shared_albums: bool | None = typer.Option(
        None, "--with-shared-albums", help="""Include shared album assets"""
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
        kwargs["is_archived"] = is_archived
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite
    if with_partners is not None:
        kwargs["with_partners"] = with_partners
    if with_shared_albums is not None:
        kwargs["with_shared_albums"] = with_shared_albums
    client = ctx.obj["client"]
    api_group = client.map
    result = run_command(client, api_group, "get_map_markers", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("reverse-geocode")
def reverse_geocode(
    ctx: typer.Context,
    lat: float = typer.Option(..., "--lat", help="""Latitude (-90 to 90)"""),
    lon: float = typer.Option(..., "--lon", help="""Longitude (-180 to 180)"""),
) -> None:
    """Reverse geocode coordinates

    Docs: https://api.immich.app/endpoints/map/reverseGeocode
    """
    kwargs = {}
    kwargs["lat"] = lat
    kwargs["lon"] = lon
    client = ctx.obj["client"]
    api_group = client.map
    result = run_command(client, api_group, "reverse_geocode", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
