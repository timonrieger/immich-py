"""Generated CLI commands for Workflows tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""A workflow is a set of actions that run whenever a triggering event occurs. Workflows also can include filters to further limit execution.

Docs: https://api.immich.app/endpoints/workflows""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-workflow")
def create_workflow(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    actions: list[str] = typer.Option(..., "--actions", help="JSON string for actions"),
    description: str | None = typer.Option(None, "--description"),
    enabled: bool | None = typer.Option(None, "--enabled"),
    filters: list[str] = typer.Option(..., "--filters", help="JSON string for filters"),
    name: str = typer.Option(..., "--name"),
    trigger_type: str = typer.Option(..., "--triggerType"),
) -> None:
    """Create a workflow

Docs: https://api.immich.app/endpoints/workflows/createWorkflow
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([actions, description, enabled, filters, name, trigger_type])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.workflow_create_dto import WorkflowCreateDto
        workflow_create_dto = deserialize_request_body(json_data, WorkflowCreateDto)
        kwargs['workflow_create_dto'] = workflow_create_dto
    elif any([
        actions,
        description,
        enabled,
        filters,
        name,
        trigger_type,
    ]):
        # Build body from dotted flags
        json_data = {}
        if actions is None:
            raise SystemExit("Error: --actions is required")
        value_actions = json.loads(actions)
        set_nested(json_data, ['actions'], value_actions)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if enabled is not None:
            set_nested(json_data, ['enabled'], enabled)
        if filters is None:
            raise SystemExit("Error: --filters is required")
        value_filters = json.loads(filters)
        set_nested(json_data, ['filters'], value_filters)
        if name is None:
            raise SystemExit("Error: --name is required")
        set_nested(json_data, ['name'], name)
        if trigger_type is None:
            raise SystemExit("Error: --triggerType is required")
        set_nested(json_data, ['triggerType'], trigger_type)
        if json_data:
            from immich.client.models.workflow_create_dto import WorkflowCreateDto
            workflow_create_dto = deserialize_request_body(json_data, WorkflowCreateDto)
            kwargs['workflow_create_dto'] = workflow_create_dto
    client = ctx.obj['client']
    api_group = client.workflows
    result = run_command(client, api_group, 'create_workflow', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
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
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.workflows
    result = run_command(client, api_group, 'delete_workflow', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
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
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.workflows
    result = run_command(client, api_group, 'get_workflow', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-workflows")
def get_workflows(
    ctx: typer.Context,
) -> None:
    """List all workflows

Docs: https://api.immich.app/endpoints/workflows/getWorkflows
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.workflows
    result = run_command(client, api_group, 'get_workflows', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-workflow")
def update_workflow(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    actions: list[str] | None = typer.Option(None, "--actions", help="JSON string for actions"),
    description: str | None = typer.Option(None, "--description"),
    enabled: bool | None = typer.Option(None, "--enabled"),
    filters: list[str] | None = typer.Option(None, "--filters", help="JSON string for filters"),
    name: str | None = typer.Option(None, "--name"),
    trigger_type: str | None = typer.Option(None, "--triggerType"),
) -> None:
    """Update a workflow

Docs: https://api.immich.app/endpoints/workflows/updateWorkflow
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([actions, description, enabled, filters, name, trigger_type])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.workflow_update_dto import WorkflowUpdateDto
        workflow_update_dto = deserialize_request_body(json_data, WorkflowUpdateDto)
        kwargs['workflow_update_dto'] = workflow_update_dto
    elif any([
        actions,
        description,
        enabled,
        filters,
        name,
        trigger_type,
    ]):
        # Build body from dotted flags
        json_data = {}
        if actions is not None:
            value_actions = json.loads(actions)
            set_nested(json_data, ['actions'], value_actions)
        if description is not None:
            set_nested(json_data, ['description'], description)
        if enabled is not None:
            set_nested(json_data, ['enabled'], enabled)
        if filters is not None:
            value_filters = json.loads(filters)
            set_nested(json_data, ['filters'], value_filters)
        if name is not None:
            set_nested(json_data, ['name'], name)
        if trigger_type is not None:
            set_nested(json_data, ['triggerType'], trigger_type)
        if json_data:
            from immich.client.models.workflow_update_dto import WorkflowUpdateDto
            workflow_update_dto = deserialize_request_body(json_data, WorkflowUpdateDto)
            kwargs['workflow_update_dto'] = workflow_update_dto
    client = ctx.obj['client']
    api_group = client.workflows
    result = run_command(client, api_group, 'update_workflow', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
