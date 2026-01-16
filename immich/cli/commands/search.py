"""Generated CLI commands for Search tag (auto-generated, do not edit)."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, parse_complex_list, print_response, run_command, set_nested

app = typer.Typer(help="""Endpoints related to searching assets via text, smart search, optical character recognition (OCR), and other filters like person, album, and other metadata. Search endpoints usually support pagination and sorting.

Docs: https://api.immich.app/endpoints/search""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("get-assets-by-city")
def get_assets_by_city(
    ctx: typer.Context,
) -> None:
    """Retrieve assets by city

Docs: https://api.immich.app/endpoints/search/getAssetsByCity
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.search, 'get_assets_by_city', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-explore-data")
def get_explore_data(
    ctx: typer.Context,
) -> None:
    """Retrieve explore data

Docs: https://api.immich.app/endpoints/search/getExploreData
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.search, 'get_explore_data', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-search-suggestions")
def get_search_suggestions(
    ctx: typer.Context,
    country: str | None = typer.Option(None, "--country"),
    include_null: str | None = typer.Option(None, "--include-null"),
    lens_model: str | None = typer.Option(None, "--lens-model"),
    make: str | None = typer.Option(None, "--make"),
    model: str | None = typer.Option(None, "--model"),
    state: str | None = typer.Option(None, "--state"),
    type: str = typer.Option(..., "--type"),
) -> None:
    """Retrieve search suggestions

Docs: https://api.immich.app/endpoints/search/getSearchSuggestions
    """
    kwargs = {}
    if country is not None:
        kwargs['country'] = country
    if include_null is not None:
        kwargs['include_null'] = include_null.lower() == 'true'
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
    result = run_command(client, client.search, 'get_search_suggestions', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-asset-statistics")
def search_asset_statistics(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(None, "--albumIds"),
    city: str | None = typer.Option(None, "--city"),
    country: str | None = typer.Option(None, "--country"),
    created_after: datetime | None = typer.Option(None, "--createdAfter"),
    created_before: datetime | None = typer.Option(None, "--createdBefore"),
    description: str | None = typer.Option(None, "--description"),
    device_id: str | None = typer.Option(None, "--deviceId"),
    is_encoded: bool | None = typer.Option(None, "--isEncoded"),
    is_favorite: bool | None = typer.Option(None, "--isFavorite"),
    is_motion: bool | None = typer.Option(None, "--isMotion"),
    is_not_in_album: bool | None = typer.Option(None, "--isNotInAlbum"),
    is_offline: bool | None = typer.Option(None, "--isOffline"),
    lens_model: str | None = typer.Option(None, "--lensModel"),
    library_id: str | None = typer.Option(None, "--libraryId"),
    make: str | None = typer.Option(None, "--make"),
    model: str | None = typer.Option(None, "--model"),
    ocr: str | None = typer.Option(None, "--ocr"),
    person_ids: list[str] | None = typer.Option(None, "--personIds"),
    rating: float | None = typer.Option(None, "--rating"),
    state: str | None = typer.Option(None, "--state"),
    tag_ids: list[str] | None = typer.Option(None, "--tagIds"),
    taken_after: datetime | None = typer.Option(None, "--takenAfter"),
    taken_before: datetime | None = typer.Option(None, "--takenBefore"),
    trashed_after: datetime | None = typer.Option(None, "--trashedAfter"),
    trashed_before: datetime | None = typer.Option(None, "--trashedBefore"),
    type: str | None = typer.Option(None, "--type"),
    updated_after: datetime | None = typer.Option(None, "--updatedAfter"),
    updated_before: datetime | None = typer.Option(None, "--updatedBefore"),
    visibility: str | None = typer.Option(None, "--visibility"),
) -> None:
    """Search asset statistics

Docs: https://api.immich.app/endpoints/search/searchAssetStatistics
    """
    kwargs = {}
    has_flags = any([album_ids, city, country, created_after, created_before, description, device_id, is_encoded, is_favorite, is_motion, is_not_in_album, is_offline, lens_model, library_id, make, model, ocr, person_ids, rating, state, tag_ids, taken_after, taken_before, trashed_after, trashed_before, type, updated_after, updated_before, visibility])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([album_ids, city, country, created_after, created_before, description, device_id, is_encoded, is_favorite, is_motion, is_not_in_album, is_offline, lens_model, library_id, make, model, ocr, person_ids, rating, state, tag_ids, taken_after, taken_before, trashed_after, trashed_before, type, updated_after, updated_before, visibility]):
        json_data = {}
        if album_ids is not None:
            set_nested(json_data, ['albumIds'], album_ids)
        if city is not None:
            set_nested(json_data, ['city'], city)
        if country is not None:
            set_nested(json_data, ['country'], country)
        if created_after is not None:
            set_nested(json_data, ['createdAfter'], created_after)
        if created_before is not None:
            set_nested(json_data, ['createdBefore'], created_before)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if device_id is not None:
            set_nested(json_data, ['deviceId'], device_id)
        if is_encoded is not None:
            set_nested(json_data, ['isEncoded'], is_encoded)
        if is_favorite is not None:
            set_nested(json_data, ['isFavorite'], is_favorite)
        if is_motion is not None:
            set_nested(json_data, ['isMotion'], is_motion)
        if is_not_in_album is not None:
            set_nested(json_data, ['isNotInAlbum'], is_not_in_album)
        if is_offline is not None:
            set_nested(json_data, ['isOffline'], is_offline)
        if lens_model is not None:
            set_nested(json_data, ['lensModel'], lens_model)
        if library_id is not None:
            set_nested(json_data, ['libraryId'], library_id)
        if make is not None:
            set_nested(json_data, ['make'], make)
        if model is not None:
            set_nested(json_data, ['model'], model)
        if ocr is not None:
            set_nested(json_data, ['ocr'], ocr)
        if person_ids is not None:
            set_nested(json_data, ['personIds'], person_ids)
        if rating is not None:
            set_nested(json_data, ['rating'], rating)
        if state is not None:
            set_nested(json_data, ['state'], state)
        if tag_ids is not None:
            set_nested(json_data, ['tagIds'], tag_ids)
        if taken_after is not None:
            set_nested(json_data, ['takenAfter'], taken_after)
        if taken_before is not None:
            set_nested(json_data, ['takenBefore'], taken_before)
        if trashed_after is not None:
            set_nested(json_data, ['trashedAfter'], trashed_after)
        if trashed_before is not None:
            set_nested(json_data, ['trashedBefore'], trashed_before)
        if type is not None:
            set_nested(json_data, ['type'], type)
        if updated_after is not None:
            set_nested(json_data, ['updatedAfter'], updated_after)
        if updated_before is not None:
            set_nested(json_data, ['updatedBefore'], updated_before)
        if visibility is not None:
            set_nested(json_data, ['visibility'], visibility)
        from immich.client.models.statistics_search_dto import StatisticsSearchDto
        statistics_search_dto = deserialize_request_body(json_data, StatisticsSearchDto)
        kwargs['statistics_search_dto'] = statistics_search_dto
    client = ctx.obj['client']
    result = run_command(client, client.search, 'search_asset_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-assets")
def search_assets(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(None, "--albumIds"),
    checksum: str | None = typer.Option(None, "--checksum"),
    city: str | None = typer.Option(None, "--city"),
    country: str | None = typer.Option(None, "--country"),
    created_after: datetime | None = typer.Option(None, "--createdAfter"),
    created_before: datetime | None = typer.Option(None, "--createdBefore"),
    description: str | None = typer.Option(None, "--description"),
    device_asset_id: str | None = typer.Option(None, "--deviceAssetId"),
    device_id: str | None = typer.Option(None, "--deviceId"),
    encoded_video_path: str | None = typer.Option(None, "--encodedVideoPath"),
    id: str | None = typer.Option(None, "--id"),
    is_encoded: bool | None = typer.Option(None, "--isEncoded"),
    is_favorite: bool | None = typer.Option(None, "--isFavorite"),
    is_motion: bool | None = typer.Option(None, "--isMotion"),
    is_not_in_album: bool | None = typer.Option(None, "--isNotInAlbum"),
    is_offline: bool | None = typer.Option(None, "--isOffline"),
    lens_model: str | None = typer.Option(None, "--lensModel"),
    library_id: str | None = typer.Option(None, "--libraryId"),
    make: str | None = typer.Option(None, "--make"),
    model: str | None = typer.Option(None, "--model"),
    ocr: str | None = typer.Option(None, "--ocr"),
    order: str | None = typer.Option(None, "--order"),
    original_file_name: str | None = typer.Option(None, "--originalFileName"),
    original_path: str | None = typer.Option(None, "--originalPath"),
    page: float | None = typer.Option(None, "--page"),
    person_ids: list[str] | None = typer.Option(None, "--personIds"),
    preview_path: str | None = typer.Option(None, "--previewPath"),
    rating: float | None = typer.Option(None, "--rating"),
    size: float | None = typer.Option(None, "--size"),
    state: str | None = typer.Option(None, "--state"),
    tag_ids: list[str] | None = typer.Option(None, "--tagIds"),
    taken_after: datetime | None = typer.Option(None, "--takenAfter"),
    taken_before: datetime | None = typer.Option(None, "--takenBefore"),
    thumbnail_path: str | None = typer.Option(None, "--thumbnailPath"),
    trashed_after: datetime | None = typer.Option(None, "--trashedAfter"),
    trashed_before: datetime | None = typer.Option(None, "--trashedBefore"),
    type: str | None = typer.Option(None, "--type"),
    updated_after: datetime | None = typer.Option(None, "--updatedAfter"),
    updated_before: datetime | None = typer.Option(None, "--updatedBefore"),
    visibility: str | None = typer.Option(None, "--visibility"),
    with_deleted: bool | None = typer.Option(None, "--withDeleted"),
    with_exif: bool | None = typer.Option(None, "--withExif"),
    with_people: bool | None = typer.Option(None, "--withPeople"),
    with_stacked: bool | None = typer.Option(None, "--withStacked"),
) -> None:
    """Search assets by metadata

Docs: https://api.immich.app/endpoints/search/searchAssets
    """
    kwargs = {}
    has_flags = any([album_ids, checksum, city, country, created_after, created_before, description, device_asset_id, device_id, encoded_video_path, id, is_encoded, is_favorite, is_motion, is_not_in_album, is_offline, lens_model, library_id, make, model, ocr, order, original_file_name, original_path, page, person_ids, preview_path, rating, size, state, tag_ids, taken_after, taken_before, thumbnail_path, trashed_after, trashed_before, type, updated_after, updated_before, visibility, with_deleted, with_exif, with_people, with_stacked])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([album_ids, checksum, city, country, created_after, created_before, description, device_asset_id, device_id, encoded_video_path, id, is_encoded, is_favorite, is_motion, is_not_in_album, is_offline, lens_model, library_id, make, model, ocr, order, original_file_name, original_path, page, person_ids, preview_path, rating, size, state, tag_ids, taken_after, taken_before, thumbnail_path, trashed_after, trashed_before, type, updated_after, updated_before, visibility, with_deleted, with_exif, with_people, with_stacked]):
        json_data = {}
        if album_ids is not None:
            set_nested(json_data, ['albumIds'], album_ids)
        if checksum is not None:
            set_nested(json_data, ['checksum'], checksum)
        if city is not None:
            set_nested(json_data, ['city'], city)
        if country is not None:
            set_nested(json_data, ['country'], country)
        if created_after is not None:
            set_nested(json_data, ['createdAfter'], created_after)
        if created_before is not None:
            set_nested(json_data, ['createdBefore'], created_before)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if device_asset_id is not None:
            set_nested(json_data, ['deviceAssetId'], device_asset_id)
        if device_id is not None:
            set_nested(json_data, ['deviceId'], device_id)
        if encoded_video_path is not None:
            set_nested(json_data, ['encodedVideoPath'], encoded_video_path)
        if id is not None:
            set_nested(json_data, ['id'], id)
        if is_encoded is not None:
            set_nested(json_data, ['isEncoded'], is_encoded)
        if is_favorite is not None:
            set_nested(json_data, ['isFavorite'], is_favorite)
        if is_motion is not None:
            set_nested(json_data, ['isMotion'], is_motion)
        if is_not_in_album is not None:
            set_nested(json_data, ['isNotInAlbum'], is_not_in_album)
        if is_offline is not None:
            set_nested(json_data, ['isOffline'], is_offline)
        if lens_model is not None:
            set_nested(json_data, ['lensModel'], lens_model)
        if library_id is not None:
            set_nested(json_data, ['libraryId'], library_id)
        if make is not None:
            set_nested(json_data, ['make'], make)
        if model is not None:
            set_nested(json_data, ['model'], model)
        if ocr is not None:
            set_nested(json_data, ['ocr'], ocr)
        if order is not None:
            set_nested(json_data, ['order'], order)
        if original_file_name is not None:
            set_nested(json_data, ['originalFileName'], original_file_name)
        if original_path is not None:
            set_nested(json_data, ['originalPath'], original_path)
        if page is not None:
            set_nested(json_data, ['page'], page)
        if person_ids is not None:
            set_nested(json_data, ['personIds'], person_ids)
        if preview_path is not None:
            set_nested(json_data, ['previewPath'], preview_path)
        if rating is not None:
            set_nested(json_data, ['rating'], rating)
        if size is not None:
            set_nested(json_data, ['size'], size)
        if state is not None:
            set_nested(json_data, ['state'], state)
        if tag_ids is not None:
            set_nested(json_data, ['tagIds'], tag_ids)
        if taken_after is not None:
            set_nested(json_data, ['takenAfter'], taken_after)
        if taken_before is not None:
            set_nested(json_data, ['takenBefore'], taken_before)
        if thumbnail_path is not None:
            set_nested(json_data, ['thumbnailPath'], thumbnail_path)
        if trashed_after is not None:
            set_nested(json_data, ['trashedAfter'], trashed_after)
        if trashed_before is not None:
            set_nested(json_data, ['trashedBefore'], trashed_before)
        if type is not None:
            set_nested(json_data, ['type'], type)
        if updated_after is not None:
            set_nested(json_data, ['updatedAfter'], updated_after)
        if updated_before is not None:
            set_nested(json_data, ['updatedBefore'], updated_before)
        if visibility is not None:
            set_nested(json_data, ['visibility'], visibility)
        if with_deleted is not None:
            set_nested(json_data, ['withDeleted'], with_deleted)
        if with_exif is not None:
            set_nested(json_data, ['withExif'], with_exif)
        if with_people is not None:
            set_nested(json_data, ['withPeople'], with_people)
        if with_stacked is not None:
            set_nested(json_data, ['withStacked'], with_stacked)
        from immich.client.models.metadata_search_dto import MetadataSearchDto
        metadata_search_dto = deserialize_request_body(json_data, MetadataSearchDto)
        kwargs['metadata_search_dto'] = metadata_search_dto
    client = ctx.obj['client']
    result = run_command(client, client.search, 'search_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-large-assets")
def search_large_assets(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(None, "--album-ids"),
    city: str | None = typer.Option(None, "--city"),
    country: str | None = typer.Option(None, "--country"),
    created_after: datetime | None = typer.Option(None, "--created-after"),
    created_before: datetime | None = typer.Option(None, "--created-before"),
    device_id: str | None = typer.Option(None, "--device-id"),
    is_encoded: str | None = typer.Option(None, "--is-encoded"),
    is_favorite: str | None = typer.Option(None, "--is-favorite"),
    is_motion: str | None = typer.Option(None, "--is-motion"),
    is_not_in_album: str | None = typer.Option(None, "--is-not-in-album"),
    is_offline: str | None = typer.Option(None, "--is-offline"),
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
    taken_after: datetime | None = typer.Option(None, "--taken-after"),
    taken_before: datetime | None = typer.Option(None, "--taken-before"),
    trashed_after: datetime | None = typer.Option(None, "--trashed-after"),
    trashed_before: datetime | None = typer.Option(None, "--trashed-before"),
    type: str | None = typer.Option(None, "--type"),
    updated_after: datetime | None = typer.Option(None, "--updated-after"),
    updated_before: datetime | None = typer.Option(None, "--updated-before"),
    visibility: str | None = typer.Option(None, "--visibility"),
    with_deleted: str | None = typer.Option(None, "--with-deleted"),
    with_exif: str | None = typer.Option(None, "--with-exif"),
) -> None:
    """Search large assets

Docs: https://api.immich.app/endpoints/search/searchLargeAssets
    """
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
        kwargs['is_encoded'] = is_encoded.lower() == 'true'
    if is_favorite is not None:
        kwargs['is_favorite'] = is_favorite.lower() == 'true'
    if is_motion is not None:
        kwargs['is_motion'] = is_motion.lower() == 'true'
    if is_not_in_album is not None:
        kwargs['is_not_in_album'] = is_not_in_album.lower() == 'true'
    if is_offline is not None:
        kwargs['is_offline'] = is_offline.lower() == 'true'
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
        kwargs['with_deleted'] = with_deleted.lower() == 'true'
    if with_exif is not None:
        kwargs['with_exif'] = with_exif.lower() == 'true'
    client = ctx.obj['client']
    result = run_command(client, client.search, 'search_large_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-person")
def search_person(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name"),
    with_hidden: str | None = typer.Option(None, "--with-hidden"),
) -> None:
    """Search people

Docs: https://api.immich.app/endpoints/search/searchPerson
    """
    kwargs = {}
    kwargs['name'] = name
    if with_hidden is not None:
        kwargs['with_hidden'] = with_hidden.lower() == 'true'
    client = ctx.obj['client']
    result = run_command(client, client.search, 'search_person', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-places")
def search_places(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name"),
) -> None:
    """Search places

Docs: https://api.immich.app/endpoints/search/searchPlaces
    """
    kwargs = {}
    kwargs['name'] = name
    client = ctx.obj['client']
    result = run_command(client, client.search, 'search_places', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-random")
def search_random(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(None, "--albumIds"),
    city: str | None = typer.Option(None, "--city"),
    country: str | None = typer.Option(None, "--country"),
    created_after: datetime | None = typer.Option(None, "--createdAfter"),
    created_before: datetime | None = typer.Option(None, "--createdBefore"),
    device_id: str | None = typer.Option(None, "--deviceId"),
    is_encoded: bool | None = typer.Option(None, "--isEncoded"),
    is_favorite: bool | None = typer.Option(None, "--isFavorite"),
    is_motion: bool | None = typer.Option(None, "--isMotion"),
    is_not_in_album: bool | None = typer.Option(None, "--isNotInAlbum"),
    is_offline: bool | None = typer.Option(None, "--isOffline"),
    lens_model: str | None = typer.Option(None, "--lensModel"),
    library_id: str | None = typer.Option(None, "--libraryId"),
    make: str | None = typer.Option(None, "--make"),
    model: str | None = typer.Option(None, "--model"),
    ocr: str | None = typer.Option(None, "--ocr"),
    person_ids: list[str] | None = typer.Option(None, "--personIds"),
    rating: float | None = typer.Option(None, "--rating"),
    size: float | None = typer.Option(None, "--size"),
    state: str | None = typer.Option(None, "--state"),
    tag_ids: list[str] | None = typer.Option(None, "--tagIds"),
    taken_after: datetime | None = typer.Option(None, "--takenAfter"),
    taken_before: datetime | None = typer.Option(None, "--takenBefore"),
    trashed_after: datetime | None = typer.Option(None, "--trashedAfter"),
    trashed_before: datetime | None = typer.Option(None, "--trashedBefore"),
    type: str | None = typer.Option(None, "--type"),
    updated_after: datetime | None = typer.Option(None, "--updatedAfter"),
    updated_before: datetime | None = typer.Option(None, "--updatedBefore"),
    visibility: str | None = typer.Option(None, "--visibility"),
    with_deleted: bool | None = typer.Option(None, "--withDeleted"),
    with_exif: bool | None = typer.Option(None, "--withExif"),
    with_people: bool | None = typer.Option(None, "--withPeople"),
    with_stacked: bool | None = typer.Option(None, "--withStacked"),
) -> None:
    """Search random assets

Docs: https://api.immich.app/endpoints/search/searchRandom
    """
    kwargs = {}
    has_flags = any([album_ids, city, country, created_after, created_before, device_id, is_encoded, is_favorite, is_motion, is_not_in_album, is_offline, lens_model, library_id, make, model, ocr, person_ids, rating, size, state, tag_ids, taken_after, taken_before, trashed_after, trashed_before, type, updated_after, updated_before, visibility, with_deleted, with_exif, with_people, with_stacked])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([album_ids, city, country, created_after, created_before, device_id, is_encoded, is_favorite, is_motion, is_not_in_album, is_offline, lens_model, library_id, make, model, ocr, person_ids, rating, size, state, tag_ids, taken_after, taken_before, trashed_after, trashed_before, type, updated_after, updated_before, visibility, with_deleted, with_exif, with_people, with_stacked]):
        json_data = {}
        if album_ids is not None:
            set_nested(json_data, ['albumIds'], album_ids)
        if city is not None:
            set_nested(json_data, ['city'], city)
        if country is not None:
            set_nested(json_data, ['country'], country)
        if created_after is not None:
            set_nested(json_data, ['createdAfter'], created_after)
        if created_before is not None:
            set_nested(json_data, ['createdBefore'], created_before)
        if device_id is not None:
            set_nested(json_data, ['deviceId'], device_id)
        if is_encoded is not None:
            set_nested(json_data, ['isEncoded'], is_encoded)
        if is_favorite is not None:
            set_nested(json_data, ['isFavorite'], is_favorite)
        if is_motion is not None:
            set_nested(json_data, ['isMotion'], is_motion)
        if is_not_in_album is not None:
            set_nested(json_data, ['isNotInAlbum'], is_not_in_album)
        if is_offline is not None:
            set_nested(json_data, ['isOffline'], is_offline)
        if lens_model is not None:
            set_nested(json_data, ['lensModel'], lens_model)
        if library_id is not None:
            set_nested(json_data, ['libraryId'], library_id)
        if make is not None:
            set_nested(json_data, ['make'], make)
        if model is not None:
            set_nested(json_data, ['model'], model)
        if ocr is not None:
            set_nested(json_data, ['ocr'], ocr)
        if person_ids is not None:
            set_nested(json_data, ['personIds'], person_ids)
        if rating is not None:
            set_nested(json_data, ['rating'], rating)
        if size is not None:
            set_nested(json_data, ['size'], size)
        if state is not None:
            set_nested(json_data, ['state'], state)
        if tag_ids is not None:
            set_nested(json_data, ['tagIds'], tag_ids)
        if taken_after is not None:
            set_nested(json_data, ['takenAfter'], taken_after)
        if taken_before is not None:
            set_nested(json_data, ['takenBefore'], taken_before)
        if trashed_after is not None:
            set_nested(json_data, ['trashedAfter'], trashed_after)
        if trashed_before is not None:
            set_nested(json_data, ['trashedBefore'], trashed_before)
        if type is not None:
            set_nested(json_data, ['type'], type)
        if updated_after is not None:
            set_nested(json_data, ['updatedAfter'], updated_after)
        if updated_before is not None:
            set_nested(json_data, ['updatedBefore'], updated_before)
        if visibility is not None:
            set_nested(json_data, ['visibility'], visibility)
        if with_deleted is not None:
            set_nested(json_data, ['withDeleted'], with_deleted)
        if with_exif is not None:
            set_nested(json_data, ['withExif'], with_exif)
        if with_people is not None:
            set_nested(json_data, ['withPeople'], with_people)
        if with_stacked is not None:
            set_nested(json_data, ['withStacked'], with_stacked)
        from immich.client.models.random_search_dto import RandomSearchDto
        random_search_dto = deserialize_request_body(json_data, RandomSearchDto)
        kwargs['random_search_dto'] = random_search_dto
    client = ctx.obj['client']
    result = run_command(client, client.search, 'search_random', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-smart")
def search_smart(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(None, "--albumIds"),
    city: str | None = typer.Option(None, "--city"),
    country: str | None = typer.Option(None, "--country"),
    created_after: datetime | None = typer.Option(None, "--createdAfter"),
    created_before: datetime | None = typer.Option(None, "--createdBefore"),
    device_id: str | None = typer.Option(None, "--deviceId"),
    is_encoded: bool | None = typer.Option(None, "--isEncoded"),
    is_favorite: bool | None = typer.Option(None, "--isFavorite"),
    is_motion: bool | None = typer.Option(None, "--isMotion"),
    is_not_in_album: bool | None = typer.Option(None, "--isNotInAlbum"),
    is_offline: bool | None = typer.Option(None, "--isOffline"),
    language: str | None = typer.Option(None, "--language"),
    lens_model: str | None = typer.Option(None, "--lensModel"),
    library_id: str | None = typer.Option(None, "--libraryId"),
    make: str | None = typer.Option(None, "--make"),
    model: str | None = typer.Option(None, "--model"),
    ocr: str | None = typer.Option(None, "--ocr"),
    page: float | None = typer.Option(None, "--page"),
    person_ids: list[str] | None = typer.Option(None, "--personIds"),
    query: str | None = typer.Option(None, "--query"),
    query_asset_id: str | None = typer.Option(None, "--queryAssetId"),
    rating: float | None = typer.Option(None, "--rating"),
    size: float | None = typer.Option(None, "--size"),
    state: str | None = typer.Option(None, "--state"),
    tag_ids: list[str] | None = typer.Option(None, "--tagIds"),
    taken_after: datetime | None = typer.Option(None, "--takenAfter"),
    taken_before: datetime | None = typer.Option(None, "--takenBefore"),
    trashed_after: datetime | None = typer.Option(None, "--trashedAfter"),
    trashed_before: datetime | None = typer.Option(None, "--trashedBefore"),
    type: str | None = typer.Option(None, "--type"),
    updated_after: datetime | None = typer.Option(None, "--updatedAfter"),
    updated_before: datetime | None = typer.Option(None, "--updatedBefore"),
    visibility: str | None = typer.Option(None, "--visibility"),
    with_deleted: bool | None = typer.Option(None, "--withDeleted"),
    with_exif: bool | None = typer.Option(None, "--withExif"),
) -> None:
    """Smart asset search

Docs: https://api.immich.app/endpoints/search/searchSmart
    """
    kwargs = {}
    has_flags = any([album_ids, city, country, created_after, created_before, device_id, is_encoded, is_favorite, is_motion, is_not_in_album, is_offline, language, lens_model, library_id, make, model, ocr, page, person_ids, query, query_asset_id, rating, size, state, tag_ids, taken_after, taken_before, trashed_after, trashed_before, type, updated_after, updated_before, visibility, with_deleted, with_exif])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([album_ids, city, country, created_after, created_before, device_id, is_encoded, is_favorite, is_motion, is_not_in_album, is_offline, language, lens_model, library_id, make, model, ocr, page, person_ids, query, query_asset_id, rating, size, state, tag_ids, taken_after, taken_before, trashed_after, trashed_before, type, updated_after, updated_before, visibility, with_deleted, with_exif]):
        json_data = {}
        if album_ids is not None:
            set_nested(json_data, ['albumIds'], album_ids)
        if city is not None:
            set_nested(json_data, ['city'], city)
        if country is not None:
            set_nested(json_data, ['country'], country)
        if created_after is not None:
            set_nested(json_data, ['createdAfter'], created_after)
        if created_before is not None:
            set_nested(json_data, ['createdBefore'], created_before)
        if device_id is not None:
            set_nested(json_data, ['deviceId'], device_id)
        if is_encoded is not None:
            set_nested(json_data, ['isEncoded'], is_encoded)
        if is_favorite is not None:
            set_nested(json_data, ['isFavorite'], is_favorite)
        if is_motion is not None:
            set_nested(json_data, ['isMotion'], is_motion)
        if is_not_in_album is not None:
            set_nested(json_data, ['isNotInAlbum'], is_not_in_album)
        if is_offline is not None:
            set_nested(json_data, ['isOffline'], is_offline)
        if language is not None:
            set_nested(json_data, ['language'], language)
        if lens_model is not None:
            set_nested(json_data, ['lensModel'], lens_model)
        if library_id is not None:
            set_nested(json_data, ['libraryId'], library_id)
        if make is not None:
            set_nested(json_data, ['make'], make)
        if model is not None:
            set_nested(json_data, ['model'], model)
        if ocr is not None:
            set_nested(json_data, ['ocr'], ocr)
        if page is not None:
            set_nested(json_data, ['page'], page)
        if person_ids is not None:
            set_nested(json_data, ['personIds'], person_ids)
        if query is not None:
            set_nested(json_data, ['query'], query)
        if query_asset_id is not None:
            set_nested(json_data, ['queryAssetId'], query_asset_id)
        if rating is not None:
            set_nested(json_data, ['rating'], rating)
        if size is not None:
            set_nested(json_data, ['size'], size)
        if state is not None:
            set_nested(json_data, ['state'], state)
        if tag_ids is not None:
            set_nested(json_data, ['tagIds'], tag_ids)
        if taken_after is not None:
            set_nested(json_data, ['takenAfter'], taken_after)
        if taken_before is not None:
            set_nested(json_data, ['takenBefore'], taken_before)
        if trashed_after is not None:
            set_nested(json_data, ['trashedAfter'], trashed_after)
        if trashed_before is not None:
            set_nested(json_data, ['trashedBefore'], trashed_before)
        if type is not None:
            set_nested(json_data, ['type'], type)
        if updated_after is not None:
            set_nested(json_data, ['updatedAfter'], updated_after)
        if updated_before is not None:
            set_nested(json_data, ['updatedBefore'], updated_before)
        if visibility is not None:
            set_nested(json_data, ['visibility'], visibility)
        if with_deleted is not None:
            set_nested(json_data, ['withDeleted'], with_deleted)
        if with_exif is not None:
            set_nested(json_data, ['withExif'], with_exif)
        from immich.client.models.smart_search_dto import SmartSearchDto
        smart_search_dto = deserialize_request_body(json_data, SmartSearchDto)
        kwargs['smart_search_dto'] = smart_search_dto
    client = ctx.obj['client']
    result = run_command(client, client.search, 'search_smart', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
