# Technical release checklist

## Code
- [ ] Clean checkout succeeds.
- [ ] `python -m compileall -q api python tests` passes.
- [ ] `pytest -q` passes.
- [ ] GeoJSON validator returns no errors for valid training data.
- [ ] ETL produces the expected feature count and CRS.
- [ ] `npm ci && npm run build` passes with a committed lockfile.

## Database
- [ ] PostGIS service reaches healthy state.
- [ ] Migration runs on an empty database.
- [ ] Seed runs.
- [ ] Spatial smoke tests run.
- [ ] Re-running migration behavior is documented (migrations are versioned, not blindly repeated).

## API
- [ ] `/health` responds without touching dependencies.
- [ ] `/ready` verifies database readiness.
- [ ] Valid BBOX returns GeoJSON.
- [ ] Invalid BBOX returns a controlled 400 response.
- [ ] CORS policy is explicit.
- [ ] Pagination is tested.
- [ ] No secrets appear in responses/logs.

## Web
- [ ] TypeScript build passes.
- [ ] Map loads.
- [ ] Move-end refresh is cancellable.
- [ ] Errors are surfaced to the user in the production example.

## Book ↔ repository
- [ ] Every Runnable Example maps to a repository path/test.
- [ ] Pseudocode is explicitly labelled.
- [ ] Version matrix matches the final CI environment.
- [ ] Book references a frozen tag/release, not only `main`.
- [ ] Commit SHA recorded in the book production notes.
- [ ] QR resolves to the frozen release/tag.

## Licensing
- [ ] Original companion code license is present.
- [ ] Dataset license is present.
- [ ] Third-party notices are complete.
- [ ] Any adapted third-party source file retains its required license header/notice.
- [ ] No vendor repository is copied wholesale without explicit license review.
