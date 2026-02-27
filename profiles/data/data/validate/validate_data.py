#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # data/
RAW = ROOT / "raw"

def main() -> int:
    if not RAW.exists():
        print("No data/raw directory found. Create data/raw/ or update this script.")
        return 0

    files = [p for p in RAW.rglob("*") if p.is_file()]
    if not files:
        print("No files in data/raw. Nothing to validate.")
        return 0

    empty = [p for p in files if p.stat().st_size == 0]
    if empty:
        print("Empty files detected:")
        for p in empty:
            print(" -", p)
        return 1

    print(f"Validated {len(files)} files (basic checks).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
