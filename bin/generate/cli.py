# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "inflection>=0.5.1,<0.6.0",
#   "pydantic>=2.0.0,<3.0.0",
#   "urllib3>=2.3.0,<3.0.0",
# ]
# ///

from __future__ import annotations

import keyword
import os
import shutil
import urllib3  # pyright: ignore[reportMissingImports]
from pathlib import Path
from typing import Annotated, Any, Literal, Optional, Union
import inflection  # pyright: ignore[reportMissingImports]
from pydantic import AfterValidator, BaseModel, Field


def python_triple_quoted_str(value: str) -> str:
    """Return a Python triple-quoted string literal for generated source code."""
    # Avoid accidental termination of the literal.
    safe = value.replace('"""', '\\"""')
    return f'"""{safe}"""'


class RequestParam(BaseModel):
    oaschema: dict[str, Any] = Field(..., description="The schema of the parameter.")
    location: Literal["body", "query", "header", "path"]
    type: Union[
        Literal[
            "str",
            "int",
            "float",
            "list",
            "dict",
            "Path",
            "bool",
            "datetime",
        ],
        str,
    ] = Field(..., description="The type of the parameter.")
    required: bool = Field(..., description="Whether the parameter is required.")
    name: str = Field(
        ..., description="The name of the parameter. Used to generate the flag name."
    )
    description: Annotated[str, AfterValidator(python_triple_quoted_str)] = Field(
        ..., description="The description of the parameter."
    )
    operation_id: str = Field(..., description="The operation ID.")
    model_name: Optional[str] = Field(None, description="The name of the model.")

    @property
    def flag_name(self) -> str:
        return to_kebab_case(self.name)


def openapi_url(ref: str) -> str:
    """Build OpenAPI spec URL from git ref."""
    return (
        "https://raw.githubusercontent.com/immich-app/immich/"
        f"{ref}/open-api/immich-openapi-specs.json"
    )


def to_snake_case(name: str) -> str:
    """Convert string to snake_case."""
    # first get the underscore in, then slugify with underscores
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
    schema: dict[str, Any],
    spec: dict[str, Any] | None = None,
) -> str:
    """Convert OpenAPI schema to Python type hint."""
    # Extract enum name from $ref BEFORE normalization
    enum_name: str | None = None
    if "$ref" in schema:
        enum_name = schema["$ref"].split("/")[-1]

    nschema = normalize_schema(schema, spec)

    if "enum" in nschema:
        # Return enum name if we extracted it from $ref, otherwise fall back to str
        return enum_name if enum_name else "str"

    schema_type = nschema.get("type")
    if schema_type is None:
        return "str"
    if schema_type == "string":
        if "format" in nschema:
            fmt = nschema["format"]
            if fmt == "uuid":
                return "str"  # UUID as string for CLI
            elif fmt == "date-time":
                return "datetime"  # Typer handles datetime parsing
            elif fmt == "binary":
                return "Path"
        return "str"
    elif schema_type == "integer":
        return "int"
    elif schema_type == "number":
        return "float"
    elif schema_type == "boolean":
        return "bool"
    elif schema_type == "array":
        items = nschema.get("items", {})
        item_type = python_type_from_schema(items, spec)
        return f"list[{item_type}]"
    elif schema_type == "object":
        # Click can't map arbitrary objects; accept JSON as a string.
        return "str"
    return "str"


def resolve_schema_ref(spec: dict[str, Any], ref: str) -> dict[str, Any]:
    """Resolve a local OpenAPI $ref like '#/components/schemas/Foo'."""
    cur: Any = spec
    for part in ref.lstrip("#/").split("/"):
        cur = cur[part]
    return cur


def normalize_schema(
    schema: dict[str, Any], spec: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Normalize a schema for CLI generation.

    Today this focuses on "allOf" by merging object-ish schemas so we can keep
    generating dotted flags instead of collapsing to JSON strings.
    """
    # If we can, resolve refs up-front to expose actual types/properties.
    if "$ref" in schema and spec is not None:
        schema = resolve_schema_ref(spec, schema["$ref"])

    # Merge allOf when possible (common in Immich OpenAPI for composed DTOs).
    if "allOf" in schema and isinstance(schema.get("allOf"), list):
        merged: dict[str, Any] = {k: v for k, v in schema.items() if k != "allOf"}

        for sub in schema.get("allOf", []) or []:
            sub_norm = normalize_schema(sub, spec)
            for k, v in sub_norm.items():
                merged[k] = v

        schema = merged

    return schema


def is_complex_type(schema: dict[str, Any], spec: dict[str, Any] | None = None) -> bool:
    """Check if schema represents a complex type (object, array-of-object, oneOf/anyOf, etc.)."""
    schema = normalize_schema(schema, spec)

    schema_type = schema.get("type")
    if schema_type == "object":
        return True
    if schema_type == "array":
        items = schema.get("items", {})
        if "$ref" in items:
            # Resolve the ref to check if it's an enum/primitive or an object
            if spec is not None:
                resolved = resolve_schema_ref(spec, items["$ref"])
                # Enums and primitives are not complex - only objects are
                if "enum" in resolved:
                    return False  # Array of enums is simple
                # If it's an object or unknown, treat as complex
                return True
        return is_complex_type(items, spec)

    # oneOf, anyOf, allOf are complex
    if any(key in schema for key in ["oneOf", "anyOf", "allOf"]):
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

    schema_type = schema.get("type")

    # Primitive or enum - leaf node
    if (
        schema_type in ("string", "integer", "number", "boolean", "array")
        or "enum" in schema
    ):
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
    return []


def get_request_body_info(
    operation: dict[str, Any], spec: dict[str, Any]
) -> list[RequestParam]:
    """Return list of RequestParam for requestBody."""
    if "requestBody" not in operation:
        return []

    request_body = operation["requestBody"]
    first_media_type = next(iter(request_body["content"].keys()))
    ref: str = request_body["content"][first_media_type]["schema"]["$ref"]
    model_name: str = ref.split("/")[-1]
    resolved_schema = resolve_schema_ref(spec, ref)
    flattened = flatten_schema(resolved_schema, spec)
    params: list[RequestParam] = []
    for path_parts, leaf_schema, is_required in flattened:
        # Generate Python parameter name from path
        param_name = "_".join(to_python_ident(part) for part in path_parts)

        description_parts = []
        description = leaf_schema.get("description")
        if description is not None:
            description_parts.append(description)

        example = leaf_schema.get("example")
        if example is not None:
            description_parts.append(f"Example: {example}")

        is_complex = is_complex_type(leaf_schema, spec)
        if is_complex:
            description_parts.append("As a JSON string")

        description = "\n\n".join(description_parts)

        param = RequestParam(
            oaschema=leaf_schema,
            location="body",
            type=python_type_from_schema(leaf_schema, spec),
            required=is_required,
            name=param_name,
            description=description,
            model_name=model_name,
            operation_id=operation["operationId"],
        )
        params.append(param)
    return params


def generate_command_function(
    operation: dict[str, Any],
    spec: dict[str, Any],
    tag_attr: str,
    tag: str,
) -> str:
    """Generate a Typer command function for an operation.

    Returns:
        Generated function code as a string
    """
    operation_id = operation["operationId"]
    func_name = to_snake_case(operation_id)
    cmd_name = to_kebab_case(operation_id)

    # Extract and process parameters
    param_data: list[RequestParam] = []
    for param in operation.get("parameters", []):
        param_in = param["in"]
        if param_in in ("path", "query", "header"):
            schema = param.get("schema", {"type": "string"})
            param_data.append(
                RequestParam(
                    location=param_in,
                    oaschema=schema,
                    type=python_type_from_schema(schema, spec),
                    required=param.get("required", False),
                    name=to_python_ident(param["name"]),
                    description=param.get("description", "")
                    + schema.get("example", ""),
                    operation_id=operation_id,
                )
            )

    # Get request body info
    body_params = get_request_body_info(operation, spec)
    param_data.extend(body_params)

    # Build function signature
    lines = [
        f'@app.command("{cmd_name}", deprecated={operation.get("deprecated", False)}, rich_help_panel="API commands")'
    ]
    lines.append(f"def {func_name}(")
    lines.append("    ctx: typer.Context,")

    for param in sorted(param_data, key=lambda x: (x.location != "path", x.name)):
        help_arg = f", help={param.description}"
        minimum = param.oaschema.get("minimum")
        maximum = param.oaschema.get("maximum")
        min_arg = f", min={minimum}" if minimum is not None else ""
        max_arg = f", max={maximum}" if maximum is not None else ""
        exists_arg = ", exists=True" if param.type == "Path" else ""
        type_str = param.type if param.required else f"{param.type} | None"
        default_value = "..." if param.required else "None"
        # Only rename non-path params that collide with path params in the same operation
        if param.location != "path" and any(
            param.name == p.name for p in param_data if p.location == "path"
        ):
            param.name = "body_" + param.name
        if param.location == "path":
            lines.append(
                f"    {param.name}: {param.type} = typer.Argument(...{help_arg}{exists_arg}),"
            )
        else:
            # use tri-state boolean for optional, but regular boolean for required
            # The server distinguishes between true/false/null, but we can't represent that in Python, thus we use a literal type.
            if param.type == "bool" and not param.required:
                type_str = "Literal['true', 'false'] | None"
            lines.append(
                f'    {param.name}: {type_str} = typer.Option({default_value}, "--{param.flag_name}"{help_arg}{min_arg}{max_arg}{exists_arg}),'
            )

    lines.append(") -> None:  # pragma: no cover")

    # Function body
    summary = operation.get("summary", operation_id)
    doc_url = f"https://api.immich.app/endpoints/{inflection.parameterize(tag)}/{operation_id}"
    lines.append(f'    """{summary}\n\n     Docs: {doc_url}\n    """')

    # Build kwargs
    lines.append("    kwargs = {}")
    if any(param.location == "body" for param in param_data):
        lines.append("    json_data = {}")

    # Add all params to kwargs
    for idx, param in enumerate(param_data):
        if param.location == "path":
            # Path params are always required and added directly
            lines.append(f"    kwargs['{param.name}'] = {param.name}")
        elif param.location == "query":
            # Convert boolean query params from string "true"/"false" to actual booleans
            if param.type == "bool" and not param.required:
                lines.append(f"    if {param.name} is not None:")
                lines.append(
                    f"        kwargs['{param.name}'] = {param.name}.lower() == 'true'"
                )
            else:
                if param.required:
                    lines.append(f"    kwargs['{param.name}'] = {param.name}")
                else:
                    lines.append(f"    if {param.name} is not None:")
                    lines.append(f"         kwargs['{param.name}'] = {param.name}")
        elif param.location == "header":  # header
            # Header params are always optional
            lines.append(f"    if {param.name} is not None:")
            lines.append(f"         kwargs['{param.name}'] = {param.name}")

        elif param.location == "body":
            if param.required:
                if is_complex_type(param.oaschema, spec):
                    lines.append(
                        f"    value_{param.name} = [json.loads(i) for i in {param.name}]"
                    )
                    lines.append(
                        f"    set_nested(json_data, [{param.name!r}], value_{param.name})"
                    )
                else:
                    if param.type == "bool" and not param.required:
                        lines.append(
                            f"    set_nested(json_data, [{param.name!r}], {param.name}.lower() == 'true')"
                        )
                    elif param.type == "Path":
                        lines.append(
                            f"    kwargs['{param.name}'] = ({param.name}.name, {param.name}.read_bytes())"
                        )
                    else:
                        lines.append(
                            f"    set_nested(json_data, [{param.name!r}], {param.name})"
                        )
            else:
                lines.append(f"    if {param.name} is not None:")
                if is_complex_type(param.oaschema, spec):
                    lines.append(
                        f"        value_{param.name} = [json.loads(i) for i in {param.name}]"
                    )
                    lines.append(
                        f"        set_nested(json_data, [{param.name!r}], value_{param.name})"
                    )
                else:
                    if param.type == "bool" and not param.required:
                        lines.append(
                            f"        set_nested(json_data, [{param.name!r}], {param.name}.lower() == 'true')"
                        )
                    elif param.type == "Path":
                        lines.append(
                            f"        set_nested(json_data, [{param.name!r}], ({param.name}.name, {param.name}.read_bytes()))"
                        )
                    else:
                        lines.append(
                            f"        set_nested(json_data, [{param.name!r}], {param.name})"
                        )
            if idx == len(param_data) - 1:
                # Validate and create model
                model_instance = to_snake_case(param.model_name)  # type: ignore[invalid-argument-type]
                lines.append(
                    f"    {model_instance} = {param.model_name}.model_validate(json_data)"
                )
                lines.append(f"    kwargs['{model_instance}'] = {model_instance}")
    # Get client and API group
    lines.append("    client: 'AsyncClient' = ctx.obj['client']")

    # Call method
    method_name = to_snake_case(operation_id)
    lines.append(
        f"    result = run_command(client, client.{tag_attr}, '{method_name}', ctx, **kwargs)"
    )

    # Print result
    lines.append("    print_response(result, ctx)")

    return "\n".join(lines)


def generate_tag_app(
    tag: str, operations: list[tuple[str, str, dict[str, Any]]], spec: dict[str, Any]
) -> str:
    """Generate a Typer app module for a tag."""
    tag_attr = to_snake_case(tag)
    tag_description = next(t for t in spec["tags"] if t["name"] == tag)["description"]
    tag_slug = inflection.parameterize(tag)
    tag_help = (
        f"{tag_description}\\n\\nDocs: https://api.immich.app/endpoints/{tag_slug}"
    )

    lines = [
        '"""Generated CLI commands for '
        + tag
        + ' tag (auto-generated, do not edit)."""',
        "",
        "from __future__ import annotations",
        "",
        "import typer",
        "import json",
        "from datetime import datetime",
        "from pathlib import Path",
        "from typing import Literal, TYPE_CHECKING",
        "if TYPE_CHECKING:",
        "    from immich import AsyncClient",
        "",
        "from immich.cli.runtime import print_response, run_command, set_nested",
        "from immich.client.generated.models import *",
        "",
    ]

    # Generate command for each operation
    command_codes: list[str] = []
    for path, method, operation in sorted(
        operations, key=lambda x: x[2].get("operationId", "")
    ):
        func_code = generate_command_function(operation, spec, tag_attr, tag)
        command_codes.append(func_code)

    lines.append(f"app = typer.Typer(help={python_triple_quoted_str(tag_help)})")
    lines.append("")

    # Add command functions
    for func_code in command_codes:
        lines.append(func_code)
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    """Main codegen entrypoint."""
    commands_dir = Path(__file__).resolve().parents[2] / "immich" / "cli" / "commands"

    # Fetch OpenAPI spec
    url = openapi_url(os.environ.get("IMMICH_OPENAPI_REF", "main"))
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

    print(f"Generated CLI commands for {len(operations_by_tag)} tags")


if __name__ == "__main__":
    raise SystemExit(main())
