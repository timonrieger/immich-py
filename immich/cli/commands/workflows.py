"""Generated CLI commands for Workflows tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    parse_complex_list,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""A workflow is a set of actions that run whenever a triggering event occurs. Workflows also can include filters to further limit execution.

Docs: https://api.immich.app/endpoints/workflows""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-workflow")
def create_workflow(
    ctx: typer.Context,
    actions: list[str] = typer.Option(
        ...,
        "--actions",
        help="key=value pairs (repeatable); e.g. key1=value1,key2=value2",
    ),
    description: str | None = typer.Option(None, "--description"),
    enabled: bool | None = typer.Option(None, "--enabled"),
    filters: list[str] = typer.Option(
        ...,
        "--filters",
        help="key=value pairs (repeatable); e.g. key1=value1,key2=value2",
    ),
    name: str = typer.Option(..., "--name"),
    trigger_type: str = typer.Option(..., "--triggerType"),
) -> None:
    """Create a workflow

    Docs: https://api.immich.app/endpoints/workflows/createWorkflow
    """
    kwargs = {}
    has_flags = any([actions, description, enabled, filters, name, trigger_type])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([actions, description, enabled, filters, name, trigger_type]):
        json_data = {}
        value_actions = parse_complex_list(actions)
        set_nested(json_data, ["actions"], value_actions)
        if description is not None:
            set_nested(json_data, ["description"], description)
        if enabled is not None:
            set_nested(json_data, ["enabled"], enabled)
        value_filters = parse_complex_list(filters)
        set_nested(json_data, ["filters"], value_filters)
        set_nested(json_data, ["name"], name)
        set_nested(json_data, ["triggerType"], trigger_type)
        from immich.client.models.workflow_create_dto import WorkflowCreateDto

        workflow_create_dto = deserialize_request_body(json_data, WorkflowCreateDto)
        kwargs["workflow_create_dto"] = workflow_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.workflows, "create_workflow", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-workflow")
def delete_workflow(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a workflow

    Docs: https://api.immich.app/endpoints/workflows/deleteWorkflow
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.workflows, "delete_workflow", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-workflow")
def get_workflow(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a workflow

    Docs: https://api.immich.app/endpoints/workflows/getWorkflow
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.workflows, "get_workflow", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-workflows")
def get_workflows(
    ctx: typer.Context,
) -> None:
    """List all workflows

    Docs: https://api.immich.app/endpoints/workflows/getWorkflows
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.workflows, "get_workflows", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-workflow")
def update_workflow(
    ctx: typer.Context,
    id: str,
    actions: list[str] | None = typer.Option(
        None,
        "--actions",
        help="key=value pairs (repeatable); e.g. key1=value1,key2=value2",
    ),
    description: str | None = typer.Option(None, "--description"),
    enabled: bool | None = typer.Option(None, "--enabled"),
    filters: list[str] | None = typer.Option(
        None,
        "--filters",
        help="key=value pairs (repeatable); e.g. key1=value1,key2=value2",
    ),
    name: str | None = typer.Option(None, "--name"),
    trigger_type: str | None = typer.Option(None, "--triggerType"),
) -> None:
    """Update a workflow

    Docs: https://api.immich.app/endpoints/workflows/updateWorkflow
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([actions, description, enabled, filters, name, trigger_type])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([actions, description, enabled, filters, name, trigger_type]):
        json_data = {}
        if actions is not None:
            value_actions = parse_complex_list(actions)
            set_nested(json_data, ["actions"], value_actions)
        if description is not None:
            set_nested(json_data, ["description"], description)
        if enabled is not None:
            set_nested(json_data, ["enabled"], enabled)
        if filters is not None:
            value_filters = parse_complex_list(filters)
            set_nested(json_data, ["filters"], value_filters)
        if name is not None:
            set_nested(json_data, ["name"], name)
        if trigger_type is not None:
            set_nested(json_data, ["triggerType"], trigger_type)
        from immich.client.models.workflow_update_dto import WorkflowUpdateDto

        workflow_update_dto = deserialize_request_body(json_data, WorkflowUpdateDto)
        kwargs["workflow_update_dto"] = workflow_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.workflows, "update_workflow", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
