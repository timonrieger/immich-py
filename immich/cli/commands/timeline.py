"""Generated CLI commands for Timeline tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command

app = typer.Typer(
    help="""Specialized endpoints related to the timeline implementation used in the web application. External applications or tools should not use or rely on these endpoints, as they are subject to change without notice.

Docs: https://api.immich.app/endpoints/timeline""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("get-time-bucket")
def get_time_bucket(
    ctx: typer.Context,
    album_id: str | None = typer.Option(
        None, "--album-id", help="""Filter assets belonging to a specific album"""
    ),
    is_favorite: bool | None = typer.Option(
        None,
        "--is-favorite",
        help="""Filter by favorite status (true for favorites only, false for non-favorites only)""",
    ),
    is_trashed: bool | None = typer.Option(
        None,
        "--is-trashed",
        help="""Filter by trash status (true for trashed assets only, false for non-trashed only)""",
    ),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    order: str | None = typer.Option(
        None,
        "--order",
        help="""Sort order for assets within time buckets (ASC for oldest first, DESC for newest first)""",
    ),
    person_id: str | None = typer.Option(
        None,
        "--person-id",
        help="""Filter assets containing a specific person (face recognition)""",
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
    tag_id: str | None = typer.Option(
        None, "--tag-id", help="""Filter assets with a specific tag"""
    ),
    time_bucket: str = typer.Option(
        ...,
        "--time-bucket",
        help="""Time bucket identifier in YYYY-MM-DD format (e.g., "2024-01-01" for January 2024)""",
    ),
    user_id: str | None = typer.Option(
        None, "--user-id", help="""Filter assets by specific user ID"""
    ),
    visibility: str | None = typer.Option(
        None,
        "--visibility",
        help="""Filter by asset visibility status (ARCHIVE, TIMELINE, HIDDEN, LOCKED)""",
    ),
    with_coordinates: bool | None = typer.Option(
        None, "--with-coordinates", help="""Include location data in the response"""
    ),
    with_partners: bool | None = typer.Option(
        None, "--with-partners", help="""Include assets shared by partners"""
    ),
    with_stacked: bool | None = typer.Option(
        None,
        "--with-stacked",
        help="""Include stacked assets in the response. When true, only primary assets from stacks are returned.""",
    ),
) -> None:
    """Get time bucket

    Docs: https://api.immich.app/endpoints/timeline/getTimeBucket
    """
    kwargs = {}
    if album_id is not None:
        kwargs["album_id"] = album_id
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed
    if key is not None:
        kwargs["key"] = key
    if order is not None:
        kwargs["order"] = order
    if person_id is not None:
        kwargs["person_id"] = person_id
    if slug is not None:
        kwargs["slug"] = slug
    if tag_id is not None:
        kwargs["tag_id"] = tag_id
    kwargs["time_bucket"] = time_bucket
    if user_id is not None:
        kwargs["user_id"] = user_id
    if visibility is not None:
        kwargs["visibility"] = visibility
    if with_coordinates is not None:
        kwargs["with_coordinates"] = with_coordinates
    if with_partners is not None:
        kwargs["with_partners"] = with_partners
    if with_stacked is not None:
        kwargs["with_stacked"] = with_stacked
    client = ctx.obj["client"]
    api_group = client.timeline
    result = run_command(client, api_group, "get_time_bucket", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-time-buckets")
def get_time_buckets(
    ctx: typer.Context,
    album_id: str | None = typer.Option(
        None, "--album-id", help="""Filter assets belonging to a specific album"""
    ),
    is_favorite: bool | None = typer.Option(
        None,
        "--is-favorite",
        help="""Filter by favorite status (true for favorites only, false for non-favorites only)""",
    ),
    is_trashed: bool | None = typer.Option(
        None,
        "--is-trashed",
        help="""Filter by trash status (true for trashed assets only, false for non-trashed only)""",
    ),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    order: str | None = typer.Option(
        None,
        "--order",
        help="""Sort order for assets within time buckets (ASC for oldest first, DESC for newest first)""",
    ),
    person_id: str | None = typer.Option(
        None,
        "--person-id",
        help="""Filter assets containing a specific person (face recognition)""",
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
    tag_id: str | None = typer.Option(
        None, "--tag-id", help="""Filter assets with a specific tag"""
    ),
    user_id: str | None = typer.Option(
        None, "--user-id", help="""Filter assets by specific user ID"""
    ),
    visibility: str | None = typer.Option(
        None,
        "--visibility",
        help="""Filter by asset visibility status (ARCHIVE, TIMELINE, HIDDEN, LOCKED)""",
    ),
    with_coordinates: bool | None = typer.Option(
        None, "--with-coordinates", help="""Include location data in the response"""
    ),
    with_partners: bool | None = typer.Option(
        None, "--with-partners", help="""Include assets shared by partners"""
    ),
    with_stacked: bool | None = typer.Option(
        None,
        "--with-stacked",
        help="""Include stacked assets in the response. When true, only primary assets from stacks are returned.""",
    ),
) -> None:
    """Get time buckets

    Docs: https://api.immich.app/endpoints/timeline/getTimeBuckets
    """
    kwargs = {}
    if album_id is not None:
        kwargs["album_id"] = album_id
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed
    if key is not None:
        kwargs["key"] = key
    if order is not None:
        kwargs["order"] = order
    if person_id is not None:
        kwargs["person_id"] = person_id
    if slug is not None:
        kwargs["slug"] = slug
    if tag_id is not None:
        kwargs["tag_id"] = tag_id
    if user_id is not None:
        kwargs["user_id"] = user_id
    if visibility is not None:
        kwargs["visibility"] = visibility
    if with_coordinates is not None:
        kwargs["with_coordinates"] = with_coordinates
    if with_partners is not None:
        kwargs["with_partners"] = with_partners
    if with_stacked is not None:
        kwargs["with_stacked"] = with_stacked
    client = ctx.obj["client"]
    api_group = client.timeline
    result = run_command(client, api_group, "get_time_buckets", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
