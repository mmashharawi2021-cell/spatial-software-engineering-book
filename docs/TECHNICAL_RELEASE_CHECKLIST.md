# Technical release checklist

Legend: `[x]` verified, `[ ]` intentionally deferred until the frozen `book-v1.0.0` release is created.

## Code
- [x] Clean checkout succeeds through GitHub Actions fresh hosted runners.
- [x] `python -m compileall -q api python tests skills agents mcp` passes.
- [x] `pytest -q` passes, including negative tool-contract tests.
- [x] GeoJSON validator returns no errors for valid training data.
- [x] ETL produces the expected feature count and CRS.
- [x] `web/package-lock.json` is committed and `npm ci && npm run build` passes.
- [x] All 60 manuscript code blocks have a canonical status/path in `docs/CODE_BLOCK_MANIFEST.md`.
- [x] All 60 mapped files are checked automatically by `tests/verify_code_block_manifest.py`.
- [x] Dart manuscript snippet is explicitly Illustrative and parser/formatter-verified in CI.

## Database
- [x] PostGIS service reaches healthy state in CI.
- [x] Migration runs on an empty database.
- [x] Seed runs.
- [x] Spatial smoke tests run.
- [x] Manuscript SQL blocks are individually file-backed and mapped in the code-block manifest.
- [x] Migration files are versioned and CI applies them to a fresh database; they are not treated as ad-hoc repeatable scripts.

## API
- [x] `/health` responds without touching dependencies.
- [x] `/ready` verifies database readiness.
- [x] Valid BBOX returns GeoJSON through a real PostGIS integration test.
- [x] Invalid and reversed BBOX values return controlled 400 responses.
- [x] CORS policy is explicit in the reference API.
- [x] Pagination is integration-tested.
- [x] Status filtering is integration-tested.
- [x] Negative-response tests assert that common secret/database markers are not leaked in HTTP response bodies.

## Web
- [x] TypeScript production build passes.
- [x] A committed npm lockfile is used through `npm ci`.
- [x] Map load is verified in Chromium with Playwright.
- [x] Visible-feature loading is verified with a deterministic mocked GeoJSON response.
- [x] Refresh cancellation behavior is verified in browser E2E tests.
- [x] Production API error-state behavior is verified in browser E2E tests.

## Skills / Agents / MCP-ready layer
- [x] Skills compile and unit tests pass.
- [x] Agents compile and unit tests pass.
- [x] MCP-ready tool registry tests pass.
- [x] Unknown tools and invalid argument containers are rejected.
- [x] Excessive spatial-query limits are rejected.
- [x] Spatial Query Agent does not expose raw SQL generation/execution.
- [x] The repository describes this layer as MCP-ready; it does not claim full MCP conformance without a dedicated conformance test.

## Book ↔ repository
- [x] Every one of the 60 manuscript code blocks maps to an exact repository file.
- [x] Runnable vs Illustrative/Pseudocode status is explicit in `docs/CODE_BLOCK_MANIFEST.md`.
- [x] Manuscript v0.5 displays a `CB-###`, status, and repository path immediately before every code block.
- [x] Version matrix matches the current verified CI environment before release freeze.
- [ ] Replace mutable `main` references in final production notes/QR with the frozen `book-v1.0.0` release URL.
- [ ] Record the final release commit SHA in the production notes after the release commit exists.
- [ ] Generate and verify the QR code against the frozen release/tag.

## Licensing
- [x] Original companion code license is present.
- [x] Dataset license is present.
- [x] Third-party notices file is present.
- [x] No vendor repository is copied wholesale into the current reference repository.
- [ ] Perform the final third-party notice/version re-audit immediately before creating `book-v1.0.0`.

## Verified CI gate
The expanded pre-release gate verifies, on a fresh GitHub-hosted runner:

1. Python compilation, unit tests, Skills, Agents, MCP-ready registry, and all 60 code-block mappings.
2. GeoJSON validation and ETL.
3. PostgreSQL/PostGIS startup, migrations, seed, and spatial smoke tests.
4. Live FastAPI integration tests against that PostGIS service, including negative BBOX and response-leak checks.
5. Reproducible web install through `npm ci`, TypeScript/Vite production build, Chromium install, and Playwright E2E tests.
6. Dart parser/formatter verification for the illustrative Flutter/Dart manuscript block.

## Release gate
The engineering/code reproducibility blockers are now closed. The remaining unchecked items are **release-freeze tasks** that cannot be completed until the final repository state and final publication artifact are frozen. Do not create `book-v1.0.0` until the final third-party notice audit is complete and the final manuscript/PDF has been re-rendered and visually reviewed.
