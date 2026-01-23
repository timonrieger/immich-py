#!/usr/bin/env python3
"""Generate API documentation markdown files from client classes."""

from pathlib import Path
import shutil

# Explicit mapping for special cases
SPECIAL_CASES: dict[str, tuple[str, str]] = {
    "api_keys_api": ("APIKeysApi", "API Keys Api"),
    "api_key_create_dto": ("APIKeyCreateDto", "API Key Create Dto"),
    "api_key_create_response_dto": (
        "APIKeyCreateResponseDto",
        "API Key Create Response Dto",
    ),
    "api_key_response_dto": ("APIKeyResponseDto", "API Key Response Dto"),
    "api_key_update_dto": ("APIKeyUpdateDto", "API Key Update Dto"),
    "clip_config": ("CLIPConfig", "CLIP Config"),
    "transcode_hw_accel": ("TranscodeHWAccel", "Transcode HW Accel"),
    "o_auth_callback_dto": ("OAuthCallbackDto", "OAuth Callback Dto"),
    "cq_mode": ("CQMode", "CQ Mode"),
}


def filename_to_title(filename: str) -> str:
    """Convert filename like 'activities_api.py' to 'Activities Api'."""
    name = filename.replace(".py", "")
    if name in SPECIAL_CASES:
        return SPECIAL_CASES[name][1]

    parts = name.split("_")
    return " ".join(part.capitalize() for part in parts)


def filename_to_class_name(filename: str) -> str:
    """Convert filename like 'activities_api.py' to 'ActivitiesApi'.

    Special cases are handled via explicit mapping, otherwise falls back to
    split by underscore, capitalize each part, and join.
    """
    name = filename.replace(".py", "")

    if name in SPECIAL_CASES:
        return SPECIAL_CASES[name][0]

    # Default: split by underscore, capitalize each part, join
    parts = name.split("_")
    return "".join(part.capitalize() for part in parts)


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
) -> int:
    """Process a directory and generate markdown files.

    Returns the number of files generated.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(source_dir.glob(file_pattern))
    files = [f for f in files if not f.name.startswith("__")]

    for source_file in files:
        filename = source_file.name
        module_path = get_module_path(source_file, project_root)

        title = filename_to_title(filename)
        class_name = filename_to_class_name(filename)
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
    shutil.rmtree(docs_ref_dir / "api", ignore_errors=True)
    count = process_directory(
        source_dir=client_dir / "generated" / "api",
        output_dir=docs_ref_dir / "api",
        project_root=project_root,
        file_pattern="*_api.py",
    )
    total_generated += count
    print(f"  {count} API files")

    # 2. generated/models/ -> docs/client/reference/models/
    print("\nProcessing generated/models/...")
    shutil.rmtree(docs_ref_dir / "models", ignore_errors=True)
    count = process_directory(
        source_dir=client_dir / "generated" / "models",
        output_dir=docs_ref_dir / "models",
        project_root=project_root,
        file_pattern="*.py",
    )
    total_generated += count
    print(f"  {count} model files")

    # 3. wrapper/ -> docs/client/reference/api
    print("\nProcessing wrapper/...")
    # don't delete the directory since there might be other custom files
    count = process_directory(
        source_dir=client_dir / "wrapper",
        output_dir=docs_ref_dir / "custom",
        project_root=project_root,
        file_pattern="*.py",
    )
    total_generated += count
    print(f"  {count} wrapper files")

    print(f"\nTotal: {total_generated} documentation files generated")


if __name__ == "__main__":
    main()
