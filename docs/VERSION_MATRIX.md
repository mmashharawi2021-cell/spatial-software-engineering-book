# Reference version matrix — 2026-09-12

This matrix records the book's reference environment. Patch versions may advance; the published repository release should be frozen with lockfiles and CI.

| Component | Reference line |
|---|---|
| PostgreSQL | 18.x (18.6 current stable when audited) |
| PostGIS | 3.6.x (3.6.4 current when audited) |
| Docker image | `postgis/postgis:18-3.6` |
| Python | 3.13 for CI; examples should avoid unnecessary version-specific syntax |
| FastAPI | 0.141.x reference line |
| Psycopg | 3.3.x reference line |
| GeoPandas | 1.1.x reference line |
| Shapely | 2.1.x reference line |
| pyproj | 3.7.x reference line |
| GDAL | 3.13.x reference line/documentation |
| MapLibre GL JS | 6.x reference line |
| Node.js | Active supported LTS/current CI line documented in repository |
| GeoJSON | RFC 7946 |
| STAC | 1.1.0 current stable spec at audit time |
| OGC API - Features | OGC API family; implement and test declared conformance classes individually |

## Policy
- In the book prose, prefer stable major/minor families unless behavior depends on a patch.
- In the repository, use lockfiles / frozen release tags for reproduction.
- Re-audit this table immediately before printing and before each new edition.
