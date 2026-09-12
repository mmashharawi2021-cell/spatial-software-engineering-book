# validate-geojson
Validates GeoJSON FeatureCollections, duplicate IDs, parseable geometries, empties, and topology validity.

Implementation: `skills.core.validate_geojson`.

Input: GeoJSON object. Output: `{valid, errors, warnings, feature_count}`.