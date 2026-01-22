"""Generated CLI commands for People tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
import json
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A person is a collection of faces, which can be favorited and named. A person can also be merged into another person. People are automatically created via the face recognition job.\n\n[link=https://api.immich.app/endpoints/people]Immich API documentation[/link]"""
)


@app.command("create-person", deprecated=False, rich_help_panel="API commands")
def create_person(
    ctx: typer.Context,
    birth_date: str | None = typer.Option(
        None,
        "--birth-date",
        help="""Person date of birth.
Note: the mobile app cannot currently set the birth date to null.""",
    ),
    color: str | None = typer.Option(None, "--color", help=""""""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=""""""
    ),
    is_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--is-hidden", help="""Person visibility"""
    ),
    name: str | None = typer.Option(None, "--name", help="""Person name."""),
) -> None:
    """Create a person

    [link=https://api.immich.app/endpoints/people/createPerson]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if birth_date is not None:
        set_nested(json_data, ["birth_date"], birth_date)
    if color is not None:
        set_nested(json_data, ["color"], color)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if is_hidden is not None:
        set_nested(json_data, ["is_hidden"], is_hidden.lower() == "true")
    if name is not None:
        set_nested(json_data, ["name"], name)
    person_create_dto = PersonCreateDto.model_validate(json_data)
    kwargs["person_create_dto"] = person_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "create_person", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-people", deprecated=False, rich_help_panel="API commands")
def delete_people(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Delete people

    [link=https://api.immich.app/endpoints/people/deletePeople]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "delete_people", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-person", deprecated=False, rich_help_panel="API commands")
def delete_person(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete person

    [link=https://api.immich.app/endpoints/people/deletePerson]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "delete_person", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-all-people", deprecated=False, rich_help_panel="API commands")
def get_all_people(
    ctx: typer.Context,
    closest_asset_id: str | None = typer.Option(
        None, "--closest-asset-id", help=""""""
    ),
    closest_person_id: str | None = typer.Option(
        None, "--closest-person-id", help=""""""
    ),
    page: float | None = typer.Option(
        None, "--page", help="""Page number for pagination""", min=1
    ),
    size: float | None = typer.Option(
        None, "--size", help="""Number of items per page""", min=1, max=1000
    ),
    with_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--with-hidden", help=""""""
    ),
) -> None:
    """Get all people

    [link=https://api.immich.app/endpoints/people/getAllPeople]Immich API documentation[/link]
    """
    kwargs = {}
    if closest_asset_id is not None:
        kwargs["closest_asset_id"] = closest_asset_id
    if closest_person_id is not None:
        kwargs["closest_person_id"] = closest_person_id
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    if with_hidden is not None:
        kwargs["with_hidden"] = with_hidden.lower() == "true"
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "get_all_people", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-person", deprecated=False, rich_help_panel="API commands")
def get_person(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Get a person

    [link=https://api.immich.app/endpoints/people/getPerson]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "get_person", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-person-statistics", deprecated=False, rich_help_panel="API commands")
def get_person_statistics(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Get person statistics

    [link=https://api.immich.app/endpoints/people/getPersonStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "get_person_statistics", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-person-thumbnail", deprecated=False, rich_help_panel="API commands")
def get_person_thumbnail(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Get person thumbnail

    [link=https://api.immich.app/endpoints/people/getPersonThumbnail]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "get_person_thumbnail", ctx, **kwargs)
    print_response(result, ctx)


@app.command("merge-person", deprecated=False, rich_help_panel="API commands")
def merge_person(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Merge people

    [link=https://api.immich.app/endpoints/people/mergePerson]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    merge_person_dto = MergePersonDto.model_validate(json_data)
    kwargs["merge_person_dto"] = merge_person_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "merge_person", ctx, **kwargs)
    print_response(result, ctx)


@app.command("reassign-faces", deprecated=False, rich_help_panel="API commands")
def reassign_faces(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    data: list[str] = typer.Option(..., "--data", help="""As a JSON string"""),
) -> None:
    """Reassign faces

    [link=https://api.immich.app/endpoints/people/reassignFaces]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_data = [json.loads(i) for i in data]
    set_nested(json_data, ["data"], value_data)
    asset_face_update_dto = AssetFaceUpdateDto.model_validate(json_data)
    kwargs["asset_face_update_dto"] = asset_face_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "reassign_faces", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-people", deprecated=False, rich_help_panel="API commands")
def update_people(
    ctx: typer.Context,
    people: list[str] = typer.Option(..., "--people", help="""As a JSON string"""),
) -> None:
    """Update people

    [link=https://api.immich.app/endpoints/people/updatePeople]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_people = [json.loads(i) for i in people]
    set_nested(json_data, ["people"], value_people)
    people_update_dto = PeopleUpdateDto.model_validate(json_data)
    kwargs["people_update_dto"] = people_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "update_people", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-person", deprecated=False, rich_help_panel="API commands")
def update_person(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    birth_date: str | None = typer.Option(
        None,
        "--birth-date",
        help="""Person date of birth.
Note: the mobile app cannot currently set the birth date to null.""",
    ),
    color: str | None = typer.Option(None, "--color", help=""""""),
    feature_face_asset_id: str | None = typer.Option(
        None,
        "--feature-face-asset-id",
        help="""Asset is used to get the feature face thumbnail.""",
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=""""""
    ),
    is_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--is-hidden", help="""Person visibility"""
    ),
    name: str | None = typer.Option(None, "--name", help="""Person name."""),
) -> None:
    """Update person

    [link=https://api.immich.app/endpoints/people/updatePerson]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if birth_date is not None:
        set_nested(json_data, ["birth_date"], birth_date)
    if color is not None:
        set_nested(json_data, ["color"], color)
    if feature_face_asset_id is not None:
        set_nested(json_data, ["feature_face_asset_id"], feature_face_asset_id)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if is_hidden is not None:
        set_nested(json_data, ["is_hidden"], is_hidden.lower() == "true")
    if name is not None:
        set_nested(json_data, ["name"], name)
    person_update_dto = PersonUpdateDto.model_validate(json_data)
    kwargs["person_update_dto"] = person_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.people, "update_person", ctx, **kwargs)
    print_response(result, ctx)
