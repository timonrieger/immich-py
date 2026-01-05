"""Generated CLI commands for Search tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Search operations")

@app.command("get-assets-by-city")
def get_assets_by_city(
    ctx: typer.Context,
) -> None:
    """Retrieve assets by city"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'get_assets_by_city', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-explore-data")
def get_explore_data(
    ctx: typer.Context,
) -> None:
    """Retrieve explore data"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'get_explore_data', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-search-suggestions")
def get_search_suggestions(
    country: str | None = typer.Option(None, "--country"),
    include_null: bool | None = typer.Option(None, "--include-null"),
    lens_model: str | None = typer.Option(None, "--lens-model"),
    make: str | None = typer.Option(None, "--make"),
    model: str | None = typer.Option(None, "--model"),
    state: str | None = typer.Option(None, "--state"),
    type: SearchSuggestionType = typer.Option(..., "--type"),
    ctx: typer.Context,
) -> None:
    """Retrieve search suggestions"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if country is not None:
        kwargs['country'] = country
    if include_null is not None:
        kwargs['include_null'] = include_null
    if lens_model is not None:
        kwargs['lens_model'] = lens_model
    if make is not None:
        kwargs['make'] = make
    if model is not None:
        kwargs['model'] = model
    if state is not None:
        kwargs['state'] = state
    kwargs['type'] = type
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'get_search_suggestions', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-asset-statistics")
def search_asset_statistics(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Search asset statistics"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.statistics_search_dto import StatisticsSearchDto
        statistics_search_dto = deserialize_request_body(json_data, StatisticsSearchDto)
        kwargs['statistics_search_dto'] = statistics_search_dto
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'search_asset_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-assets")
def search_assets(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Search assets by metadata"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.metadata_search_dto import MetadataSearchDto
        metadata_search_dto = deserialize_request_body(json_data, MetadataSearchDto)
        kwargs['metadata_search_dto'] = metadata_search_dto
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'search_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-large-assets")
def search_large_assets(
    album_ids: list[str] | None = typer.Option(None, "--album-ids"),
    city: str | None = typer.Option(None, "--city"),
    country: str | None = typer.Option(None, "--country"),
    created_after: str | None = typer.Option(None, "--created-after"),
    created_before: str | None = typer.Option(None, "--created-before"),
    device_id: str | None = typer.Option(None, "--device-id"),
    is_encoded: bool | None = typer.Option(None, "--is-encoded"),
    is_favorite: bool | None = typer.Option(None, "--is-favorite"),
    is_motion: bool | None = typer.Option(None, "--is-motion"),
    is_not_in_album: bool | None = typer.Option(None, "--is-not-in-album"),
    is_offline: bool | None = typer.Option(None, "--is-offline"),
    lens_model: str | None = typer.Option(None, "--lens-model"),
    library_id: str | None = typer.Option(None, "--library-id"),
    make: str | None = typer.Option(None, "--make"),
    min_file_size: int | None = typer.Option(None, "--min-file-size"),
    model: str | None = typer.Option(None, "--model"),
    ocr: str | None = typer.Option(None, "--ocr"),
    person_ids: list[str] | None = typer.Option(None, "--person-ids"),
    rating: float | None = typer.Option(None, "--rating"),
    size: float | None = typer.Option(None, "--size"),
    state: str | None = typer.Option(None, "--state"),
    tag_ids: list[str] | None = typer.Option(None, "--tag-ids"),
    taken_after: str | None = typer.Option(None, "--taken-after"),
    taken_before: str | None = typer.Option(None, "--taken-before"),
    trashed_after: str | None = typer.Option(None, "--trashed-after"),
    trashed_before: str | None = typer.Option(None, "--trashed-before"),
    type: AssetTypeEnum | None = typer.Option(None, "--type"),
    updated_after: str | None = typer.Option(None, "--updated-after"),
    updated_before: str | None = typer.Option(None, "--updated-before"),
    visibility: AssetVisibility | None = typer.Option(None, "--visibility"),
    with_deleted: bool | None = typer.Option(None, "--with-deleted"),
    with_exif: bool | None = typer.Option(None, "--with-exif"),
    ctx: typer.Context,
) -> None:
    """Search large assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if album_ids is not None:
        kwargs['album_ids'] = album_ids
    if city is not None:
        kwargs['city'] = city
    if country is not None:
        kwargs['country'] = country
    if created_after is not None:
        kwargs['created_after'] = created_after
    if created_before is not None:
        kwargs['created_before'] = created_before
    if device_id is not None:
        kwargs['device_id'] = device_id
    if is_encoded is not None:
        kwargs['is_encoded'] = is_encoded
    if is_favorite is not None:
        kwargs['is_favorite'] = is_favorite
    if is_motion is not None:
        kwargs['is_motion'] = is_motion
    if is_not_in_album is not None:
        kwargs['is_not_in_album'] = is_not_in_album
    if is_offline is not None:
        kwargs['is_offline'] = is_offline
    if lens_model is not None:
        kwargs['lens_model'] = lens_model
    if library_id is not None:
        kwargs['library_id'] = library_id
    if make is not None:
        kwargs['make'] = make
    if min_file_size is not None:
        kwargs['min_file_size'] = min_file_size
    if model is not None:
        kwargs['model'] = model
    if ocr is not None:
        kwargs['ocr'] = ocr
    if person_ids is not None:
        kwargs['person_ids'] = person_ids
    if rating is not None:
        kwargs['rating'] = rating
    if size is not None:
        kwargs['size'] = size
    if state is not None:
        kwargs['state'] = state
    if tag_ids is not None:
        kwargs['tag_ids'] = tag_ids
    if taken_after is not None:
        kwargs['taken_after'] = taken_after
    if taken_before is not None:
        kwargs['taken_before'] = taken_before
    if trashed_after is not None:
        kwargs['trashed_after'] = trashed_after
    if trashed_before is not None:
        kwargs['trashed_before'] = trashed_before
    if type is not None:
        kwargs['type'] = type
    if updated_after is not None:
        kwargs['updated_after'] = updated_after
    if updated_before is not None:
        kwargs['updated_before'] = updated_before
    if visibility is not None:
        kwargs['visibility'] = visibility
    if with_deleted is not None:
        kwargs['with_deleted'] = with_deleted
    if with_exif is not None:
        kwargs['with_exif'] = with_exif
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'search_large_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-person")
def search_person(
    name: str = typer.Option(..., "--name"),
    with_hidden: bool | None = typer.Option(None, "--with-hidden"),
    ctx: typer.Context,
) -> None:
    """Search people"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['name'] = name
    if with_hidden is not None:
        kwargs['with_hidden'] = with_hidden
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'search_person', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-places")
def search_places(
    name: str = typer.Option(..., "--name"),
    ctx: typer.Context,
) -> None:
    """Search places"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['name'] = name
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'search_places', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-random")
def search_random(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Search random assets"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.random_search_dto import RandomSearchDto
        random_search_dto = deserialize_request_body(json_data, RandomSearchDto)
        kwargs['random_search_dto'] = random_search_dto
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'search_random', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-smart")
def search_smart(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Smart asset search"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.smart_search_dto import SmartSearchDto
        smart_search_dto = deserialize_request_body(json_data, SmartSearchDto)
        kwargs['smart_search_dto'] = smart_search_dto
    client = ctx.obj['client']
    api_group = client.search
    result = run_command(client, api_group, 'search_smart', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
