# Technical release checklist

Legend: `[x]` verified, `[ ]` still required before `book-v1.0.0`.

## Code
- [x] Clean checkout succeeds through GitHub Actions fresh hosted runners.
- [x] `python -m compileall -q api python tests skills agents mcp` passes.
- [x] `pytest -q` passes.
- [x] GeoJSON validator returns no errors for valid training data.
- [x] ETL produces the expected feature count and CRS.
- [ ] Replace `npm install` with reproducible `npm ci` and commit a lockfile; then verify `npm ci && npm run build`.
- [ ] Every manuscript code block has a final status in `docs/CODE_BLOCK_AUDIT.md`: Runnable with exact file/test, or explicitly Illustrative/Pseudocode.
- [ ] Dart/Flutter manuscript snippet is compiler-verified or explicitly marked Illustrative.

## Database
- [x] PostGIS service reaches healthy state in CI.
- [x] Migration runs on an empty database.
- [x] Seed runs.
- [x] Spatial smoke tests run.
- [ ] Re-running migration behavior is documented (migrations are versioned, not blindly repeated).
- [ ] Manuscript SQL fragments intended as Runnable examples are individually file-backed/tested.

## API
- [ ] `/health` responds without touching dependencies.
- [ ] `/ready` verifies database readiness.
- [ ] Valid BBOX returns GeoJSON through an integration test.
- [ ] Invalid BBOX returns a controlled 400 response through an integration test.
- [x] CORS policy is explicit in the reference API.
- [ ] Pagination is integration-tested.
- [ ] Negative/security response tests confirm no secrets appear in responses/logs.

## Web
- [x] TypeScript production build passes.
- [ ] Map load is verified in a browser/E2E test.
- [ ] Move-end refresh/cancellation is verified in a browser/E2E test.
- [ ] Production error-state behavior is verified in a browser/E2E test.

## Skills / Agents / MCP-ready layer
- [x] Skills compile and unit tests pass.
- [x] Agents compile and unit tests pass.
- [x] MCP-ready tool registry tests pass.
- [x] Spatial Query Agent does not expose raw SQL generation/execution.
- [ ] Tool input schemas and failure cases have complete negative tests.
- [ ] Any claim of MCP conformance is withheld unless tested against the applicable official conformance expectations.

## Book ↔ repository
- [ ] Every Runnable Example maps to an exact repository file and verification method.
- [ ] Pseudocode/Illustrative blocks are explicitly labelled in the manuscript.
- [ ] Version matrix matches the final CI environment.
- [ ] Book references a frozen tag/release, not only `main`.
- [ ] Commit SHA recorded in the book production notes.
- [ ] QR resolves to the frozen release/tag.

## Licensing
- [x] Original companion code license is present.
- [x] Dataset license is present.
- [x] Third-party notices file is present.
- [ ] Third-party notices are re-audited immediately before release.
- [ ] Any adapted third-party source file retains its required license header/notice.
- [x] No vendor repository is copied wholesale into the current reference repository.

## Release gate
Do **not** create `book-v1.0.0` while any item above that affects reproducibility, code correctness, security, or Book↔Repository traceability remains unchecked.
