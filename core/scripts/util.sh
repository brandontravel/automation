#!/usr/bin/env bash
set -euo pipefail

say() { printf "%s\n" "$*"; }
die() { printf "ERROR: %s\n" "$*" >&2; exit 1; }
