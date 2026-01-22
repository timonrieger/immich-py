#!/usr/bin/env python3
"""Generate API documentation markdown files from client classes."""

from pathlib import Path


def filename_to_title(filename: str) -> str:
    """Convert filename like 'activities_api.py' to 'Activities Api'."""
    name = filename.replace(".py", "")
    parts = name.split("_")
    return " ".join(part.capitalize() for part in parts)


def filename_to_class_name(filename: str) -> str:
    """Convert filename like 'activities_api.py' to 'ActivitiesApi'.

    Special cases:
    - 'api_keys_api.py' -> 'APIKeysApi' (API at start is uppercase)
    - 'clip_config.py' -> 'CLIPConfig' (CLIP at start is uppercase)
    - 'transcode_hw_accel.py' -> 'TranscodeHWAccel' (HW is uppercase)
    - 'o_auth_callback_dto.py' -> 'OAuthCallbackDto'
    """
    name = filename.replace(".py", "")
    parts = name.split("_")

    # Handle special case: "o_auth" -> "OAuth"
    if len(parts) >= 2 and parts[0] == "o" and parts[1] == "auth":
        return "OAuth" + "".join(part.capitalize() for part in parts[2:])

    # Acronyms that should always be uppercase (anywhere in the name)
    always_uppercase = {"hw"}

    # Acronyms that should be uppercase only at the start
    uppercase_at_start = {"api", "clip"}

    result_parts = []
    for i, part in enumerate(parts):
        if part in always_uppercase:
            result_parts.append(part.upper())
        elif i == 0 and part in uppercase_at_start:
            result_parts.append(part.upper())
        else:
            result_parts.append(part.capitalize())

    return "".join(result_parts)


def get_module_path(file_path: Path, project_root: Path) -> str:
    """Convert file path to Python module path."""
    rel_path = file_path.relative_to(project_root)
    module_path = str(rel_path).replace("/", ".").replace(".py", "")
    return module_path


def generate_markdown_content(title: str, module_path: str, class_name: str) -> str:
    """Generate markdown content for a class."""
    return f"""# {title}

::: {module_path}.{class_name}
"""


def process_directory(
    source_dir: Path,
    output_dir: Path,
    project_root: Path,
    file_pattern: str,
    title_prefix: str = "",
) -> int:
    """Process a directory and generate markdown files.

    Returns the number of files generated.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(source_dir.glob(file_pattern))
    files = [f for f in files if not f.name.startswith("__")]

    for source_file in files:
        filename = source_file.name
        class_name = filename_to_class_name(filename)
        module_path = get_module_path(source_file, project_root)

        title = filename_to_title(filename)
        if title_prefix:
            title = f"{title_prefix}: {title}"

        content = generate_markdown_content(title, module_path, class_name)

        output_file = output_dir / filename.replace(".py", ".md")
        output_file.write_text(content)
        print(f"  Generated: {output_file.relative_to(project_root)}")

    return len(files)


def main():
    """Generate markdown files for all client classes."""
    project_root = Path(__file__).parent.parent.parent
    client_dir = project_root / "immich" / "client"
    docs_ref_dir = project_root / "docs" / "client" / "reference"

    total_generated = 0

    # 1. generated/api/ -> docs/client/reference/api/
    print("\nProcessing generated/api/...")
    count = process_directory(
        source_dir=client_dir / "generated" / "api",
        output_dir=docs_ref_dir / "api",
        project_root=project_root,
        file_pattern="*_api.py",
    )
    total_generated += count
    print(f"  {count} API files")

    # # 2. generated/models/ -> docs/client/reference/models/
    # print("\nProcessing generated/models/...")
    # count = process_directory(
    #     source_dir=client_dir / "generated" / "models",
    #     output_dir=docs_ref_dir / "models",
    #     project_root=project_root,
    #     file_pattern="*.py",
    # )
    # total_generated += count
    # print(f"  {count} model files")

    # 3. wrapper/ -> docs/client/reference/wrapper/
    print("\nProcessing wrapper/...")
    count = process_directory(
        source_dir=client_dir / "wrapper",
        output_dir=docs_ref_dir / "wrapper",
        project_root=project_root,
        file_pattern="*.py",
    )
    total_generated += count
    print(f"  {count} wrapper files")

    print(f"\nTotal: {total_generated} documentation files generated")


if __name__ == "__main__":
    main()
