from agents import FieldDataAgent, GeoAIAssistant, MapAssistantAgent, SpatialDataAgent, SpatialQueryAgent
from mcp.tool_registry import invoke_tool
from skills import build_spatial_query_plan, detect_data_quality_issues, validate_geojson
import pytest


def sample_geojson():
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "b1",
                "properties": {"status": "reviewed"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[34.0, 31.0], [34.001, 31.0], [34.001, 31.001], [34.0, 31.001], [34.0, 31.0]]],
                },
            }
        ],
    }


def test_validate_geojson_and_spatial_data_agent():
    data = sample_geojson()
    assert validate_geojson(data)["valid"] is True
    inspected = SpatialDataAgent().inspect(data)
    assert inspected["validation"]["feature_count"] == 1


def test_query_plan_rejects_raw_sql_concept():
    plan = build_spatial_query_plan(collection="buildings", bbox=[34, 31, 35, 32], limit=25)
    assert plan["raw_sql_allowed"] is False
    assert SpatialQueryAgent().plan(collection="buildings")["execution_mode"] == "parameterized-only"


def test_field_agent_detects_duplicate_and_missing_geometry():
    records = [
        {"id": "1", "status": "done", "geometry": {"type": "Point", "coordinates": [34, 31]}},
        {"id": "1", "status": "pending", "geometry": None},
    ]
    result = FieldDataAgent().review(records)
    assert result["summary"]["missing_geometry"] == 1
    assert any(issue["type"] == "duplicate_id" for issue in result["quality_issues"])
    assert len(detect_data_quality_issues(records)) >= 2


def test_map_agent_and_mcp_registry():
    style = MapAssistantAgent().build_style("mapbox://example", "buildings")
    assert style["version"] == 8
    mcp_result = invoke_tool("summarize-field-data", {"records": []})
    assert mcp_result["total_records"] == 0


def test_geoai_assistant_is_provider_agnostic():
    assistant = GeoAIAssistant()
    result = assistant.plan({"goal": "inspect spatial data"})
    assert result["mode"] == "deterministic"
    assert "spatial-query" in result["available_skills"]


def test_geoai_accepts_structured_planner_adapter():
    assistant = GeoAIAssistant(planner=lambda request: {"skill": "validate-geojson", "arguments": request})
    result = assistant.plan({"data": {}})
    assert result["mode"] == "llm-assisted"
    assert result["action"]["skill"] == "validate-geojson"


def test_tool_registry_rejects_unknown_tool():
    with pytest.raises(KeyError):
        invoke_tool("drop-database", {})


def test_tool_registry_requires_dictionary_arguments():
    with pytest.raises(TypeError):
        invoke_tool("summarize-field-data", [])  # type: ignore[arg-type]


def test_spatial_query_rejects_excessive_limit():
    with pytest.raises((TypeError, ValueError)):
        build_spatial_query_plan(collection="buildings", bbox=[34, 31, 35, 32], limit=1000000)
