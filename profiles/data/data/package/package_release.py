#!/usr/bin/env python3
"""Generic dataset packager.

Creates a zipped release bundle under `data/dist/`.

Usage:
  package_release.py <tag>
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # data/
RAW = ROOT / "raw"
DIST = ROOT / "dist"

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: package_release.py <tag>")
        return 2

    tag = sys.argv[1]
    DIST.mkdir(parents=True, exist_ok=True)

    bundle = DIST / f"data-bundle-{tag}.zip"
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as z:
        if RAW.exists():
            for p in RAW.rglob("*"):
                if p.is_file():
                    z.write(p, p.relative_to(ROOT))
        # include metadata if present
        meta = ROOT / "metadata"
        if meta.exists():
            for p in meta.rglob("*"):
                if p.is_file():
                    z.write(p, p.relative_to(ROOT))

    print(f"Wrote: {bundle}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
