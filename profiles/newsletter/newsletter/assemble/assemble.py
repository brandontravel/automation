#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # newsletter/
modules_dir = ROOT / "modules"
out_dir = ROOT / "dist"
out_file = out_dir / "issue.md"

out_dir.mkdir(parents=True, exist_ok=True)

parts = []
for f in sorted(modules_dir.glob("*.md")):
    parts.append(f.read_text(encoding="utf-8").rstrip())

out_file.write_text("\n\n".join(parts).strip() + "\n", encoding="utf-8")
print(f"Wrote: {out_file}")
