"""Generated CLI commands for People tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""A person is a collection of faces, which can be favorited and named. A person can also be merged into another person. People are automatically created via the face recognition job.

Docs: https://api.immich.app/endpoints/people""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-person")
def create_person(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    birth_date: str | None = typer.Option(
        None, "--birthDate", help="""Person date of birth"""
    ),
    color: str | None = typer.Option(None, "--color", help="""Person color (hex)"""),
    is_favorite: bool | None = typer.Option(
        None, "--isFavorite", help="""Mark as favorite"""
    ),
    is_hidden: bool | None = typer.Option(
        None, "--isHidden", help="""Person visibility (hidden)"""
    ),
    name: str | None = typer.Option(None, "--name", help="""Person name"""),
) -> None:
    """Create a person

    Docs: https://api.immich.app/endpoints/people/createPerson
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([birth_date, color, is_favorite, is_hidden, name])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.person_create_dto import PersonCreateDto

        person_create_dto = deserialize_request_body(json_data, PersonCreateDto)
        kwargs["person_create_dto"] = person_create_dto
    elif any(
        [
            birth_date,
            color,
            is_favorite,
            is_hidden,
            name,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if birth_date is not None:
            set_nested(json_data, ["birthDate"], birth_date)
        if color is not None:
            set_nested(json_data, ["color"], color)
        if is_favorite is not None:
            set_nested(json_data, ["isFavorite"], is_favorite)
        if is_hidden is not None:
            set_nested(json_data, ["isHidden"], is_hidden)
        if name is not None:
            set_nested(json_data, ["name"], name)
        if json_data:
            from immich.client.models.person_create_dto import PersonCreateDto

            person_create_dto = deserialize_request_body(json_data, PersonCreateDto)
            kwargs["person_create_dto"] = person_create_dto
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "create_person", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-people")
def delete_people(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Delete people

    Docs: https://api.immich.app/endpoints/people/deletePeople
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([ids])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    elif any(
        [
            ids,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ["ids"], ids)
        if json_data:
            from immich.client.models.bulk_ids_dto import BulkIdsDto

            bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
            kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "delete_people", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-person")
def delete_person(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Person ID"""),
) -> None:
    """Delete person

    Docs: https://api.immich.app/endpoints/people/deletePerson
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "delete_person", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-all-people")
def get_all_people(
    ctx: typer.Context,
    closest_asset_id: str | None = typer.Option(
        None, "--closest-asset-id", help="""Closest asset ID for similarity search"""
    ),
    closest_person_id: str | None = typer.Option(
        None, "--closest-person-id", help="""Closest person ID for similarity search"""
    ),
    page: float | None = typer.Option(
        None, "--page", help="""Page number for pagination"""
    ),
    size: float | None = typer.Option(
        None, "--size", help="""Number of items per page"""
    ),
    with_hidden: bool | None = typer.Option(
        None, "--with-hidden", help="""Include hidden people"""
    ),
) -> None:
    """Get all people

    Docs: https://api.immich.app/endpoints/people/getAllPeople
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
        kwargs["with_hidden"] = with_hidden
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "get_all_people", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-person")
def get_person(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Person ID"""),
) -> None:
    """Get a person

    Docs: https://api.immich.app/endpoints/people/getPerson
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "get_person", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-person-statistics")
def get_person_statistics(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Person ID"""),
) -> None:
    """Get person statistics

    Docs: https://api.immich.app/endpoints/people/getPersonStatistics
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "get_person_statistics", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-person-thumbnail")
def get_person_thumbnail(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Person ID"""),
) -> None:
    """Get person thumbnail

    Docs: https://api.immich.app/endpoints/people/getPersonThumbnail
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "get_person_thumbnail", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("merge-person")
def merge_person(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Target person ID to merge into"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    ids: list[str] = typer.Option(..., "--ids", help="""Person IDs to merge"""),
) -> None:
    """Merge people

    Docs: https://api.immich.app/endpoints/people/mergePerson
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([ids])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.merge_person_dto import MergePersonDto

        merge_person_dto = deserialize_request_body(json_data, MergePersonDto)
        kwargs["merge_person_dto"] = merge_person_dto
    elif any(
        [
            ids,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ["ids"], ids)
        if json_data:
            from immich.client.models.merge_person_dto import MergePersonDto

            merge_person_dto = deserialize_request_body(json_data, MergePersonDto)
            kwargs["merge_person_dto"] = merge_person_dto
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "merge_person", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("reassign-faces")
def reassign_faces(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Target person ID"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    data: list[str] = typer.Option(..., "--data", help="""Face update items"""),
) -> None:
    """Reassign faces

    Docs: https://api.immich.app/endpoints/people/reassignFaces
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([data])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_face_update_dto import AssetFaceUpdateDto

        asset_face_update_dto = deserialize_request_body(json_data, AssetFaceUpdateDto)
        kwargs["asset_face_update_dto"] = asset_face_update_dto
    elif any(
        [
            data,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if data is None:
            raise SystemExit("Error: --data is required")
        value_data = json.loads(data)
        set_nested(json_data, ["data"], value_data)
        if json_data:
            from immich.client.models.asset_face_update_dto import AssetFaceUpdateDto

            asset_face_update_dto = deserialize_request_body(
                json_data, AssetFaceUpdateDto
            )
            kwargs["asset_face_update_dto"] = asset_face_update_dto
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "reassign_faces", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-people")
def update_people(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    people: list[str] = typer.Option(..., "--people", help="""People to update"""),
) -> None:
    """Update people

    Docs: https://api.immich.app/endpoints/people/updatePeople
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([people])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.people_update_dto import PeopleUpdateDto

        people_update_dto = deserialize_request_body(json_data, PeopleUpdateDto)
        kwargs["people_update_dto"] = people_update_dto
    elif any(
        [
            people,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if people is None:
            raise SystemExit("Error: --people is required")
        value_people = json.loads(people)
        set_nested(json_data, ["people"], value_people)
        if json_data:
            from immich.client.models.people_update_dto import PeopleUpdateDto

            people_update_dto = deserialize_request_body(json_data, PeopleUpdateDto)
            kwargs["people_update_dto"] = people_update_dto
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "update_people", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-person")
def update_person(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Person ID"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    birth_date: str | None = typer.Option(
        None, "--birthDate", help="""Person date of birth"""
    ),
    color: str | None = typer.Option(None, "--color", help="""Person color (hex)"""),
    feature_face_asset_id: str | None = typer.Option(
        None,
        "--featureFaceAssetId",
        help="""Asset ID used for feature face thumbnail""",
    ),
    is_favorite: bool | None = typer.Option(
        None, "--isFavorite", help="""Mark as favorite"""
    ),
    is_hidden: bool | None = typer.Option(
        None, "--isHidden", help="""Person visibility (hidden)"""
    ),
    name: str | None = typer.Option(None, "--name", help="""Person name"""),
) -> None:
    """Update person

    Docs: https://api.immich.app/endpoints/people/updatePerson
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any(
        [birth_date, color, feature_face_asset_id, is_favorite, is_hidden, name]
    )
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.person_update_dto import PersonUpdateDto

        person_update_dto = deserialize_request_body(json_data, PersonUpdateDto)
        kwargs["person_update_dto"] = person_update_dto
    elif any(
        [
            birth_date,
            color,
            feature_face_asset_id,
            is_favorite,
            is_hidden,
            name,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if birth_date is not None:
            set_nested(json_data, ["birthDate"], birth_date)
        if color is not None:
            set_nested(json_data, ["color"], color)
        if feature_face_asset_id is not None:
            set_nested(json_data, ["featureFaceAssetId"], feature_face_asset_id)
        if is_favorite is not None:
            set_nested(json_data, ["isFavorite"], is_favorite)
        if is_hidden is not None:
            set_nested(json_data, ["isHidden"], is_hidden)
        if name is not None:
            set_nested(json_data, ["name"], name)
        if json_data:
            from immich.client.models.person_update_dto import PersonUpdateDto

            person_update_dto = deserialize_request_body(json_data, PersonUpdateDto)
            kwargs["person_update_dto"] = person_update_dto
    client = ctx.obj["client"]
    api_group = client.people
    result = run_command(client, api_group, "update_person", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
