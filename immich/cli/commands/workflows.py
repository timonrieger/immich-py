"""Generated CLI commands for Workflows tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='A workflow is a set of actions that run whenever a triggering event occurs. Workflows also can include filters to further limit execution.. https://api.immich.app/endpoints/workflows', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-workflow")
def create_workflow(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create a workflow"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
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
    """Delete a workflow"""
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
    """Retrieve a workflow"""
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
    """List all workflows"""
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
) -> None:
    """Update a workflow"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.workflow_update_dto import WorkflowUpdateDto
        workflow_update_dto = deserialize_request_body(json_data, WorkflowUpdateDto)
        kwargs['workflow_update_dto'] = workflow_update_dto
    client = ctx.obj['client']
    api_group = client.workflows
    result = run_command(client, api_group, 'update_workflow', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
