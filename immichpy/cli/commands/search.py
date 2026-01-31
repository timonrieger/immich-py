"""Generated CLI commands for Search tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command, set_nested
from immichpy.client.generated.models import *

app = typer.Typer(
    help="""Endpoints related to searching assets via text, smart search, optical character recognition (OCR), and other filters like person, album, and other metadata. Search endpoints usually support pagination and sorting.\n\n[link=https://api.immich.app/endpoints/search]Immich API documentation[/link]"""
)


@app.command("get-assets-by-city", deprecated=False, rich_help_panel="API commands")
def get_assets_by_city(
    ctx: typer.Context,
) -> None:
    """Retrieve assets by city

    [link=https://api.immich.app/endpoints/search/getAssetsByCity]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "get_assets_by_city", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-explore-data", deprecated=False, rich_help_panel="API commands")
def get_explore_data(
    ctx: typer.Context,
) -> None:
    """Retrieve explore data

    [link=https://api.immich.app/endpoints/search/getExploreData]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "get_explore_data", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-search-suggestions", deprecated=False, rich_help_panel="API commands")
def get_search_suggestions(
    ctx: typer.Context,
    country: str | None = typer.Option(None, "--country", help="""Filter by country"""),
    include_null: Literal["true", "false"] | None = typer.Option(
        None, "--include-null", help="""Include null values in suggestions"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help="""Filter by lens model"""
    ),
    make: str | None = typer.Option(None, "--make", help="""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help="""Filter by camera model"""
    ),
    state: str | None = typer.Option(
        None, "--state", help="""Filter by state/province"""
    ),
    type: SearchSuggestionType = typer.Option(
        ..., "--type", help="""Suggestion type"""
    ),
) -> None:
    """Retrieve search suggestions

    [link=https://api.immich.app/endpoints/search/getSearchSuggestions]Immich API documentation[/link]
    """
    kwargs = {}
    if country is not None:
        kwargs["country"] = country
    if include_null is not None:
        kwargs["include_null"] = include_null.lower() == "true"
    if lens_model is not None:
        kwargs["lens_model"] = lens_model
    if make is not None:
        kwargs["make"] = make
    if model is not None:
        kwargs["model"] = model
    if state is not None:
        kwargs["state"] = state
    kwargs["type"] = type
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "get_search_suggestions", ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "search-asset-statistics", deprecated=False, rich_help_panel="API commands"
)
def search_asset_statistics(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(
        None, "--album-ids", help="""Filter by album IDs"""
    ),
    city: str | None = typer.Option(None, "--city", help="""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help="""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None, "--created-after", help="""Filter by creation date (after)"""
    ),
    created_before: datetime | None = typer.Option(
        None, "--created-before", help="""Filter by creation date (before)"""
    ),
    description: str | None = typer.Option(
        None, "--description", help="""Filter by description text"""
    ),
    device_id: str | None = typer.Option(
        None, "--device-id", help="""Device ID to filter by"""
    ),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help="""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help="""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help="""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help="""Filter by offline status"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help="""Filter by lens model"""
    ),
    library_id: str | None = typer.Option(
        None, "--library-id", help="""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help="""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help="""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help="""Filter by OCR text content"""
    ),
    person_ids: list[str] | None = typer.Option(
        None, "--person-ids", help="""Filter by person IDs"""
    ),
    rating: float | None = typer.Option(
        None, "--rating", help="""Filter by rating""", min=-1, max=5
    ),
    state: str | None = typer.Option(
        None, "--state", help="""Filter by state/province name"""
    ),
    tag_ids: list[str] | None = typer.Option(
        None, "--tag-ids", help="""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None, "--taken-after", help="""Filter by taken date (after)"""
    ),
    taken_before: datetime | None = typer.Option(
        None, "--taken-before", help="""Filter by taken date (before)"""
    ),
    trashed_after: datetime | None = typer.Option(
        None, "--trashed-after", help="""Filter by trash date (after)"""
    ),
    trashed_before: datetime | None = typer.Option(
        None, "--trashed-before", help="""Filter by trash date (before)"""
    ),
    type: str | None = typer.Option(None, "--type", help="""Asset type"""),
    updated_after: datetime | None = typer.Option(
        None, "--updated-after", help="""Filter by update date (after)"""
    ),
    updated_before: datetime | None = typer.Option(
        None, "--updated-before", help="""Filter by update date (before)"""
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help="""Asset visibility"""
    ),
) -> None:
    """Search asset statistics

    [link=https://api.immich.app/endpoints/search/searchAssetStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if album_ids is not None:
        set_nested(json_data, ["album_ids"], album_ids)
    if city is not None:
        set_nested(json_data, ["city"], city)
    if country is not None:
        set_nested(json_data, ["country"], country)
    if created_after is not None:
        set_nested(json_data, ["created_after"], created_after)
    if created_before is not None:
        set_nested(json_data, ["created_before"], created_before)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if device_id is not None:
        set_nested(json_data, ["device_id"], device_id)
    if is_encoded is not None:
        set_nested(json_data, ["is_encoded"], is_encoded.lower() == "true")
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if is_motion is not None:
        set_nested(json_data, ["is_motion"], is_motion.lower() == "true")
    if is_not_in_album is not None:
        set_nested(json_data, ["is_not_in_album"], is_not_in_album.lower() == "true")
    if is_offline is not None:
        set_nested(json_data, ["is_offline"], is_offline.lower() == "true")
    if lens_model is not None:
        set_nested(json_data, ["lens_model"], lens_model)
    if library_id is not None:
        set_nested(json_data, ["library_id"], library_id)
    if make is not None:
        set_nested(json_data, ["make"], make)
    if model is not None:
        set_nested(json_data, ["model"], model)
    if ocr is not None:
        set_nested(json_data, ["ocr"], ocr)
    if person_ids is not None:
        set_nested(json_data, ["person_ids"], person_ids)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if state is not None:
        set_nested(json_data, ["state"], state)
    if tag_ids is not None:
        set_nested(json_data, ["tag_ids"], tag_ids)
    if taken_after is not None:
        set_nested(json_data, ["taken_after"], taken_after)
    if taken_before is not None:
        set_nested(json_data, ["taken_before"], taken_before)
    if trashed_after is not None:
        set_nested(json_data, ["trashed_after"], trashed_after)
    if trashed_before is not None:
        set_nested(json_data, ["trashed_before"], trashed_before)
    if type is not None:
        set_nested(json_data, ["type"], type)
    if updated_after is not None:
        set_nested(json_data, ["updated_after"], updated_after)
    if updated_before is not None:
        set_nested(json_data, ["updated_before"], updated_before)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    statistics_search_dto = StatisticsSearchDto.model_validate(json_data)
    kwargs["statistics_search_dto"] = statistics_search_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.search, "search_asset_statistics", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("search-assets", deprecated=False, rich_help_panel="API commands")
def search_assets(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(
        None, "--album-ids", help="""Filter by album IDs"""
    ),
    checksum: str | None = typer.Option(
        None, "--checksum", help="""Filter by file checksum"""
    ),
    city: str | None = typer.Option(None, "--city", help="""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help="""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None, "--created-after", help="""Filter by creation date (after)"""
    ),
    created_before: datetime | None = typer.Option(
        None, "--created-before", help="""Filter by creation date (before)"""
    ),
    description: str | None = typer.Option(
        None, "--description", help="""Filter by description text"""
    ),
    device_asset_id: str | None = typer.Option(
        None, "--device-asset-id", help="""Filter by device asset ID"""
    ),
    device_id: str | None = typer.Option(
        None, "--device-id", help="""Device ID to filter by"""
    ),
    encoded_video_path: str | None = typer.Option(
        None, "--encoded-video-path", help="""Filter by encoded video file path"""
    ),
    id: str | None = typer.Option(None, "--id", help="""Filter by asset ID"""),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help="""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help="""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help="""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help="""Filter by offline status"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help="""Filter by lens model"""
    ),
    library_id: str | None = typer.Option(
        None, "--library-id", help="""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help="""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help="""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help="""Filter by OCR text content"""
    ),
    order: str | None = typer.Option(None, "--order", help="""Asset sort order"""),
    original_file_name: str | None = typer.Option(
        None, "--original-file-name", help="""Filter by original file name"""
    ),
    original_path: str | None = typer.Option(
        None, "--original-path", help="""Filter by original file path"""
    ),
    page: float | None = typer.Option(None, "--page", help="""Page number""", min=1),
    person_ids: list[str] | None = typer.Option(
        None, "--person-ids", help="""Filter by person IDs"""
    ),
    preview_path: str | None = typer.Option(
        None, "--preview-path", help="""Filter by preview file path"""
    ),
    rating: float | None = typer.Option(
        None, "--rating", help="""Filter by rating""", min=-1, max=5
    ),
    size: float | None = typer.Option(
        None, "--size", help="""Number of results to return""", min=1, max=1000
    ),
    state: str | None = typer.Option(
        None, "--state", help="""Filter by state/province name"""
    ),
    tag_ids: list[str] | None = typer.Option(
        None, "--tag-ids", help="""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None, "--taken-after", help="""Filter by taken date (after)"""
    ),
    taken_before: datetime | None = typer.Option(
        None, "--taken-before", help="""Filter by taken date (before)"""
    ),
    thumbnail_path: str | None = typer.Option(
        None, "--thumbnail-path", help="""Filter by thumbnail file path"""
    ),
    trashed_after: datetime | None = typer.Option(
        None, "--trashed-after", help="""Filter by trash date (after)"""
    ),
    trashed_before: datetime | None = typer.Option(
        None, "--trashed-before", help="""Filter by trash date (before)"""
    ),
    type: str | None = typer.Option(None, "--type", help="""Asset type"""),
    updated_after: datetime | None = typer.Option(
        None, "--updated-after", help="""Filter by update date (after)"""
    ),
    updated_before: datetime | None = typer.Option(
        None, "--updated-before", help="""Filter by update date (before)"""
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help="""Asset visibility"""
    ),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help="""Include deleted assets"""
    ),
    with_exif: Literal["true", "false"] | None = typer.Option(
        None, "--with-exif", help="""Include EXIF data in response"""
    ),
    with_people: Literal["true", "false"] | None = typer.Option(
        None, "--with-people", help="""Include assets with people"""
    ),
    with_stacked: Literal["true", "false"] | None = typer.Option(
        None, "--with-stacked", help="""Include stacked assets"""
    ),
) -> None:
    """Search assets by metadata

    [link=https://api.immich.app/endpoints/search/searchAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if album_ids is not None:
        set_nested(json_data, ["album_ids"], album_ids)
    if checksum is not None:
        set_nested(json_data, ["checksum"], checksum)
    if city is not None:
        set_nested(json_data, ["city"], city)
    if country is not None:
        set_nested(json_data, ["country"], country)
    if created_after is not None:
        set_nested(json_data, ["created_after"], created_after)
    if created_before is not None:
        set_nested(json_data, ["created_before"], created_before)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if device_asset_id is not None:
        set_nested(json_data, ["device_asset_id"], device_asset_id)
    if device_id is not None:
        set_nested(json_data, ["device_id"], device_id)
    if encoded_video_path is not None:
        set_nested(json_data, ["encoded_video_path"], encoded_video_path)
    if id is not None:
        set_nested(json_data, ["id"], id)
    if is_encoded is not None:
        set_nested(json_data, ["is_encoded"], is_encoded.lower() == "true")
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if is_motion is not None:
        set_nested(json_data, ["is_motion"], is_motion.lower() == "true")
    if is_not_in_album is not None:
        set_nested(json_data, ["is_not_in_album"], is_not_in_album.lower() == "true")
    if is_offline is not None:
        set_nested(json_data, ["is_offline"], is_offline.lower() == "true")
    if lens_model is not None:
        set_nested(json_data, ["lens_model"], lens_model)
    if library_id is not None:
        set_nested(json_data, ["library_id"], library_id)
    if make is not None:
        set_nested(json_data, ["make"], make)
    if model is not None:
        set_nested(json_data, ["model"], model)
    if ocr is not None:
        set_nested(json_data, ["ocr"], ocr)
    if order is not None:
        set_nested(json_data, ["order"], order)
    if original_file_name is not None:
        set_nested(json_data, ["original_file_name"], original_file_name)
    if original_path is not None:
        set_nested(json_data, ["original_path"], original_path)
    if page is not None:
        set_nested(json_data, ["page"], page)
    if person_ids is not None:
        set_nested(json_data, ["person_ids"], person_ids)
    if preview_path is not None:
        set_nested(json_data, ["preview_path"], preview_path)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if size is not None:
        set_nested(json_data, ["size"], size)
    if state is not None:
        set_nested(json_data, ["state"], state)
    if tag_ids is not None:
        set_nested(json_data, ["tag_ids"], tag_ids)
    if taken_after is not None:
        set_nested(json_data, ["taken_after"], taken_after)
    if taken_before is not None:
        set_nested(json_data, ["taken_before"], taken_before)
    if thumbnail_path is not None:
        set_nested(json_data, ["thumbnail_path"], thumbnail_path)
    if trashed_after is not None:
        set_nested(json_data, ["trashed_after"], trashed_after)
    if trashed_before is not None:
        set_nested(json_data, ["trashed_before"], trashed_before)
    if type is not None:
        set_nested(json_data, ["type"], type)
    if updated_after is not None:
        set_nested(json_data, ["updated_after"], updated_after)
    if updated_before is not None:
        set_nested(json_data, ["updated_before"], updated_before)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    if with_deleted is not None:
        set_nested(json_data, ["with_deleted"], with_deleted.lower() == "true")
    if with_exif is not None:
        set_nested(json_data, ["with_exif"], with_exif.lower() == "true")
    if with_people is not None:
        set_nested(json_data, ["with_people"], with_people.lower() == "true")
    if with_stacked is not None:
        set_nested(json_data, ["with_stacked"], with_stacked.lower() == "true")
    metadata_search_dto = MetadataSearchDto.model_validate(json_data)
    kwargs["metadata_search_dto"] = metadata_search_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "search_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-large-assets", deprecated=False, rich_help_panel="API commands")
def search_large_assets(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(
        None, "--album-ids", help="""Filter by album IDs"""
    ),
    city: str | None = typer.Option(None, "--city", help="""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help="""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None, "--created-after", help="""Filter by creation date (after)"""
    ),
    created_before: datetime | None = typer.Option(
        None, "--created-before", help="""Filter by creation date (before)"""
    ),
    device_id: str | None = typer.Option(
        None, "--device-id", help="""Device ID to filter by"""
    ),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help="""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help="""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help="""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help="""Filter by offline status"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help="""Filter by lens model"""
    ),
    library_id: str | None = typer.Option(
        None, "--library-id", help="""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help="""Filter by camera make"""),
    min_file_size: int | None = typer.Option(
        None, "--min-file-size", help="""Minimum file size in bytes""", min=0
    ),
    model: str | None = typer.Option(
        None, "--model", help="""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help="""Filter by OCR text content"""
    ),
    person_ids: list[str] | None = typer.Option(
        None, "--person-ids", help="""Filter by person IDs"""
    ),
    rating: float | None = typer.Option(
        None, "--rating", help="""Filter by rating""", min=-1, max=5
    ),
    size: float | None = typer.Option(
        None, "--size", help="""Number of results to return""", min=1, max=1000
    ),
    state: str | None = typer.Option(
        None, "--state", help="""Filter by state/province name"""
    ),
    tag_ids: list[str] | None = typer.Option(
        None, "--tag-ids", help="""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None, "--taken-after", help="""Filter by taken date (after)"""
    ),
    taken_before: datetime | None = typer.Option(
        None, "--taken-before", help="""Filter by taken date (before)"""
    ),
    trashed_after: datetime | None = typer.Option(
        None, "--trashed-after", help="""Filter by trash date (after)"""
    ),
    trashed_before: datetime | None = typer.Option(
        None, "--trashed-before", help="""Filter by trash date (before)"""
    ),
    type: AssetTypeEnum | None = typer.Option(
        None, "--type", help="""Asset type filter"""
    ),
    updated_after: datetime | None = typer.Option(
        None, "--updated-after", help="""Filter by update date (after)"""
    ),
    updated_before: datetime | None = typer.Option(
        None, "--updated-before", help="""Filter by update date (before)"""
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help="""Filter by visibility"""
    ),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help="""Include deleted assets"""
    ),
    with_exif: Literal["true", "false"] | None = typer.Option(
        None, "--with-exif", help="""Include EXIF data in response"""
    ),
) -> None:
    """Search large assets

    [link=https://api.immich.app/endpoints/search/searchLargeAssets]Immich API documentation[/link]
    """
    kwargs = {}
    if album_ids is not None:
        kwargs["album_ids"] = album_ids
    if city is not None:
        kwargs["city"] = city
    if country is not None:
        kwargs["country"] = country
    if created_after is not None:
        kwargs["created_after"] = created_after
    if created_before is not None:
        kwargs["created_before"] = created_before
    if device_id is not None:
        kwargs["device_id"] = device_id
    if is_encoded is not None:
        kwargs["is_encoded"] = is_encoded.lower() == "true"
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite.lower() == "true"
    if is_motion is not None:
        kwargs["is_motion"] = is_motion.lower() == "true"
    if is_not_in_album is not None:
        kwargs["is_not_in_album"] = is_not_in_album.lower() == "true"
    if is_offline is not None:
        kwargs["is_offline"] = is_offline.lower() == "true"
    if lens_model is not None:
        kwargs["lens_model"] = lens_model
    if library_id is not None:
        kwargs["library_id"] = library_id
    if make is not None:
        kwargs["make"] = make
    if min_file_size is not None:
        kwargs["min_file_size"] = min_file_size
    if model is not None:
        kwargs["model"] = model
    if ocr is not None:
        kwargs["ocr"] = ocr
    if person_ids is not None:
        kwargs["person_ids"] = person_ids
    if rating is not None:
        kwargs["rating"] = rating
    if size is not None:
        kwargs["size"] = size
    if state is not None:
        kwargs["state"] = state
    if tag_ids is not None:
        kwargs["tag_ids"] = tag_ids
    if taken_after is not None:
        kwargs["taken_after"] = taken_after
    if taken_before is not None:
        kwargs["taken_before"] = taken_before
    if trashed_after is not None:
        kwargs["trashed_after"] = trashed_after
    if trashed_before is not None:
        kwargs["trashed_before"] = trashed_before
    if type is not None:
        kwargs["type"] = type
    if updated_after is not None:
        kwargs["updated_after"] = updated_after
    if updated_before is not None:
        kwargs["updated_before"] = updated_before
    if visibility is not None:
        kwargs["visibility"] = visibility
    if with_deleted is not None:
        kwargs["with_deleted"] = with_deleted.lower() == "true"
    if with_exif is not None:
        kwargs["with_exif"] = with_exif.lower() == "true"
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "search_large_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-person", deprecated=False, rich_help_panel="API commands")
def search_person(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name", help="""Person name to search for"""),
    with_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--with-hidden", help="""Include hidden people"""
    ),
) -> None:
    """Search people

    [link=https://api.immich.app/endpoints/search/searchPerson]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["name"] = name
    if with_hidden is not None:
        kwargs["with_hidden"] = with_hidden.lower() == "true"
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "search_person", ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-places", deprecated=False, rich_help_panel="API commands")
def search_places(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name", help="""Place name to search for"""),
) -> None:
    """Search places

    [link=https://api.immich.app/endpoints/search/searchPlaces]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["name"] = name
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "search_places", ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-random", deprecated=False, rich_help_panel="API commands")
def search_random(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(
        None, "--album-ids", help="""Filter by album IDs"""
    ),
    city: str | None = typer.Option(None, "--city", help="""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help="""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None, "--created-after", help="""Filter by creation date (after)"""
    ),
    created_before: datetime | None = typer.Option(
        None, "--created-before", help="""Filter by creation date (before)"""
    ),
    device_id: str | None = typer.Option(
        None, "--device-id", help="""Device ID to filter by"""
    ),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help="""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help="""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help="""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help="""Filter by offline status"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help="""Filter by lens model"""
    ),
    library_id: str | None = typer.Option(
        None, "--library-id", help="""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help="""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help="""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help="""Filter by OCR text content"""
    ),
    person_ids: list[str] | None = typer.Option(
        None, "--person-ids", help="""Filter by person IDs"""
    ),
    rating: float | None = typer.Option(
        None, "--rating", help="""Filter by rating""", min=-1, max=5
    ),
    size: float | None = typer.Option(
        None, "--size", help="""Number of results to return""", min=1, max=1000
    ),
    state: str | None = typer.Option(
        None, "--state", help="""Filter by state/province name"""
    ),
    tag_ids: list[str] | None = typer.Option(
        None, "--tag-ids", help="""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None, "--taken-after", help="""Filter by taken date (after)"""
    ),
    taken_before: datetime | None = typer.Option(
        None, "--taken-before", help="""Filter by taken date (before)"""
    ),
    trashed_after: datetime | None = typer.Option(
        None, "--trashed-after", help="""Filter by trash date (after)"""
    ),
    trashed_before: datetime | None = typer.Option(
        None, "--trashed-before", help="""Filter by trash date (before)"""
    ),
    type: str | None = typer.Option(None, "--type", help="""Asset type"""),
    updated_after: datetime | None = typer.Option(
        None, "--updated-after", help="""Filter by update date (after)"""
    ),
    updated_before: datetime | None = typer.Option(
        None, "--updated-before", help="""Filter by update date (before)"""
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help="""Asset visibility"""
    ),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help="""Include deleted assets"""
    ),
    with_exif: Literal["true", "false"] | None = typer.Option(
        None, "--with-exif", help="""Include EXIF data in response"""
    ),
    with_people: Literal["true", "false"] | None = typer.Option(
        None, "--with-people", help="""Include assets with people"""
    ),
    with_stacked: Literal["true", "false"] | None = typer.Option(
        None, "--with-stacked", help="""Include stacked assets"""
    ),
) -> None:
    """Search random assets

    [link=https://api.immich.app/endpoints/search/searchRandom]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if album_ids is not None:
        set_nested(json_data, ["album_ids"], album_ids)
    if city is not None:
        set_nested(json_data, ["city"], city)
    if country is not None:
        set_nested(json_data, ["country"], country)
    if created_after is not None:
        set_nested(json_data, ["created_after"], created_after)
    if created_before is not None:
        set_nested(json_data, ["created_before"], created_before)
    if device_id is not None:
        set_nested(json_data, ["device_id"], device_id)
    if is_encoded is not None:
        set_nested(json_data, ["is_encoded"], is_encoded.lower() == "true")
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if is_motion is not None:
        set_nested(json_data, ["is_motion"], is_motion.lower() == "true")
    if is_not_in_album is not None:
        set_nested(json_data, ["is_not_in_album"], is_not_in_album.lower() == "true")
    if is_offline is not None:
        set_nested(json_data, ["is_offline"], is_offline.lower() == "true")
    if lens_model is not None:
        set_nested(json_data, ["lens_model"], lens_model)
    if library_id is not None:
        set_nested(json_data, ["library_id"], library_id)
    if make is not None:
        set_nested(json_data, ["make"], make)
    if model is not None:
        set_nested(json_data, ["model"], model)
    if ocr is not None:
        set_nested(json_data, ["ocr"], ocr)
    if person_ids is not None:
        set_nested(json_data, ["person_ids"], person_ids)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if size is not None:
        set_nested(json_data, ["size"], size)
    if state is not None:
        set_nested(json_data, ["state"], state)
    if tag_ids is not None:
        set_nested(json_data, ["tag_ids"], tag_ids)
    if taken_after is not None:
        set_nested(json_data, ["taken_after"], taken_after)
    if taken_before is not None:
        set_nested(json_data, ["taken_before"], taken_before)
    if trashed_after is not None:
        set_nested(json_data, ["trashed_after"], trashed_after)
    if trashed_before is not None:
        set_nested(json_data, ["trashed_before"], trashed_before)
    if type is not None:
        set_nested(json_data, ["type"], type)
    if updated_after is not None:
        set_nested(json_data, ["updated_after"], updated_after)
    if updated_before is not None:
        set_nested(json_data, ["updated_before"], updated_before)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    if with_deleted is not None:
        set_nested(json_data, ["with_deleted"], with_deleted.lower() == "true")
    if with_exif is not None:
        set_nested(json_data, ["with_exif"], with_exif.lower() == "true")
    if with_people is not None:
        set_nested(json_data, ["with_people"], with_people.lower() == "true")
    if with_stacked is not None:
        set_nested(json_data, ["with_stacked"], with_stacked.lower() == "true")
    random_search_dto = RandomSearchDto.model_validate(json_data)
    kwargs["random_search_dto"] = random_search_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "search_random", ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-smart", deprecated=False, rich_help_panel="API commands")
def search_smart(
    ctx: typer.Context,
    album_ids: list[str] | None = typer.Option(
        None, "--album-ids", help="""Filter by album IDs"""
    ),
    city: str | None = typer.Option(None, "--city", help="""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help="""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None, "--created-after", help="""Filter by creation date (after)"""
    ),
    created_before: datetime | None = typer.Option(
        None, "--created-before", help="""Filter by creation date (before)"""
    ),
    device_id: str | None = typer.Option(
        None, "--device-id", help="""Device ID to filter by"""
    ),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help="""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help="""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help="""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help="""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help="""Filter by offline status"""
    ),
    language: str | None = typer.Option(
        None, "--language", help="""Search language code"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help="""Filter by lens model"""
    ),
    library_id: str | None = typer.Option(
        None, "--library-id", help="""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help="""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help="""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help="""Filter by OCR text content"""
    ),
    page: float | None = typer.Option(None, "--page", help="""Page number""", min=1),
    person_ids: list[str] | None = typer.Option(
        None, "--person-ids", help="""Filter by person IDs"""
    ),
    query: str | None = typer.Option(
        None, "--query", help="""Natural language search query"""
    ),
    query_asset_id: str | None = typer.Option(
        None, "--query-asset-id", help="""Asset ID to use as search reference"""
    ),
    rating: float | None = typer.Option(
        None, "--rating", help="""Filter by rating""", min=-1, max=5
    ),
    size: float | None = typer.Option(
        None, "--size", help="""Number of results to return""", min=1, max=1000
    ),
    state: str | None = typer.Option(
        None, "--state", help="""Filter by state/province name"""
    ),
    tag_ids: list[str] | None = typer.Option(
        None, "--tag-ids", help="""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None, "--taken-after", help="""Filter by taken date (after)"""
    ),
    taken_before: datetime | None = typer.Option(
        None, "--taken-before", help="""Filter by taken date (before)"""
    ),
    trashed_after: datetime | None = typer.Option(
        None, "--trashed-after", help="""Filter by trash date (after)"""
    ),
    trashed_before: datetime | None = typer.Option(
        None, "--trashed-before", help="""Filter by trash date (before)"""
    ),
    type: str | None = typer.Option(None, "--type", help="""Asset type"""),
    updated_after: datetime | None = typer.Option(
        None, "--updated-after", help="""Filter by update date (after)"""
    ),
    updated_before: datetime | None = typer.Option(
        None, "--updated-before", help="""Filter by update date (before)"""
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help="""Asset visibility"""
    ),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help="""Include deleted assets"""
    ),
    with_exif: Literal["true", "false"] | None = typer.Option(
        None, "--with-exif", help="""Include EXIF data in response"""
    ),
) -> None:
    """Smart asset search

    [link=https://api.immich.app/endpoints/search/searchSmart]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if album_ids is not None:
        set_nested(json_data, ["album_ids"], album_ids)
    if city is not None:
        set_nested(json_data, ["city"], city)
    if country is not None:
        set_nested(json_data, ["country"], country)
    if created_after is not None:
        set_nested(json_data, ["created_after"], created_after)
    if created_before is not None:
        set_nested(json_data, ["created_before"], created_before)
    if device_id is not None:
        set_nested(json_data, ["device_id"], device_id)
    if is_encoded is not None:
        set_nested(json_data, ["is_encoded"], is_encoded.lower() == "true")
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if is_motion is not None:
        set_nested(json_data, ["is_motion"], is_motion.lower() == "true")
    if is_not_in_album is not None:
        set_nested(json_data, ["is_not_in_album"], is_not_in_album.lower() == "true")
    if is_offline is not None:
        set_nested(json_data, ["is_offline"], is_offline.lower() == "true")
    if language is not None:
        set_nested(json_data, ["language"], language)
    if lens_model is not None:
        set_nested(json_data, ["lens_model"], lens_model)
    if library_id is not None:
        set_nested(json_data, ["library_id"], library_id)
    if make is not None:
        set_nested(json_data, ["make"], make)
    if model is not None:
        set_nested(json_data, ["model"], model)
    if ocr is not None:
        set_nested(json_data, ["ocr"], ocr)
    if page is not None:
        set_nested(json_data, ["page"], page)
    if person_ids is not None:
        set_nested(json_data, ["person_ids"], person_ids)
    if query is not None:
        set_nested(json_data, ["query"], query)
    if query_asset_id is not None:
        set_nested(json_data, ["query_asset_id"], query_asset_id)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if size is not None:
        set_nested(json_data, ["size"], size)
    if state is not None:
        set_nested(json_data, ["state"], state)
    if tag_ids is not None:
        set_nested(json_data, ["tag_ids"], tag_ids)
    if taken_after is not None:
        set_nested(json_data, ["taken_after"], taken_after)
    if taken_before is not None:
        set_nested(json_data, ["taken_before"], taken_before)
    if trashed_after is not None:
        set_nested(json_data, ["trashed_after"], trashed_after)
    if trashed_before is not None:
        set_nested(json_data, ["trashed_before"], trashed_before)
    if type is not None:
        set_nested(json_data, ["type"], type)
    if updated_after is not None:
        set_nested(json_data, ["updated_after"], updated_after)
    if updated_before is not None:
        set_nested(json_data, ["updated_before"], updated_before)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    if with_deleted is not None:
        set_nested(json_data, ["with_deleted"], with_deleted.lower() == "true")
    if with_exif is not None:
        set_nested(json_data, ["with_exif"], with_exif.lower() == "true")
    smart_search_dto = SmartSearchDto.model_validate(json_data)
    kwargs["smart_search_dto"] = smart_search_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.search, "search_smart", ctx, **kwargs)
    print_response(result, ctx)
