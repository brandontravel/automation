#!/usr/bin/env python3
"""Very small link linter for assembled issues.

- Extracts http(s) URLs from the built issue file and checks format only.
- Keep it dependency-free; network checks belong in CI curl steps.
"""
import re
import sys
from pathlib import Path

URL_RE = re.compile(r"https?://[^\s\)\]">]+")

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: lint_links.py <path-to-issue.md>")
        return 2

    p = Path(sys.argv[1])
    text = p.read_text(encoding="utf-8", errors="ignore")
    urls = [u.rstrip(".,;:!?)\"]'") for u in URL_RE.findall(text)]
    bad = [u for u in urls if " " in u or u.endswith("..")]

    print(f"Found {len(urls)} URLs")
    if bad:
        print("Bad-looking URLs:")
        for u in bad:
            print(" -", u)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
