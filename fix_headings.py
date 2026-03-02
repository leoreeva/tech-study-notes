#!/usr/bin/env python3
"""
Script to process .qd files and renumber headings correctly.
Removes existing numbering from headings (##, ###, ####, etc.) and adds new sequential numbering.
"""

import re
import os
from pathlib import Path


def process_file(file_path):
    """Process a single .qd file to renumber headings."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    new_lines = []
    heading_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for line in lines:
        # Match heading lines (##, ###, ####, etc.)
        match = re.match(r"^(#{2,6})\s*(\d+(\.\d+)*\.?)\s+(.*)$", line)
        if match:
            hashes = match.group(1)
            level = len(hashes)
            # Remove the numbering
            heading_text = match.group(4)

            # Increment the appropriate counter
            heading_counter[level] += 1

            # Reset lower-level counters when we encounter a higher-level heading
            if level == 2:
                heading_counter[3] = 0
                heading_counter[4] = 0
                heading_counter[5] = 0
                heading_counter[6] = 0
            elif level == 3:
                heading_counter[4] = 0
                heading_counter[5] = 0
                heading_counter[6] = 0
            elif level == 4:
                heading_counter[5] = 0
                heading_counter[6] = 0
            elif level == 5:
                heading_counter[6] = 0

            # Build the new heading number
            new_number = ""
            if level == 2:
                new_number = f"{heading_counter[2]}."
            elif level == 3:
                new_number = f"{heading_counter[2]}.{heading_counter[3]}."
            elif level == 4:
                new_number = (
                    f"{heading_counter[2]}.{heading_counter[3]}.{heading_counter[4]}."
                )
            elif level == 5:
                new_number = f"{heading_counter[2]}.{heading_counter[3]}.{heading_counter[4]}.{heading_counter[5]}."
            elif level == 6:
                new_number = f"{heading_counter[2]}.{heading_counter[3]}.{heading_counter[4]}.{heading_counter[5]}.{heading_counter[6]}."

            # Reconstruct the line with new numbering
            new_line = f"{hashes} {new_number} {heading_text}"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    # Write the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))


def main():
    """Main function to process all .qd files in the repository."""
    # Find all .qd files in the repository
    qd_files = list(Path(".").rglob("*.qd"))

    print(f"Found {len(qd_files)} .qd files to process")

    for file_path in qd_files:
        print(f"Processing {file_path}")
        process_file(file_path)

    print("All files processed successfully!")


if __name__ == "__main__":
    main()
