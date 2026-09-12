# Geospatial Agents

Agents orchestrate deterministic skills; they do not replace spatial databases or core GIS logic.

| Agent | Role |
|---|---|
| Spatial Data Agent | Validate and optionally transform spatial data. |
| Spatial Query Agent | Produce safe structured query plans. |
| Field Data Agent | Summarize field records and surface quality issues. |
| Map Assistant Agent | Build minimal MapLibre styles. |
| GeoAI Assistant | Provider-agnostic orchestration shell for semantic planning. |

The default implementation works without an LLM. An LLM adapter may be attached only to `GeoAIAssistant.planner` and must return structured actions.