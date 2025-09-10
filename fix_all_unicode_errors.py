#!/usr/bin/env python3
"""
Fix all UnicodeDecodeError issues in YAML files based on yamllint traceback
"""

import glob
import os
from typing import Dict, List


def fix_unicode_in_file(file_path: str) -> bool:
    """Fix all Unicode issues in a specific file by removing non-ASCII bytes"""

    print(f"Checking file: {file_path}")

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False

    # Read as bytes
    with open(file_path, "rb") as f:
        content = f.read()

    print(f"File size: {len(content)} bytes")

    # Find all non-ASCII bytes (bytes > 127)
    problematic_bytes: Dict[int, List[int]] = {}
    for i, byte in enumerate(content):
        if byte > 127:  # Non-ASCII byte
            if byte not in problematic_bytes:
                problematic_bytes[byte] = []
            problematic_bytes[byte].append(i)

    if not problematic_bytes:
        print(f"No non-ASCII bytes found in {file_path}")
        return True

    print("Found problematic bytes:")
    total_positions = 0
    for byte_val, positions in problematic_bytes.items():
        char_repr = chr(byte_val) if 32 <= byte_val <= 126 else "non-printable"
        pos_preview = f"{positions[:5]}{'...' if len(positions) > 5 else ''}"
        print(
            f"  0x{byte_val:02x} ({char_repr}): {len(positions)} instances "
            f"at positions {pos_preview}"
        )
        total_positions += len(positions)

    # Remove all non-ASCII bytes
    new_content = bytes([b for b in content if b <= 127])

    print(f"New size: {len(new_content)} bytes")
    print(f"Removed {len(content) - len(new_content)} bytes")

    # Write back
    with open(file_path, "wb") as f:
        f.write(new_content)

    print(f"Fixed {file_path}")

    # Test if it can be read with cp1252
    try:
        with open(file_path, "r", encoding="cp1252") as f:
            f.read(1000)  # Read first 1000 chars to test
        print("✓ File can now be read with cp1252 encoding")
        return True
    except UnicodeDecodeError as e:
        print(f"✗ Still has cp1252 issues: {e}")
        return False


def main() -> None:
    """Main function to fix all YAML files"""

    # Pattern to find all YAML files
    yaml_files = [
        ".github/workflows/*.yml",
        ".github/dependabot.yml",
        ".pre-commit-config.yaml",
        ".yamllint",
    ]

    all_files = []
    for pattern in yaml_files:
        all_files.extend(glob.glob(pattern))

    print(f"Found {len(all_files)} YAML files to check")

    fixed_count = 0
    error_count = 0

    for file_path in all_files:
        try:
            if fix_unicode_in_file(file_path):
                fixed_count += 1
            else:
                error_count += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            error_count += 1

    print("\nResults:")
    print(f"✓ Successfully processed: {fixed_count} files")
    print(f"✗ Errors: {error_count} files")

    if error_count == 0:
        print("\n🎉 All YAML files should now be readable by yamllint!")
    else:
        print(f"\n⚠️  {error_count} files still have issues.")


if __name__ == "__main__":
    main()
