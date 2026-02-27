# Automation (Core + Profiles)

This repository is a **modular automation template** you can copy into any GitHub organization as an `automation` repo.

It is intentionally **generic**:
- No assumptions about Jekyll/Hugo/Node/etc.
- Workflows look for `build.sh` / `build.py` scripts you can drop in later.
- Scripts are dependency-light and meant to be reviewed by humans before anything is published.

## How to use (fast)
1. Copy this repo into the org as **`automation`**.
2. Keep `core/` always.
3. Pick the profile(s) you need from `profiles/` and delete the rest.
4. To actually run GitHub Actions:
   - Copy the workflow YAMLs you want into the **repo root**: `.github/workflows/`
   - GitHub Actions only runs workflows from that path.

## What’s included

### `core/` (baseline)
- Repo health checks (low-assumption)
- Markdown link checks (best-effort)
- Ops docs and env/secrets examples
- Shared helper scripts
- Social posting templates

### `profiles/` (drop-in modules)
- `newsletter/` — assemble newsletter drafts from modular parts
- `data/` — validate + package datasets, draft releases
- `research/` — build research artifacts (PDF pipeline placeholder) + release support
- `website/` — deploy + check static sites (generic Pages deploy)

## Convention
- `automation` is the **source-of-truth library**.
- Each project repo is the **execution layer**:
  - copy the workflows you need into that repo’s `.github/workflows/`
  - keep repo-specific config local to the repo.

