# Spatial Skills

Reusable, deterministic geospatial capabilities used by the book agents.

| Skill ID | Purpose |
|---|---|
| `validate-geojson` | Validate FeatureCollections and geometry quality. |
| `transform-crs` | Transform GeoJSON between coordinate reference systems. |
| `spatial-query` | Build safe structured spatial query plans; never raw SQL. |
| `summarize-field-data` | Summarize field records and completion signals. |
| `detect-data-quality-issues` | Detect missing required fields and duplicate IDs. |
| `generate-map-style` | Generate minimal MapLibre style JSON. |

Implementation lives in `skills/core.py`. Each skill is deterministic and independently testable.