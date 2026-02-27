# Secrets (examples)

Only add secrets if a workflow truly requires them.

Common patterns:
- `GH_PAT` — Personal Access Token if you need cross-repo operations (avoid unless needed)
- `DEPLOY_TOKEN` — Deploy key/token for external hosting
- `API_KEY_*` — Third-party integrations (avoid committing; use GitHub Actions secrets)

For most orgs, you can keep automation **secret-free**.
