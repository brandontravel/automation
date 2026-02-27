#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MODULES_DIR="$ROOT/modules"
OUT_DIR="$ROOT/dist"
OUT_FILE="$OUT_DIR/issue.md"

mkdir -p "$OUT_DIR"
: > "$OUT_FILE"

for f in "$MODULES_DIR"/*.md; do
  [ -f "$f" ] || continue
  cat "$f" >> "$OUT_FILE"
  printf "\n\n" >> "$OUT_FILE"
done

echo "Wrote: $OUT_FILE"
