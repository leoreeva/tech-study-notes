#!/usr/bin/env python3
from pathlib import Path


def update_index_file(index_file: Path, subfolder_name: str) -> bool:
    old = '<img src="media/'
    new = f'<img src="{subfolder_name}/media/'

    content = index_file.read_text(encoding="utf-8")
    updated = content.replace(old, new)

    if updated != content:
        index_file.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    base_dir = Path("output") / "Tech-Study-Notes"

    if not base_dir.is_dir():
        raise FileNotFoundError(f"Folder not found: {base_dir.resolve()}")

    changed = 0
    checked = 0

    for subfolder in base_dir.iterdir():
        if not subfolder.is_dir():
            continue

        index_file = subfolder / "index.html"
        if not index_file.is_file():
            continue

        checked += 1
        if update_index_file(index_file, subfolder.name):
            changed += 1
            print(f"Updated: {index_file}")
        else:
            print(f"No change: {index_file}")

    print(f"\nChecked {checked} index.html file(s), updated {changed}.")


if __name__ == "__main__":
    main()
