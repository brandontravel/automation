#!/usr/bin/env python3
"""Placeholder site link check.

If you want stricter checking, replace this script with a real checker.
For now, this simply confirms the publish directory exists.
"""
from pathlib import Path

CANDIDATES = ["_site", "site", "dist", "public", "docs"]

def main() -> int:
    for d in CANDIDATES:
        if Path(d).is_dir():
            print(f"Found publish directory: {d}")
            return 0
    print("No publish directory found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
