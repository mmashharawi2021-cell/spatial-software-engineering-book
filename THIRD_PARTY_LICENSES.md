# Third-party software, tools, and standards

**Final pre-release audit date:** 2026-09-12

This companion repository depends on, tests with, or references third-party software and standards. It does **not** relicense those projects, and no upstream vendor repository is copied wholesale into this repository.

The repository's original companion code is licensed separately under `LICENSE-CODE`. Synthetic training data is licensed separately under `DATA_LICENSE.md`. Third-party software remains under its upstream license.

## Runtime / build / test dependencies

| Project | Role in this repository | Upstream-declared license | Upstream / authority |
|---|---|---|---|
| PostgreSQL | Database foundation | PostgreSQL License | https://www.postgresql.org/about/licence/ |
| PostGIS | Spatial database extension | GNU GPL v2 | https://postgis.net/ |
| FastAPI | Reference REST API | MIT | https://github.com/fastapi/fastapi |
| Uvicorn | ASGI server used by the API example/CI | BSD-3-Clause | https://github.com/encode/uvicorn |
| Psycopg 3 | PostgreSQL connectivity | LGPL-3.0-only | https://www.psycopg.org/psycopg3/ |
| Pydantic | API validation/model layer | MIT | https://github.com/pydantic/pydantic |
| GeoPandas | Geospatial ETL/test tooling | BSD-3-Clause | https://github.com/geopandas/geopandas |
| Shapely | Geometry operations | BSD-3-Clause | https://github.com/shapely/shapely |
| pyproj | CRS/transformation tooling | MIT | https://github.com/pyproj4/pyproj |
| PROJ | Coordinate transformation engine/reference | MIT / X-MIT style | https://proj.org/ |
| GDAL | Raster/vector tooling reference | MIT-style | https://gdal.org/ |
| MapLibre GL JS | Browser map rendering | BSD-3-Clause | https://github.com/maplibre/maplibre-gl-js |
| Vite | Web build tooling | MIT | https://github.com/vitejs/vite |
| TypeScript | Web language/toolchain | Apache-2.0 | https://github.com/microsoft/TypeScript |
| Playwright | Browser E2E tests | Apache-2.0 | https://github.com/microsoft/playwright |
| @types/geojson / DefinitelyTyped | TypeScript GeoJSON types | MIT | https://github.com/DefinitelyTyped/DefinitelyTyped |

`web/package-lock.json` pins the web dependency graph used for the verified release workflow. The lockfile records dependency versions and integrity metadata; it does not change any dependency's upstream license.

The Python API file `api/requirements.txt` intentionally declares narrow runtime version ranges. CI verifies the supported environment on fresh GitHub-hosted runners; downstream redistributors remain responsible for preserving notices required by the exact dependency versions they package.

## Referenced standards and guidance

The following are cited or used as technical guidance. They are not copied into this repository as third-party source code.

| Standard / guidance | Authority | Use in this repository |
|---|---|---|
| OGC API - Features | Open Geospatial Consortium | API design and BBOX semantics guidance |
| GeoJSON RFC 7946 | IETF | GeoJSON interoperability guidance |
| STAC | STAC community / Radiant Earth ecosystem | Catalog metadata references |
| OpenAPI Specification | OpenAPI Initiative | API contract references |
| OWASP API Security Top 10 | OWASP Foundation | Security review guidance |
| Model Context Protocol (MCP) Specification | MCP project | Tool/resource integration architecture reference |

Standards documents and trademarks remain subject to the terms of their respective publishers. Linking to or implementing a standard does not transfer ownership or imply certification/conformance.

## Distribution rule

Before copying or adapting any third-party source file into this repository:

1. verify the license of that exact upstream file/version;
2. preserve required copyright, license, and NOTICE text;
3. record the source and version next to the adapted material;
4. do not represent third-party work as authored by the book author; and
5. do not claim standards conformance unless a dedicated conformance test supports that claim.

This file is a project notice and engineering audit record, not legal advice.
