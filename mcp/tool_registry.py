from __future__ import annotations

from typing import Any, Callable

from skills import (
    build_spatial_query_plan,
    detect_data_quality_issues,
    generate_maplibre_style,
    summarize_field_records,
    transform_geojson_crs,
    validate_geojson,
)

TOOLS: dict[str, Callable[..., Any]] = {
    "validate-geojson": validate_geojson,
    "transform-crs": transform_geojson_crs,
    "spatial-query": build_spatial_query_plan,
    "summarize-field-data": summarize_field_records,
    "detect-data-quality-issues": detect_data_quality_issues,
    "generate-map-style": generate_maplibre_style,
}


def invoke_tool(name: str, arguments: dict[str, Any]) -> Any:
    if name not in TOOLS:
        raise KeyError(f"Unknown tool: {name}")
    if not isinstance(arguments, dict):
        raise TypeError("Tool arguments must be a dictionary.")
    return TOOLS[name](**arguments)
