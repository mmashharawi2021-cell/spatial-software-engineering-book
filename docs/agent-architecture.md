# Skills, Agents, and MCP-ready Architecture

## Principle
The geospatial system remains data-first. PostGIS, APIs, validation, and deterministic GIS logic are the foundation. Agents are an orchestration layer above those components, not a replacement for them.

```text
User / Application
        |
        v
GeoAI Assistant / Specialized Agent
        |
        v
Structured Tool Call
        |
        v
Reusable Skill
        |
        v
PostGIS / API / Map / Field Data
```

## Separation of responsibilities
- **Skills**: deterministic, independently testable geospatial capabilities.
- **Agents**: coordinate one or more skills to achieve a higher-level goal.
- **MCP-ready registry**: exposes the same skills through a tool registry without coupling the repository to any single LLM vendor or transport.
- **LLM adapters**: optional semantic planners. They must return structured actions and never bypass validation or authorization boundaries.

## Safety boundaries
1. Spatial query tools do not accept or emit unrestricted raw SQL.
2. Collection names, fields, operators, bbox and limits are validated.
3. CRS transformation requires an explicit source CRS.
4. Agent outputs are plans or deterministic results; production authorization remains the responsibility of the API/service layer.
5. No agent receives database credentials directly.

## Current skills
`validate-geojson`, `transform-crs`, `spatial-query`, `summarize-field-data`, `detect-data-quality-issues`, and `generate-map-style`.

## Current agents
`SpatialDataAgent`, `SpatialQueryAgent`, `FieldDataAgent`, `MapAssistantAgent`, and `GeoAIAssistant`.

## Provider independence
`GeoAIAssistant` accepts an optional callable planner. That adapter can be implemented for OpenAI, Anthropic, Gemini, Ollama, llama.cpp, or another provider without changing the skills layer.

## MCP direction
`mcp/tools.json` is a transport-neutral manifest and `mcp/tool_registry.py` is the local adapter. A future MCP server should wrap this registry rather than duplicating geospatial logic.