"""Generated CLI commands for Timeline tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Timeline operations")

@app.command("get-time-bucket")
def get_time_bucket(
    ctx: typer.Context,
    album_id: str | None = typer.Option(None, "--album-id"),
    is_favorite: bool | None = typer.Option(None, "--is-favorite"),
    is_trashed: bool | None = typer.Option(None, "--is-trashed"),
    key: str | None = typer.Option(None, "--key"),
    order: str | None = typer.Option(None, "--order"),
    person_id: str | None = typer.Option(None, "--person-id"),
    slug: str | None = typer.Option(None, "--slug"),
    tag_id: str | None = typer.Option(None, "--tag-id"),
    time_bucket: str = typer.Option(..., "--time-bucket"),
    user_id: str | None = typer.Option(None, "--user-id"),
    visibility: str | None = typer.Option(None, "--visibility"),
    with_coordinates: bool | None = typer.Option(None, "--with-coordinates"),
    with_partners: bool | None = typer.Option(None, "--with-partners"),
    with_stacked: bool | None = typer.Option(None, "--with-stacked"),
) -> None:
    """Get time bucket"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if album_id is not None:
        kwargs['album_id'] = album_id
    if is_favorite is not None:
        kwargs['is_favorite'] = is_favorite
    if is_trashed is not None:
        kwargs['is_trashed'] = is_trashed
    if key is not None:
        kwargs['key'] = key
    if order is not None:
        kwargs['order'] = order
    if person_id is not None:
        kwargs['person_id'] = person_id
    if slug is not None:
        kwargs['slug'] = slug
    if tag_id is not None:
        kwargs['tag_id'] = tag_id
    kwargs['time_bucket'] = time_bucket
    if user_id is not None:
        kwargs['user_id'] = user_id
    if visibility is not None:
        kwargs['visibility'] = visibility
    if with_coordinates is not None:
        kwargs['with_coordinates'] = with_coordinates
    if with_partners is not None:
        kwargs['with_partners'] = with_partners
    if with_stacked is not None:
        kwargs['with_stacked'] = with_stacked
    client = ctx.obj['client']
    api_group = client.timeline
    result = run_command(client, api_group, 'get_time_bucket', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-time-buckets")
def get_time_buckets(
    ctx: typer.Context,
    album_id: str | None = typer.Option(None, "--album-id"),
    is_favorite: bool | None = typer.Option(None, "--is-favorite"),
    is_trashed: bool | None = typer.Option(None, "--is-trashed"),
    key: str | None = typer.Option(None, "--key"),
    order: str | None = typer.Option(None, "--order"),
    person_id: str | None = typer.Option(None, "--person-id"),
    slug: str | None = typer.Option(None, "--slug"),
    tag_id: str | None = typer.Option(None, "--tag-id"),
    user_id: str | None = typer.Option(None, "--user-id"),
    visibility: str | None = typer.Option(None, "--visibility"),
    with_coordinates: bool | None = typer.Option(None, "--with-coordinates"),
    with_partners: bool | None = typer.Option(None, "--with-partners"),
    with_stacked: bool | None = typer.Option(None, "--with-stacked"),
) -> None:
    """Get time buckets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if album_id is not None:
        kwargs['album_id'] = album_id
    if is_favorite is not None:
        kwargs['is_favorite'] = is_favorite
    if is_trashed is not None:
        kwargs['is_trashed'] = is_trashed
    if key is not None:
        kwargs['key'] = key
    if order is not None:
        kwargs['order'] = order
    if person_id is not None:
        kwargs['person_id'] = person_id
    if slug is not None:
        kwargs['slug'] = slug
    if tag_id is not None:
        kwargs['tag_id'] = tag_id
    if user_id is not None:
        kwargs['user_id'] = user_id
    if visibility is not None:
        kwargs['visibility'] = visibility
    if with_coordinates is not None:
        kwargs['with_coordinates'] = with_coordinates
    if with_partners is not None:
        kwargs['with_partners'] = with_partners
    if with_stacked is not None:
        kwargs['with_stacked'] = with_stacked
    client = ctx.obj['client']
    api_group = client.timeline
    result = run_command(client, api_group, 'get_time_buckets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
