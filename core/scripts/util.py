#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

def project_root(start: Path | None = None) -> Path:
    p = (start or Path.cwd()).resolve()
    for _ in range(20):
        if (p / ".git").exists() or (p / "README.md").exists():
            return p
        if p.parent == p:
            break
        p = p.parent
    return Path.cwd().resolve()
