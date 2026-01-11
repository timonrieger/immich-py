# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "inflection",
#   "urllib3",
# ]
# ///

from __future__ import annotations

import argparse
import keyword
import os
import shutil
import urllib3
from pathlib import Path
from typing import Any
import inflection

def openapi_url(ref: str) -> str:
    """Build OpenAPI spec URL from git ref."""
    return (
        "https://raw.githubusercontent.com/timonrieger/immich/"
        f"{ref}/open-api/immich-openapi-specs.json"
    )


def to_snake_case(name: str) -> str:
    """Convert string to snake_case."""
    # first get the underscore in, then take out all parenthesis with dashes, then underscore again
    snake = inflection.underscore(name)
    return inflection.parameterize(snake, separator="_")


def to_kebab_case(name: str) -> str:
    """Convert string to kebab-case."""
    snake = to_snake_case(name)
    return inflection.dasherize(snake)


def to_python_ident(name: str) -> str:
    """Convert an OpenAPI name into a safe Python identifier.

    This must match (or be compatible with) openapi-generator's Python naming:
    - snake_case
    - avoid keywords like `for`, `from`, `class`, etc.
    """
    ident = to_snake_case(name)
    if keyword.iskeyword(ident):
        ident = ident + "_"
    return ident


def python_type_from_schema(
    schema: dict[str, Any], spec: dict[str, Any] | None = None
) -> str:
    """Convert OpenAPI schema to Python type hint."""
    schema = normalize_schema(schema, spec)
    if "type" not in schema:
        # Reference or complex type
        if "$ref" in schema:
            # For CLI params, prefer JSON-serializable primitives where possible.
            # Avoid emitting model/enums here because Python 3.14+ will eagerly
            # evaluate string annotations (Typer -> inspect), requiring imports.
            if spec is not None:
                resolved = normalize_schema(resolve_schema_ref(spec, schema["$ref"]), spec)
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
        # No type and no $ref - treat as complex/unknown, return str
        return "str"

    schema_type = schema.get("type")
    if schema_type is None:
        return "str"
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


def normalize_schema(
    schema: dict[str, Any], spec: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Normalize a schema for CLI generation.

    Today this focuses on "allOf" by merging object-ish schemas so we can keep
    generating dotted flags instead of collapsing to JSON strings.
    """
    if not isinstance(schema, dict):
        return {}

    # If we can, resolve refs up-front to expose actual types/properties.
    if "$ref" in schema and spec is not None:
        schema = resolve_schema_ref(spec, schema["$ref"])

    # Merge allOf when possible (common in Immich OpenAPI for composed DTOs).
    if "allOf" in schema and isinstance(schema.get("allOf"), list):
        merged: dict[str, Any] = {k: v for k, v in schema.items() if k != "allOf"}
        merged_required: set[str] = set(merged.get("required", []) or [])
        merged_props: dict[str, Any] = dict(merged.get("properties", {}) or {})

        for sub in schema.get("allOf", []) or []:
            if not isinstance(sub, dict):
                continue
            sub_norm = normalize_schema(sub, spec)

            req = sub_norm.get("required")
            if isinstance(req, list):
                merged_required |= set(req)

            props = sub_norm.get("properties")
            if isinstance(props, dict):
                merged_props.update(props)

            for k, v in sub_norm.items():
                if k in {"properties", "required"}:
                    continue
                # last-one-wins is fine for CLI typing/flattening purposes
                merged[k] = v

        if merged_props:
            merged["type"] = "object"
            merged["properties"] = merged_props
        if merged_required:
            merged["required"] = sorted(merged_required)

        schema = merged

    return schema


def is_complex_type(schema: dict[str, Any], spec: dict[str, Any] | None = None) -> bool:
    """Check if schema represents a complex type (object, array-of-object, oneOf/anyOf, etc.)."""
    schema = normalize_schema(schema, spec)
    if "$ref" in schema:
        if spec is not None:
            resolved = resolve_schema_ref(spec, schema["$ref"])
            return is_complex_type(resolved, spec=None)
        return True  # Unknown ref, treat as complex
    
    schema_type = schema.get("type")
    if schema_type == "object":
        return True
    if schema_type == "array":
        items = schema.get("items", {})
        if "$ref" in items:
            return True
        if items.get("type") == "object":
            return True
        return is_complex_type(items, spec)
    
    # oneOf, anyOf, allOf are complex
    if any(key in schema for key in ["oneOf", "anyOf", "allOf"]):
        return True
    
    # additionalProperties indicates object-like structure
    if "additionalProperties" in schema:
        return True
    
    return False


def flatten_schema(
    schema: dict[str, Any],
    spec: dict[str, Any],
    path: list[str] | None = None,
    required_path: bool = True,
) -> list[tuple[list[str], dict[str, Any], bool]]:
    """Flatten a schema into leaf entries with dotted paths.
    
    Returns list of (path_parts, schema, is_required) tuples.
    """
    if path is None:
        path = []
    schema = normalize_schema(schema, spec)
    
    # Handle oneOf/anyOf - treat as complex, return single entry
    # (allOf is normalized above to keep flattening working)
    if any(key in schema for key in ["oneOf", "anyOf"]):
        return [(path, schema, required_path)]
    
    schema_type = schema.get("type")
    
    # Primitive or enum - leaf node
    if schema_type in ("string", "integer", "number", "boolean") or "enum" in schema:
        return [(path, schema, required_path)]
    
    # Array of primitives - leaf node
    if schema_type == "array":
        items = schema.get("items", {})
        if not is_complex_type(items, spec):
            return [(path, schema, required_path)]
        # Array of objects - treat as complex
        return [(path, schema, required_path)]
    
    # Object - recurse into properties
    if schema_type == "object":
        props = schema.get("properties", {})
        if not props:
            # Empty object or additionalProperties - treat as complex
            return [(path, schema, required_path)]
        
        required_props = set(schema.get("required", []) or [])
        results: list[tuple[list[str], dict[str, Any], bool]] = []
        
        for prop_name, prop_schema in props.items():
            if not isinstance(prop_schema, dict):
                continue
            new_path = path + [prop_name]
            results.extend(
                flatten_schema(
                    prop_schema,
                    spec,
                    new_path,
                    required_path=(required_path and prop_name in required_props),
                )
            )
        
        return results
    
    # Fallback: treat as complex
    return [(path, schema, required_path)]


def option_name_for_path(path_parts: list[str]) -> str:
    """Generate dotted option name from path parts, e.g. ['user', 'name'] -> '--user.name'."""
    return "--" + ".".join(path_parts)


def python_triple_quoted_str(value: str) -> str:
    """Return a Python triple-quoted string literal for generated source code."""
    # Avoid accidental termination of the literal.
    safe = value.replace('"""', '\\"""')
    return f'"""{safe}"""'


def get_request_body_info(
    operation: dict[str, Any], spec: dict[str, Any]
) -> tuple[str, str, dict[str, Any], bool] | None:
    """Return (content_type, model_name, resolved_schema, is_required) for requestBody."""
    if "requestBody" not in operation:
        return None

    request_body = operation["requestBody"]
    is_required = request_body.get("required", False)
    content = request_body.get("content", {})
    if "application/json" in content:
        schema = content.get("application/json", {}).get("schema", {})
        ref = schema["$ref"]
        return ("application/json", ref.split("/")[-1], resolve_schema_ref(spec, ref), is_required)
    if "multipart/form-data" in content:
        schema = content.get("multipart/form-data", {}).get("schema", {})
        ref = schema["$ref"]
        return (
            "multipart/form-data",
            ref.split("/")[-1],
            resolve_schema_ref(spec, ref),
            is_required,
        )
    return None


def generate_command_function(
    operation: dict[str, Any],
    spec: dict[str, Any],
    tag_attr: str,
    tag: str,
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

    # Track Python argument names to avoid duplicate arguments in the generated
    # function signature (e.g. path param `id` colliding with body field `id`).
    used_param_names: set[str] = {"ctx"}

    # Path parameters (required positional)
    for param in sorted(path_params, key=lambda p: p["name"]):
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        used_param_names.add(param_name)
        schema = param.get("schema", {"type": "string"})
        param_type = python_type_from_schema(schema, spec)
        required = param.get("required", False)
        description = param.get("description", "")
        if description:
            description_str = python_triple_quoted_str(description)
            if required:
                lines.append(
                    f'    {param_name}: {param_type} = typer.Argument(..., help={description_str}),'
                )
            else:
                lines.append(
                    f'    {param_name}: {param_type} | None = typer.Argument(None, help={description_str}),'
                )
        else:
            if required:
                lines.append(f"    {param_name}: {param_type},")
            else:
                lines.append(f"    {param_name}: {param_type} | None = None,")

    # Track all option names for collision detection
    used_option_names: set[str] = set()

    # Query parameters (optional flags)
    for param in sorted(query_params, key=lambda p: p["name"]):
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        used_param_names.add(param_name)
        schema = param.get("schema", {"type": "string"})
        param_type = python_type_from_schema(schema, spec)
        flag_name = to_kebab_case(openapi_name)
        full_opt_name = f"--{flag_name}"
        description = param.get("description", "")
        
        # Check for collisions
        if full_opt_name in used_option_names:
            raise ValueError(
                f"Option name collision in {operation_id}: '{full_opt_name}' already used (query param)"
            )
        used_option_names.add(full_opt_name)
        
        required = param.get("required", False)
        if description:
            description_str = python_triple_quoted_str(description)
            if required:
                lines.append(
                    f'    {param_name}: {param_type} = typer.Option(..., "--{flag_name}", help={description_str}),'
                )
            else:
                lines.append(
                    f'    {param_name}: {param_type} | None = typer.Option(None, "--{flag_name}", help={description_str}),'
                )
        else:
            if required:
                lines.append(
                    f'    {param_name}: {param_type} = typer.Option(..., "--{flag_name}"),'
                )
            else:
                lines.append(
                    f'    {param_name}: {param_type} | None = typer.Option(None, "--{flag_name}"),'
                )

    # Header parameters (optional flags)
    for param in sorted(header_params, key=lambda p: p["name"]):
        openapi_name = param["name"]
        param_name = to_python_ident(openapi_name)
        used_param_names.add(param_name)
        schema = param.get("schema", {"type": "string"})
        param_type = python_type_from_schema(schema, spec)
        flag_name = to_kebab_case(openapi_name)
        full_opt_name = f"--{flag_name}"
        description = param.get("description", "")
        
        # Check for collisions
        if full_opt_name in used_option_names:
            raise ValueError(
                f"Option name collision in {operation_id}: '{full_opt_name}' already used (header param)"
            )
        used_option_names.add(full_opt_name)
        
        required = param.get("required", False)
        if description:
            description_str = python_triple_quoted_str(description)
            if required:
                lines.append(
                    f'    {param_name}: {param_type} = typer.Option(..., "--{flag_name}", help={description_str}),'
                )
            else:
                lines.append(
                    f'    {param_name}: {param_type} | None = typer.Option(None, "--{flag_name}", help={description_str}),'
                )
        else:
            if required:
                lines.append(
                    f'    {param_name}: {param_type} = typer.Option(..., "--{flag_name}"),'
                )
            else:
                lines.append(
                    f'    {param_name}: {param_type} | None = typer.Option(None, "--{flag_name}"),'
                )
    
    # Request body options
    body_flags: list[tuple[list[str], dict[str, Any], bool, str, str]] = []  # (path, schema, required, param_name, opt_name)
    
    if request_body_info:
        content_type, request_body_model, resolved_schema, body_required = request_body_info
        if content_type == "application/json":
            # Keep --json for backward compatibility
            if "--json" in used_option_names:
                raise ValueError(
                    f"Option name collision in {operation_id}: '--json' already used"
                )
            used_option_names.add("--json")
            lines.append(
                '    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),'
            )
            used_param_names.add("json_str")
            
            # Flatten schema and generate dotted flags
            flattened = flatten_schema(resolved_schema, spec)
            for path_parts, leaf_schema, is_required in flattened:
                opt_name = option_name_for_path(path_parts)
                
                # Check for collisions
                if opt_name in used_option_names:
                    raise ValueError(
                        f"Option name collision in {operation_id}: '{opt_name}' already used. "
                        f"Path: {'.'.join(path_parts)}"
                    )
                used_option_names.add(opt_name)
                
                # Generate Python parameter name from path
                base_param_name = "_".join(to_python_ident(part) for part in path_parts)
                param_name = base_param_name

                # Avoid collisions with existing signature args (e.g. `id`)
                if param_name in used_param_names:
                    param_name = f"body_{param_name}"

                # Ensure uniqueness across both existing args and other body args
                counter = 1
                while (
                    param_name in used_param_names
                    or any(existing[3] == param_name for existing in body_flags)
                ):
                    candidate = f"{base_param_name}_{counter}"
                    param_name = (
                        f"body_{candidate}" if candidate in used_param_names else candidate
                    )
                    counter += 1

                used_param_names.add(param_name)
                
                # Determine type
                # leaf_schema is already resolved in flatten_schema, so pass spec=None
                # to avoid re-resolving and handle schemas without explicit type
                param_type = python_type_from_schema(leaf_schema, spec=None)
                is_complex = is_complex_type(leaf_schema, spec)
                description = leaf_schema.get("description", "")
                
                body_flags.append((path_parts, leaf_schema, is_required, param_name, opt_name))
                
                # Emit Typer option
                if description:
                    description_str = python_triple_quoted_str(description)
                    if is_required:
                        if is_complex:
                            lines.append(
                                f'    {param_name}: {param_type} = typer.Option(..., "{opt_name}", help={description_str}),'
                            )
                        else:
                            lines.append(
                                f'    {param_name}: {param_type} = typer.Option(..., "{opt_name}", help={description_str}),'
                            )
                    else:
                        if is_complex:
                            lines.append(
                                f'    {param_name}: {param_type} | None = typer.Option(None, "{opt_name}", help={description_str}),'
                            )
                        else:
                            lines.append(
                                f'    {param_name}: {param_type} | None = typer.Option(None, "{opt_name}", help={description_str}),'
                            )
                else:
                    if is_required:
                        if is_complex:
                            lines.append(
                                f'    {param_name}: {param_type} = typer.Option(..., "{opt_name}", help="JSON string for {".".join(path_parts)}"),'
                            )
                        else:
                            lines.append(
                                f'    {param_name}: {param_type} = typer.Option(..., "{opt_name}"),'
                            )
                    else:
                        if is_complex:
                            lines.append(
                                f'    {param_name}: {param_type} | None = typer.Option(None, "{opt_name}", help="JSON string for {".".join(path_parts)}"),'
                            )
                        else:
                            lines.append(
                                f'    {param_name}: {param_type} | None = typer.Option(None, "{opt_name}"),'
                            )
        elif content_type == "multipart/form-data":
            # Inline JSON for non-file fields
            if "--json" in used_option_names:
                raise ValueError(
                    f"Option name collision in {operation_id}: '--json' already used"
                )
            used_option_names.add("--json")
            lines.append(
                '    json_str: str | None = typer.Option(None, "--json", help="Inline JSON with multipart fields (non-file)"),'
            )
            # Add file-part options for binary fields
            props = (
                resolved_schema.get("properties", {})
                if isinstance(resolved_schema, dict)
                else {}
            )
            required_props = set(resolved_schema.get("required", []) or [])
            for prop_name, prop_schema in sorted(props.items(), key=lambda kv: kv[0]):
                if not isinstance(prop_schema, dict):
                    continue
                if (
                    prop_schema.get("type") == "string"
                    and prop_schema.get("format") == "binary"
                ):
                    arg_name = to_python_ident(prop_name)
                    opt_name = to_kebab_case(prop_name)
                    full_opt_name = f"--{opt_name}"
                    description = prop_schema.get("description", "")
                    
                    # Check for collisions
                    if full_opt_name in used_option_names:
                        raise ValueError(
                            f"Option name collision in {operation_id}: '{full_opt_name}' already used"
                        )
                    used_option_names.add(full_opt_name)
                    
                    if description:
                        description_str = python_triple_quoted_str(description)
                        if prop_name in required_props:
                            lines.append(
                                f'    {arg_name}: Path = typer.Option(..., "--{opt_name}", help={description_str}),'
                            )
                        else:
                            lines.append(
                                f'    {arg_name}: Path | None = typer.Option(None, "--{opt_name}", help={description_str}),'
                            )
                    else:
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
    summary = operation.get("summary", operation_id)
    doc_url = f"https://api.immich.app/endpoints/{inflection.parameterize(tag)}/{operation_id}"
    lines.append(f'    """{summary}\n\nDocs: {doc_url}\n    """')

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
        content_type, request_body_model, resolved_schema, body_required = request_body_info
        if content_type == "application/json":
            body_param_name = to_python_ident(request_body_model)
            model_module = to_snake_case(request_body_model)
            
            # Check mutual exclusion: --json and dotted flags cannot both be used
            if body_flags:
                body_flag_params = [param_name for _, _, _, param_name, _ in body_flags]
                lines.append("    # Check mutual exclusion between --json and dotted flags")
                lines.append(f"    has_json = json_str is not None")
                lines.append(f"    has_flags = any([{', '.join(body_flag_params)}])")
                lines.append("    if has_json and has_flags:")
                lines.append(
                    '        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")'
                )
                
                # Check if body is required but not provided
                if body_required:
                    lines.append("    if not has_json and not has_flags:")
                    lines.append(
                        '        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")'
                    )
            
            # Handle --json path (backward compatibility)
            lines.append("    if json_str is not None:")
            lines.append("        json_data = json.loads(json_str)")
            lines.append(
                f"        from immich.client.models.{model_module} import {request_body_model}"
            )
            lines.append(
                f"        {body_param_name} = deserialize_request_body(json_data, {request_body_model})"
            )
            lines.append(f"        kwargs['{body_param_name}'] = {body_param_name}")
            
            # Handle dotted flags path
            if body_flags:
                lines.append("    elif any([")
                body_flag_params = [param_name for _, _, _, param_name, _ in body_flags]
                lines.append("        " + ",\n        ".join(body_flag_params) + ",")
                lines.append("    ]):")
                lines.append("        # Build body from dotted flags")
                lines.append("        json_data = {}")
                
                for path_parts, leaf_schema, is_required, param_name, opt_name in body_flags:
                    is_complex = is_complex_type(leaf_schema, spec)
                    
                    if is_required:
                        if is_complex:
                            lines.append(f"        if {param_name} is None:")
                            lines.append(
                                f'            raise SystemExit("Error: --{opt_name.lstrip("--")} is required")'
                            )
                            lines.append(f"        value_{param_name} = json.loads({param_name})")
                            lines.append(f"        set_nested(json_data, {path_parts!r}, value_{param_name})")
                        else:
                            lines.append(f"        if {param_name} is None:")
                            lines.append(
                                f'            raise SystemExit("Error: --{opt_name.lstrip("--")} is required")'
                            )
                            lines.append(f"        set_nested(json_data, {path_parts!r}, {param_name})")
                    else:
                        lines.append(f"        if {param_name} is not None:")
                        if is_complex:
                            lines.append(f"            value_{param_name} = json.loads({param_name})")
                            lines.append(f"            set_nested(json_data, {path_parts!r}, value_{param_name})")
                        else:
                            lines.append(f"            set_nested(json_data, {path_parts!r}, {param_name})")
                
                # Validate and create model
                lines.append("        if json_data:")
                lines.append(
                    f"            from immich.client.models.{model_module} import {request_body_model}"
                )
                lines.append(
                    f"            {body_param_name} = deserialize_request_body(json_data, {request_body_model})"
                )
                lines.append(f"            kwargs['{body_param_name}'] = {body_param_name}")
        elif content_type == "multipart/form-data":
            props = (
                resolved_schema.get("properties", {})
                if isinstance(resolved_schema, dict)
                else {}
            )
            required_props = set(resolved_schema.get("required", []) or [])
            lines.append("    json_data = json.loads(json_str) if json_str is not None else {}")
            lines.append("    missing: list[str] = []")
            for prop_name, prop_schema in sorted(props.items(), key=lambda kv: kv[0]):
                if not isinstance(prop_schema, dict):
                    continue
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
                    lines.append(f"        kwargs['{snake}'] = json_data['{prop_name}']")
                    lines.append(f"    elif '{snake}' in json_data:")
                    lines.append(f"        kwargs['{snake}'] = json_data['{snake}']")
                    if prop_name in required_props:
                        lines.append("    else:")
                        lines.append(f"        missing.append('{prop_name}')")
            lines.append("    if missing:")
            lines.append(
                "        raise SystemExit("
                "\"Error: missing required multipart fields: \" + ', '.join(missing) + "
                '". Provide them via --json and/or file options."'
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
    tag_attr = to_snake_case(tag)
    tag_description = next(t for t in spec["tags"] if t["name"] == tag)["description"]
    tag_slug = inflection.parameterize(tag)
    tag_help = f"{tag_description}\n\nDocs: https://api.immich.app/endpoints/{tag_slug}"

    lines = [
        '"""Generated CLI commands for '
        + tag
        + ' tag (auto-generated, do not edit)."""',
        "",
        "from __future__ import annotations",
        "",
        "import json",
        "from pathlib import Path",
        "import typer",
        "",
        "from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested",
        "",
        f"app = typer.Typer(help={python_triple_quoted_str(tag_help)}, context_settings={{'help_option_names': ['-h', '--help']}})",
        "",
    ]

    # Generate command for each operation
    for path, method, operation in sorted(
        operations, key=lambda x: x[2].get("operationId", "")
    ):
        func_code = generate_command_function(operation, spec, tag_attr, tag)
        lines.append(func_code)
        lines.append("")

    return "\n".join(lines)


def generate_init_py(tags: list[str]) -> str:
    """Generate __init__.py with lazy import map for commands."""
    lines = [
        '"""Lazy import map for CLI commands (auto-generated, do not edit)."""',
        "",
        "from __future__ import annotations",
        "",
        "# Lazy import map: module_name -> CLI command name",
        "# Modules are imported lazily in app.py for faster shell completion",
        "_MODULE_MAP: dict[str, str] = {",
    ]

    # Sort tags for consistent output
    for tag in sorted(tags):
        module_name = to_snake_case(tag)
        app_name = to_kebab_case(tag)
        lines.append(f'    "{module_name}": "{app_name}",')

    lines.append("}")

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

    commands_dir = Path(__file__).resolve().parents[2] / "immich" / "cli" / "commands"

    # Fetch OpenAPI spec
    url = openapi_url(args.ref)
    print(f"Fetching OpenAPI spec from: {url}")

    spec = urllib3.request("GET", url).json()

    # Validate and group operations
    operations_by_tag: dict[str, list[tuple[str, str, dict[str, Any]]]] = {}

    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method not in ["get", "post", "put", "patch", "delete"]:
                continue

            # Group by first tag
            tags = operation.get("tags", [])
            tag = tags[0] if tags else "default"
            if tag not in operations_by_tag:
                operations_by_tag[tag] = []
            operations_by_tag[tag].append((path, method, operation))

    # Clean and recreate commands directory
    if commands_dir.exists():
        shutil.rmtree(commands_dir)
    commands_dir.mkdir(parents=True, exist_ok=True)

    # Generate app modules
    for tag in sorted(operations_by_tag.keys()):
        operations = operations_by_tag[tag]
        tag_snake = to_snake_case(tag)
        app_content = generate_tag_app(tag, operations, spec)

        app_file = commands_dir / f"{tag_snake}.py"
        app_file.write_text(app_content, encoding="utf-8")

    # Generate __init__.py with lazy import map
    init_content = generate_init_py(list(operations_by_tag.keys()))
    init_file = commands_dir / "__init__.py"
    init_file.write_text(init_content, encoding="utf-8")

    print(f"Generated CLI commands for {len(operations_by_tag)} tags")


if __name__ == "__main__":
    raise SystemExit(main())

