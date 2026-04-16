from pathlib import Path
import shutil

# Source root
root = Path("output/Tech-Study-Notes")
media_dir = root / "media"

# Supported image extensions
image_extensions = {
    ".jpg", ".jpeg", ".png", ".gif", ".bmp",
    ".tif", ".tiff", ".webp", ".svg"
}

# Create media folder if it does not exist
media_dir.mkdir(parents=True, exist_ok=True)

# First pass: copy images to media and remove originals
for file_path in root.rglob("*"):
    if not file_path.is_file():
        continue

    # Skip files already inside media
    if media_dir in file_path.parents:
        continue

    if file_path.suffix.lower() in image_extensions:
        destination = media_dir / file_path.name

        # Avoid overwriting files with the same name
        if destination.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            counter = 1
            while destination.exists():
                destination = media_dir / f"{stem}_{counter}{suffix}"
                counter += 1

        shutil.copy2(file_path, destination)
        print(f"Copied: {file_path} -> {destination}")

        # Remove original image after successful copy
        file_path.unlink()
        print(f"Deleted original: {file_path}")

# Second pass: remove empty folders, deepest first
for dir_path in sorted(root.rglob("*"), key=lambda p: len(p.parts), reverse=True):
    if not dir_path.is_dir():
        continue

    # Never remove the root folder or media folder
    if dir_path == root or dir_path == media_dir:
        continue

    try:
        next(dir_path.iterdir())
    except StopIteration:
        dir_path.rmdir()
        print(f"Removed empty folder: {dir_path}")

print("Done.")
