# transform-crs
Transforms valid GeoJSON geometries from a declared source CRS to a target CRS using `pyproj` + `shapely`.

Implementation: `skills.core.transform_geojson_crs`.

Default target: `EPSG:4326`. The skill refuses invalid GeoJSON before transformation.