from __future__ import annotations

from collections import Counter
from copy import deepcopy
from typing import Any, Iterable

from pyproj import Transformer
from shapely.geometry import mapping, shape

_ALLOWED_OPERATORS = {"eq", "neq", "gt", "gte", "lt", "lte", "in"}


def validate_geojson(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if data.get("type") != "FeatureCollection":
        errors.append("Root object must be a GeoJSON FeatureCollection.")
        return {"valid": False, "errors": errors, "warnings": warnings, "feature_count": 0}

    features = data.get("features")
    if not isinstance(features, list):
        errors.append("FeatureCollection.features must be a list.")
        return {"valid": False, "errors": errors, "warnings": warnings, "feature_count": 0}

    seen_ids: set[str] = set()
    for index, feature in enumerate(features):
        if not isinstance(feature, dict) or feature.get("type") != "Feature":
            errors.append(f"Feature {index} is not a valid GeoJSON Feature.")
            continue
        feature_id = feature.get("id")
        if feature_id is not None:
            sid = str(feature_id)
            if sid in seen_ids:
                errors.append(f"Duplicate feature id: {sid}")
            seen_ids.add(sid)
        geometry = feature.get("geometry")
        if geometry is None:
            warnings.append(f"Feature {index} has null geometry.")
            continue
        try:
            geom = shape(geometry)
        except Exception as exc:  # defensive validation boundary
            errors.append(f"Feature {index} geometry cannot be parsed: {exc}")
            continue
        if geom.is_empty:
            errors.append(f"Feature {index} geometry is empty.")
        if not geom.is_valid:
            errors.append(f"Feature {index} geometry is topologically invalid.")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "feature_count": len(features),
    }


def transform_geojson_crs(
    data: dict[str, Any],
    source_crs: str,
    target_crs: str = "EPSG:4326",
) -> dict[str, Any]:
    validation = validate_geojson(data)
    if not validation["valid"]:
        raise ValueError("Input GeoJSON must be valid before CRS transformation.")

    transformer = Transformer.from_crs(source_crs, target_crs, always_xy=True)
    output = deepcopy(data)
    for feature in output["features"]:
        if feature.get("geometry") is None:
            continue
        geom = shape(feature["geometry"])
        from shapely.ops import transform as shapely_transform
        feature["geometry"] = mapping(shapely_transform(transformer.transform, geom))
    output["metadata"] = {
        **output.get("metadata", {}),
        "source_crs": source_crs,
        "target_crs": target_crs,
    }
    return output


def build_spatial_query_plan(
    *,
    collection: str,
    bbox: Iterable[float] | None = None,
    filters: list[dict[str, Any]] | None = None,
    limit: int = 100,
) -> dict[str, Any]:
    if not collection.replace("_", "").isalnum():
        raise ValueError("Collection name contains unsupported characters.")
    if not 1 <= limit <= 1000:
        raise ValueError("limit must be between 1 and 1000.")

    bbox_list = list(bbox) if bbox is not None else None
    if bbox_list is not None:
        if len(bbox_list) != 4:
            raise ValueError("bbox must contain exactly four numbers.")
        minx, miny, maxx, maxy = map(float, bbox_list)
        if minx >= maxx or miny >= maxy:
            raise ValueError("bbox bounds are invalid.")
        bbox_list = [minx, miny, maxx, maxy]

    safe_filters: list[dict[str, Any]] = []
    for item in filters or []:
        field = str(item.get("field", ""))
        operator = str(item.get("operator", ""))
        if not field.replace("_", "").isalnum():
            raise ValueError("Filter field contains unsupported characters.")
        if operator not in _ALLOWED_OPERATORS:
            raise ValueError(f"Unsupported filter operator: {operator}")
        safe_filters.append({"field": field, "operator": operator, "value": item.get("value")})

    return {
        "collection": collection,
        "bbox": bbox_list,
        "filters": safe_filters,
        "limit": limit,
        "execution_mode": "parameterized-only",
        "raw_sql_allowed": False,
    }


def summarize_field_records(records: list[dict[str, Any]], status_field: str = "status") -> dict[str, Any]:
    statuses = Counter(str(record.get(status_field, "missing")) for record in records)
    missing_geometry = sum(1 for record in records if not record.get("geometry"))
    return {
        "total_records": len(records),
        "status_counts": dict(sorted(statuses.items())),
        "missing_geometry": missing_geometry,
        "completion_ratio": round(
            (len(records) - missing_geometry) / len(records), 4
        ) if records else 0.0,
    }


def detect_data_quality_issues(
    records: list[dict[str, Any]],
    required_fields: tuple[str, ...] = ("id", "geometry"),
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, record in enumerate(records):
        for field in required_fields:
            if record.get(field) in (None, ""):
                issues.append({"index": index, "type": "missing_required_field", "field": field})
        record_id = record.get("id")
        if record_id is not None:
            sid = str(record_id)
            if sid in seen_ids:
                issues.append({"index": index, "type": "duplicate_id", "value": sid})
            seen_ids.add(sid)
    return issues


def generate_maplibre_style(
    source_url: str,
    source_layer: str,
    *,
    layer_id: str = "features",
    geometry_type: str = "fill",
) -> dict[str, Any]:
    if geometry_type not in {"fill", "line", "circle"}:
        raise ValueError("geometry_type must be fill, line, or circle.")
    return {
        "version": 8,
        "sources": {
            "book-source": {
                "type": "vector",
                "url": source_url,
            }
        },
        "layers": [
            {
                "id": layer_id,
                "type": geometry_type,
                "source": "book-source",
                "source-layer": source_layer,
            }
        ],
    }
