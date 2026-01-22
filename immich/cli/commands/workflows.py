"""Generated CLI commands for Workflows tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
import json
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A workflow is a set of actions that run whenever a triggering event occurs. Workflows also can include filters to further limit execution.\n\n[link=https://api.immich.app/endpoints/workflows]Immich API documentation[/link]"""
)


@app.command("create-workflow", deprecated=False, rich_help_panel="API commands")
def create_workflow(
    ctx: typer.Context,
    actions: list[str] = typer.Option(..., "--actions", help="""As a JSON string"""),
    description: str | None = typer.Option(None, "--description", help=""""""),
    enabled: Literal["true", "false"] | None = typer.Option(
        None, "--enabled", help=""""""
    ),
    filters: list[str] = typer.Option(..., "--filters", help="""As a JSON string"""),
    name: str = typer.Option(..., "--name", help=""""""),
    trigger_type: str = typer.Option(..., "--trigger-type", help=""""""),
) -> None:
    """Create a workflow

    [link=https://api.immich.app/endpoints/workflows/createWorkflow]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_actions = [json.loads(i) for i in actions]
    set_nested(json_data, ["actions"], value_actions)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if enabled is not None:
        set_nested(json_data, ["enabled"], enabled.lower() == "true")
    value_filters = [json.loads(i) for i in filters]
    set_nested(json_data, ["filters"], value_filters)
    set_nested(json_data, ["name"], name)
    set_nested(json_data, ["trigger_type"], trigger_type)
    workflow_create_dto = WorkflowCreateDto.model_validate(json_data)
    kwargs["workflow_create_dto"] = workflow_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.workflows, "create_workflow", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-workflow", deprecated=False, rich_help_panel="API commands")
def delete_workflow(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a workflow

    [link=https://api.immich.app/endpoints/workflows/deleteWorkflow]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.workflows, "delete_workflow", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-workflow", deprecated=False, rich_help_panel="API commands")
def get_workflow(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a workflow

    [link=https://api.immich.app/endpoints/workflows/getWorkflow]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.workflows, "get_workflow", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-workflows", deprecated=False, rich_help_panel="API commands")
def get_workflows(
    ctx: typer.Context,
) -> None:
    """List all workflows

    [link=https://api.immich.app/endpoints/workflows/getWorkflows]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.workflows, "get_workflows", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-workflow", deprecated=False, rich_help_panel="API commands")
def update_workflow(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    actions: list[str] | None = typer.Option(
        None, "--actions", help="""As a JSON string"""
    ),
    description: str | None = typer.Option(None, "--description", help=""""""),
    enabled: Literal["true", "false"] | None = typer.Option(
        None, "--enabled", help=""""""
    ),
    filters: list[str] | None = typer.Option(
        None, "--filters", help="""As a JSON string"""
    ),
    name: str | None = typer.Option(None, "--name", help=""""""),
) -> None:
    """Update a workflow

    [link=https://api.immich.app/endpoints/workflows/updateWorkflow]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if actions is not None:
        value_actions = [json.loads(i) for i in actions]
        set_nested(json_data, ["actions"], value_actions)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if enabled is not None:
        set_nested(json_data, ["enabled"], enabled.lower() == "true")
    if filters is not None:
        value_filters = [json.loads(i) for i in filters]
        set_nested(json_data, ["filters"], value_filters)
    if name is not None:
        set_nested(json_data, ["name"], name)
    workflow_update_dto = WorkflowUpdateDto.model_validate(json_data)
    kwargs["workflow_update_dto"] = workflow_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.workflows, "update_workflow", ctx, **kwargs)
    print_response(result, ctx)
