# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "rtoml"
# ]
# ///

"""Append model files to the Models list in zensical.toml."""

from pathlib import Path
import re

import rtoml


def get_existing_models(zensical_path: Path) -> set[str]:
    """Get existing model files from zensical.toml."""
    data = rtoml.load(zensical_path)

    if "project" not in data:
        raise ValueError("No 'project' section found in zensical.toml")

    if "nav" not in data["project"]:
        raise ValueError("No 'nav' key found in zensical.toml")

    nav = data["project"]["nav"]

    # Find Models section
    for item in nav:
        if isinstance(item, dict) and "Client" in item:
            client_section = item["Client"]
            if isinstance(client_section, list):
                for client_item in client_section:
                    if isinstance(client_item, dict) and "Reference" in client_item:
                        ref_section = client_item["Reference"]
                        if isinstance(ref_section, list):
                            for ref_item in ref_section:
                                if isinstance(ref_item, dict) and "Models" in ref_item:
                                    models_list = ref_item["Models"]
                                    if isinstance(models_list, list):
                                        return set(models_list)
    return set()


def append_models(zensical_path: Path, model_files: list[str]) -> None:
    """Append model files to the Models list in zensical.toml using text manipulation."""
    content = zensical_path.read_text()

    # Get existing files to avoid duplicates
    existing_files = get_existing_models(zensical_path)

    # Filter out files that already exist
    new_files = [f for f in model_files if f not in existing_files]

    if not new_files:
        print("All model files already exist in zensical.toml")
        return

    # Find the Models section and the closing bracket
    # Pattern: { Models = [ ... ] },
    pattern = r"(\{\s*Models\s*=\s*\[)(.*?)(\]\s*\},)"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        raise ValueError("Could not find Models section in zensical.toml")

    start, existing_content, end = match.groups()

    # Extract existing entries from the content
    existing_entries = []
    for line in existing_content.strip().split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            # Remove quotes and comma
            entry = line.rstrip(",").strip().strip('"').strip("'")
            if entry:
                existing_entries.append(entry)

    # Combine existing and new entries, sorted
    all_entries = sorted(set(existing_entries + new_files))

    # Build the new content
    indent = " " * 16  # Match the indentation level
    new_content = start + "\n"
    for entry in all_entries:
        new_content += f'{indent}"{entry}",\n'
    new_content += indent.rstrip() + end

    # Replace in the original content
    new_file_content = content[: match.start()] + new_content + content[match.end() :]

    # Write back to file
    zensical_path.write_text(new_file_content)


def discover_model_files(project_root: Path) -> list[str]:
    """Discover all model markdown files in docs/client/reference/models/."""
    models_dir = project_root / "docs" / "client" / "reference" / "models"

    if not models_dir.exists():
        return []

    model_files = []
    for md_file in sorted(models_dir.glob("*.md")):
        # Prepend the path relative to docs_dir
        relative_path = f"client/reference/models/{md_file.name}"
        model_files.append(relative_path)

    return model_files


def main():
    """Main entry point."""
    project_root = Path(__file__).parent.parent.parent
    zensical_path = project_root / "zensical.toml"

    # Auto-discover model files
    model_files = discover_model_files(project_root)

    if not model_files:
        print("No model files found in docs/client/reference/models/")
        return

    append_models(zensical_path, model_files)

    print(f"Appended {len(model_files)} model file(s) to zensical.toml")


if __name__ == "__main__":
    main()
