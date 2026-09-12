# Clean Checkout Verification — Pre-release

## Purpose
Verify that a reader can obtain the repository from a clean checkout and that the documented stack installs, builds, and tests without relying on hidden local state.

## Authoritative verification path
GitHub Actions is the authoritative clean-checkout test because each hosted runner starts fresh and executes `actions/checkout` before installing dependencies.

The CI workflow verifies:

1. Repository checkout on a fresh runner.
2. Python 3.13 setup.
3. API/Python dependencies installation.
4. Python compile checks.
5. Unit tests including Skills, Agents, and MCP registry checks.
6. GeoJSON validation.
7. GeoPandas ETL.
8. PostgreSQL/PostGIS service startup.
9. Database migration.
10. Seed loading.
11. Spatial database smoke tests.
12. Node setup and Web dependency installation.
13. TypeScript/Vite production build.

## Local sandbox note
A direct `git clone https://github.com/...` was attempted during this audit, but the audit sandbox cannot resolve `github.com` through outbound DNS. This is an execution-environment limitation and is not treated as a repository defect. Repository state and clean-checkout behavior are therefore validated through GitHub Actions.

## Current release gate
A green CI run is necessary but not sufficient for `book-v1.0.0`. The release remains blocked until every manuscript code block is classified as either:

- **Runnable** with an exact repository file and verification method; or
- **Illustrative / Pseudocode** and explicitly labeled as such in the manuscript.

See `docs/CODE_BLOCK_AUDIT.md`.
