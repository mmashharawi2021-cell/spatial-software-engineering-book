# Technical review checklist

- Confirm every spatial result has explicit CRS/unit assumptions.
- Validate geometries before analysis and import.
- Run migrations from a clean database.
- Test BBOX/search boundary cases.
- Test offline conflicts and retry/idempotency behavior.
- Verify security/authorization at API and data levels.
- Profile queries before and after indexes/tiles/cache.
- Record model/data version for every GeoAI output.
- Reproduce all runnable examples from a clean environment.
