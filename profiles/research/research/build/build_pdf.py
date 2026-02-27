#!/usr/bin/env python3
"""PDF build placeholder.

Implement your preferred pipeline here.
Write outputs to: research/dist/ (or profiles/research/research/dist/).
"""
from pathlib import Path

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    dist = root / "dist"
    dist.mkdir(parents=True, exist_ok=True)
    (dist / "README.txt").write_text(
        "This is a placeholder build output. Implement build_pdf.py to generate PDFs.\n",
        encoding="utf-8",
    )
    print(f"Wrote placeholder to: {dist}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
