from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from skills import (
    build_spatial_query_plan,
    detect_data_quality_issues,
    generate_maplibre_style,
    summarize_field_records,
    transform_geojson_crs,
    validate_geojson,
)


@dataclass
class SpatialDataAgent:
    def inspect(self, geojson: dict[str, Any], *, source_crs: str | None = None, target_crs: str = "EPSG:4326") -> dict[str, Any]:
        validation = validate_geojson(geojson)
        result: dict[str, Any] = {"validation": validation}
        if validation["valid"] and source_crs and source_crs != target_crs:
            result["transformed"] = transform_geojson_crs(geojson, source_crs, target_crs)
        return result


@dataclass
class SpatialQueryAgent:
    def plan(self, **kwargs: Any) -> dict[str, Any]:
        return build_spatial_query_plan(**kwargs)


@dataclass
class FieldDataAgent:
    def review(self, records: list[dict[str, Any]]) -> dict[str, Any]:
        return {
            "summary": summarize_field_records(records),
            "quality_issues": detect_data_quality_issues(records),
        }


@dataclass
class MapAssistantAgent:
    def build_style(self, source_url: str, source_layer: str, **kwargs: Any) -> dict[str, Any]:
        return generate_maplibre_style(source_url, source_layer, **kwargs)


@dataclass
class GeoAIAssistant:
    """Provider-agnostic orchestrator.

    `planner` is optional and may be any local or remote model adapter that accepts a
    request dictionary and returns a structured action. Core skills remain deterministic.
    """

    planner: Callable[[dict[str, Any]], dict[str, Any]] | None = None

    def capabilities(self) -> list[str]:
        return [
            "validate-geojson",
            "transform-crs",
            "spatial-query",
            "summarize-field-data",
            "detect-data-quality-issues",
            "generate-map-style",
        ]

    def plan(self, request: dict[str, Any]) -> dict[str, Any]:
        if self.planner is None:
            return {
                "mode": "deterministic",
                "available_skills": self.capabilities(),
                "request": request,
                "message": "Attach an LLM adapter only when semantic planning is required.",
            }
        action = self.planner(request)
        if not isinstance(action, dict):
            raise TypeError("Planner must return a structured dictionary action.")
        return {"mode": "llm-assisted", "action": action}
