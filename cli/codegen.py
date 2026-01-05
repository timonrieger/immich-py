#!/usr/bin/env python3
"""Generate Typer CLI commands from OpenAPI specification."""

from __future__ import annotations

import argparse
import json
import keyword
import os
import re
import shutil
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def project_root() -> Path:
    """Get project root directory."""
    return Path(__file__).resolve().parents[1]


def openapi_url(ref: str) -> str:
    """Build OpenAPI spec URL from git ref."""
    return (
        "https://raw.githubusercontent.com/immich-app/immich/"
        f"{ref}/open-api/immich-openapi-specs.json"
    )

def fetch_openapi_spec_json(url: str) -> dict[str, Any]:
    """Fetch and parse OpenAPI JSON from a URL."""
    req = urllib.request.Request(url, headers={"User-Agent": "immich-cli-codegen"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Failed to fetch OpenAPI spec (status={e.code})") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Failed to fetch OpenAPI spec: {e.reason}") from e

    try:
        return json.loads(data.decode("utf-8"))
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in OpenAPI spec: {e}") from e


def to_snake_case(name: str) -> str:
    """Convert string to snake_case."""
    # Insert underscore before uppercase letters (except first)
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Insert underscore before uppercase letters that follow lowercase
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    # Replace spaces/hyphens with underscores and lowercase
    s3 = re.sub(r"[\s-]+", "_", s2)
    # Replace any remaining non-identifier characters (e.g. parentheses, slashes)
    s4 = re.sub(r"[^A-Za-z0-9_]", "_", s3)
    s5 = re.sub(r"_+", "_", s4).strip("_")
    return s5.lower()


def to_kebab_case(name: str) -> str:
    """Convert string to kebab-case."""
    snake = to_snake_case(name)
    return snake.replace("_", "-")

def to_python_ident(name: str) -> str:
    """Convert an OpenAPI name into a safe Python identifier.

    This must match (or be compatible with) openapi-generator's Python naming:
    - snake_case
    - avoid keywords like `for`, `from`, `class`, etc.
    """
    ident = to_snake_case(name)
    if not ident:
        return "param"
    if ident[0].isdigit():
        ident = "_" + ident
    if keyword.iskeyword(ident):
        ident = ident + "_"
    return ident


def python_type_from_schema(schema: dict[str, Any], spec: dict[str, Any] | None = None) -> str:
    """Convert OpenAPI schema to Python type hint."""
    if "type" not in schema:
        # Reference or complex type
        if "$ref" in schema:
            # For CLI params, prefer JSON-serializable primitives where possible.
            # Avoid emitting model/enums here because Python 3.14+ will eagerly
            # evaluate string annotations (Typer -> inspect), requiring imports.
            if spec is not None:
                resolved = resolve_schema_ref(spec, schema["$ref"])
                # enums are represented as strings/ints in CLI
                if "enum" in resolved:
                    t = resolved.get("type")
                    if t == "integer":
                        return "int"
                    if t == "boolean":
                        return "bool"
                    if t == "number":
                        return "float"
                    return "str"
                # fall back to resolved primitive if present
                if "type" in resolved:
                    return python_type_from_schema(resolved, spec=None)
            # Avoid typing.Any in CLI signatures: Typer/Click rejects it.
            return "str"
        return "Any"

    schema_type = schema["type"]
    if schema_type == "string":
        if "format" in schema:
            fmt = schema["format"]
            if fmt == "uuid":
                return "str"  # UUID as string for CLI
            if fmt == "date-time":
                return "str"  # datetime as string for CLI
        return "str"
    elif schema_type == "integer":
        return "int"
    elif schema_type == "number":
        return "float"
    elif schema_type == "boolean":
        return "bool"
    elif schema_type == "array":
        items = schema.get("items", {})
        item_type = python_type_from_schema(items)
        # Keep list item types Click-friendly.
        if item_type not in {"str", "int", "float", "bool"}:
            item_type = "str"
        return f"list[{item_type}]"
    elif schema_type == "object":
        # Click can't map arbitrary objects; accept JSON as a string.
        return "str"
    else:
        return "str"


def validate_operation(operation: dict[str, Any], path: str, method: str) -> None:
    """Validate operation meets CLI generation requirements."""
    if "operationId" not in operation:
        raise ValueError(
            f"Operation {method.upper()} {path} missing required 'operationId'"
        )

    if "tags" not in operation or not operation["tags"]:
        raise ValueError(
            f"Operation {operation.get('operationId')} missing required 'tags'"
        )

    # Check parameters
    for param in operation.get("parameters", []):
        param_in = param.get("in")
        if param_in not in ["path", "query", "header"]:
            raise ValueError(
                f"Operation {operation.get('operationId')} has unsupported "
                f"parameter location: {param_in} "
                "(only 'path', 'query', and 'header' supported)"
            )

    # Check request body
    if "requestBody" in operation:
        content = operation["requestBody"].get("content", {})
        supported = {"application/json", "multipart/form-data"}
        content_types = set(content.keys())
        if not (content_types & supported):
            raise ValueError(
                f"Operation {operation.get('operationId')} has requestBody but no "
                f"supported content type. Supported: {sorted(supported)}. "
                f"Found: {sorted(content.keys())}"
            )

        # Require $ref schema for supported content types (keeps codegen deterministic)
        for ct in sorted(content_types & supported):
            schema = content.get(ct, {}).get("schema", {})
            if "$ref" not in schema:
                raise ValueError(
                    f"Operation {operation.get('operationId')} has requestBody with "
                    f"'{ct}' but schema is not a $ref (unsupported)"
                )


def resolve_schema_ref(spec: dict[str, Any], ref: str) -> dict[str, Any]:
    """Resolve a local OpenAPI $ref like '#/components/schemas/Foo'."""
    if not ref.startswith("#/"):
        raise ValueError(f"Unsupported $ref (only local refs supported): {ref}")
    cur: Any = spec
    for part in ref.lstrip("#/").split("/"):
        if not isinstance(cur, dict) or part not in cur:
            raise ValueError(f"Unresolvable $ref: {ref}")
        cur = cur[part]
    if not isinstance(cur, dict):
        raise ValueError(f"Unresolvable $ref (not an object): {ref}")
    return cur


def get_request_body_info(
    operation: dict[str, Any], spec: dict[str, Any]
) -> tuple[str, str, dict[str, Any]] | None:
    """Return (content_type, model_name, resolved_schema) for requestBody."""
    if "requestBody" not in operation:
        return None

    content = operation["requestBody"].get("content", {})
    if "application/json" in content:
        schema = content.get("application/json", {}).get("schema", {})
        ref = schema["$ref"]
        return ("application/json", ref.split("/")[-1], resolve_schema_ref(spec, ref))
    if "multipart/form-data" in content:
        schema = content.get("multipart/form-data", {}).get("schema", {})
        ref = schema["$ref"]
        return ("multipart/form-data", ref.split("/")[-1], resolve_schema_ref(spec, ref))
    return None


def generate_command_function(
    operation: dict[str, Any],
    path: str,
    method: str,
    spec: dict[str, Any],
    tag_attr: str,
) -> str:
    """Generate a Typer command function for an operation."""
    operation_id = operation["operationId"]
    func_name = to_snake_case(operation_id)
    cmd_name = to_kebab_case(operation_id)

    # Extract parameters
    path_params: list[dict[str, Any]] = []
    query_params: list[dict[str, Any]] = []
    header_params: list[dict[str, Any]] = []

    for param in operation.get("parameters", []):
        if param["in"] == "path":
            path_params.append(param)
        elif param["in"] == "query":
            query_params.append(param)
        elif param["in"] == "header":
            header_params.append(param)

    # Get request body info
    request_body_info = get_request_body_info(operation, spec)

    # Build function signature
    lines = [f'@app.command("{cmd_name}")']
    lines.append(f"def {func_name}(")
    # Typer context must be a non-default parameter; emit it first to avoid
    # Python's "non-default follows default" SyntaxError.
    lines.append("    ctx: typer.Context,")

    # Path parameters (required positional)
    for param in sorted(path_params, key=lambda p: p["name"]):
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        schema = param.get("schema", {"type": "string"})
        param_type = python_type_from_schema(schema, spec)
        required = param.get("required", False)
        if required:
            lines.append(f"    {param_name}: {param_type},")
        else:
            lines.append(f"    {param_name}: {param_type} | None = None,")

    # Query parameters (optional flags)
    for param in sorted(query_params, key=lambda p: p["name"]):
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        schema = param.get("schema", {"type": "string"})
        param_type = python_type_from_schema(schema, spec)
        flag_name = to_kebab_case(openapi_name)
        required = param.get("required", False)
        if required:
            lines.append(
                f"    {param_name}: {param_type} = typer.Option(..., \"--{flag_name}\"),"
            )
        else:
            lines.append(
                f"    {param_name}: {param_type} | None = typer.Option(None, \"--{flag_name}\"),"
            )

    # Header parameters (optional flags)
    for param in sorted(header_params, key=lambda p: p["name"]):
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        schema = param.get("schema", {"type": "string"})
        param_type = python_type_from_schema(schema, spec)
        flag_name = to_kebab_case(openapi_name)
        required = param.get("required", False)
        if required:
            lines.append(
                f"    {param_name}: {param_type} = typer.Option(..., \"--{flag_name}\"),"
            )
        else:
            lines.append(
                f"    {param_name}: {param_type} | None = typer.Option(None, \"--{flag_name}\"),"
            )

    # Request body options
    if request_body_info:
        content_type, request_body_model, resolved_schema = request_body_info
        if content_type == "application/json":
            lines.append(
                '    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),'
            )
        elif content_type == "multipart/form-data":
            # Keep rule: requestBody => --json PATH for non-file fields
            lines.append(
                '    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with multipart fields (non-file)"),'
            )
            # Add file-part options for binary fields
            props = resolved_schema.get("properties", {}) if isinstance(resolved_schema, dict) else {}
            required_props = set(resolved_schema.get("required", []) or [])
            for prop_name, prop_schema in sorted(props.items(), key=lambda kv: kv[0]):
                if not isinstance(prop_schema, dict):
                    continue
                if prop_schema.get("type") == "string" and prop_schema.get("format") == "binary":
                    arg_name = to_python_ident(prop_name)
                    opt_name = to_kebab_case(prop_name)
                    if prop_name in required_props:
                        lines.append(
                            f'    {arg_name}: Path = typer.Option(..., "--{opt_name}", help="File to upload for {prop_name}"),'
                        )
                    else:
                        lines.append(
                            f'    {arg_name}: Path | None = typer.Option(None, "--{opt_name}", help="File to upload for {prop_name}"),'
                        )

    lines.append(") -> None:")

    # Function body
    lines.append('    """' + operation.get("summary", operation_id) + '"""')
    lines.append("    from pathlib import Path")
    lines.append("    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command")

    # Build kwargs
    lines.append("    kwargs = {}")

    # Add path params
    for param in path_params:
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        lines.append(f"    kwargs['{param_name}'] = {param_name}")

    # Add query params
    for param in query_params:
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        required = param.get("required", False)
        if required:
            lines.append(f"    kwargs['{param_name}'] = {param_name}")
        else:
            lines.append(f"    if {param_name} is not None:")
            lines.append(f"        kwargs['{param_name}'] = {param_name}")

    # Add header params
    for param in header_params:
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        required = param.get("required", False)
        if required:
            lines.append(f"    kwargs['{param_name}'] = {param_name}")
        else:
            lines.append(f"    if {param_name} is not None:")
            lines.append(f"        kwargs['{param_name}'] = {param_name}")

    # Handle request body
    if request_body_info:
        content_type, request_body_model, resolved_schema = request_body_info
        if content_type == "application/json":
            # Infer parameter name from model name (e.g., UserUpdateMeDto -> user_update_me_dto)
            body_param_name = to_python_ident(request_body_model)
            lines.append("    if json_path is not None:")
            lines.append("        json_data = load_json_file(json_path)")
            # Model import path: convert ModelNameDto to model_name_dto.py
            model_module = to_snake_case(request_body_model)
            lines.append(
                f"        from immich.client.models.{model_module} import {request_body_model}"
            )
            lines.append(
                f"        {body_param_name} = deserialize_request_body(json_data, {request_body_model})"
            )
            lines.append(f"        kwargs['{body_param_name}'] = {body_param_name}")
        elif content_type == "multipart/form-data":
            # Load json fields (non-file) and merge into kwargs using snake_case keys
            props = (
                resolved_schema.get("properties", {})
                if isinstance(resolved_schema, dict)
                else {}
            )
            required_props = set(resolved_schema.get("required", []) or [])
            lines.append(
                "    json_data = load_json_file(json_path) if json_path is not None else {}"
            )
            # Fail loudly if required non-file fields are missing
            lines.append("    missing: list[str] = []")
            for prop_name, prop_schema in sorted(props.items(), key=lambda kv: kv[0]):
                if not isinstance(prop_schema, dict):
                    continue
                snake = to_snake_case(prop_name)
                snake = to_python_ident(prop_name)
                is_binary = (
                    prop_schema.get("type") == "string"
                    and prop_schema.get("format") == "binary"
                )
                if is_binary:
                    # File fields come from dedicated CLI options
                    if prop_name in required_props:
                        lines.append(f"    kwargs['{snake}'] = load_file_bytes({snake})")
                    else:
                        lines.append(f"    if {snake} is not None:")
                        lines.append(
                            f"        kwargs['{snake}'] = load_file_bytes({snake})"
                        )
                else:
                    # Prefer original OpenAPI key, fallback to snake_case key
                    lines.append(f"    if '{prop_name}' in json_data:")
                    lines.append(
                        f"        kwargs['{snake}'] = json_data['{prop_name}']"
                    )
                    lines.append(f"    elif '{snake}' in json_data:")
                    lines.append(f"        kwargs['{snake}'] = json_data['{snake}']")
                    if prop_name in required_props:
                        lines.append("    else:")
                        lines.append(f"        missing.append('{prop_name}')")
            lines.append("    if missing:")
            lines.append(
                "        raise SystemExit("
                "\"Error: missing required multipart fields: \" + ', '.join(missing) + "
                "\". Provide them via --json and/or file options.\""
                ")"
            )

    # Get client and API group
    lines.append("    client = ctx.obj['client']")
    lines.append(f"    api_group = client.{tag_attr}")

    # Call method
    method_name = to_snake_case(operation_id)
    lines.append(f"    result = run_command(client, api_group, '{method_name}', **kwargs)")

    # Print result
    lines.append("    format_mode = ctx.obj.get('format', 'pretty')")
    lines.append("    print_response(result, format_mode)")

    return "\n".join(lines)


def generate_tag_app(
    tag: str, operations: list[tuple[str, str, dict[str, Any]]], spec: dict[str, Any]
) -> str:
    """Generate a Typer app module for a tag."""
    tag_snake = to_snake_case(tag)
    tag_attr = tag_snake  # This should match AsyncClient attribute

    lines = [
        '"""Generated CLI commands for ' + tag + ' tag (auto-generated, do not edit)."""',
        "",
        "from __future__ import annotations",
        "",
        "from pathlib import Path",
        "from typing import Any",
        "import typer",
        "from typer import Context",
        "",
        f"app = typer.Typer(help=\"{tag} operations\")",
        "",
    ]

    # Generate command for each operation
    for path, method, operation in sorted(operations, key=lambda x: x[2].get("operationId", "")):
        func_code = generate_command_function(operation, path, method, spec, tag_attr)
        lines.append(func_code)
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    """Main codegen entrypoint."""
    parser = argparse.ArgumentParser(
        description="Generate Immich CLI from OpenAPI specification."
    )
    parser.add_argument(
        "--ref",
        default=os.environ.get("IMMICH_OPENAPI_REF", "main"),
        help="Immich git ref for OpenAPI spec (default: IMMICH_OPENAPI_REF or 'main')",
    )
    args = parser.parse_args()

    root = project_root()
    generated_dir = root / "immich" / "cli" / "generated"
    apps_dir = generated_dir / "apps"

    # Fetch OpenAPI spec
    url = openapi_url(args.ref)
    print(f"Fetching OpenAPI spec from: {url}")

    try:
        spec = fetch_openapi_spec_json(url)
    except RuntimeError as e:
        print(f"Error: {e}", file=__import__("sys").stderr)
        return 1

    # Validate and group operations
    operations_by_tag: dict[str, list[tuple[str, str, dict[str, Any]]]] = {}

    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method not in ["get", "post", "put", "patch", "delete"]:
                continue

            try:
                validate_operation(operation, path, method)
            except ValueError as e:
                print(f"Error: {e}", file=__import__("sys").stderr)
                return 1

            # Group by first tag
            tags = operation.get("tags", [])
            tag = tags[0] if tags else "default"
            if tag not in operations_by_tag:
                operations_by_tag[tag] = []
            operations_by_tag[tag].append((path, method, operation))

    # Clean and recreate generated directory
    if generated_dir.exists():
        shutil.rmtree(generated_dir)
    generated_dir.mkdir(parents=True, exist_ok=True)
    apps_dir.mkdir(parents=True, exist_ok=True)

    # Generate app modules
    apps_dict: dict[str, str] = {}
    for tag in sorted(operations_by_tag.keys()):
        operations = operations_by_tag[tag]
        tag_snake = to_snake_case(tag)
        app_content = generate_tag_app(tag, operations, spec)

        app_file = apps_dir / f"{tag_snake}.py"
        app_file.write_text(app_content, encoding="utf-8")
        # Use a CLI-safe group name (no spaces/parentheses)
        apps_dict[to_kebab_case(tag)] = f"immich.cli.generated.apps.{tag_snake}"

    # Generate __init__.py
    init_lines = [
        '"""Generated CLI commands (auto-generated, do not edit)."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "import typer",
        "",
    ]

    # Import apps
    for tag_cli, module_path in sorted(apps_dict.items()):
        # module_path ends with <tag_snake>
        tag_snake = module_path.rsplit(".", 1)[-1]
        init_lines.append(f"from immich.cli.generated.apps import {tag_snake}")

    init_lines.append("")
    init_lines.append("APPS: dict[str, typer.Typer] = {")

    for tag_cli, module_path in sorted(apps_dict.items()):
        tag_snake = module_path.rsplit(".", 1)[-1]
        init_lines.append(f'    "{tag_cli}": {tag_snake}.app,')

    init_lines.append("}")

    init_file = generated_dir / "__init__.py"
    init_file.write_text("\n".join(init_lines), encoding="utf-8")

    print(f"Generated CLI commands for {len(operations_by_tag)} tags")
    print(f"Output directory: {generated_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

