# Book ↔ Repository Mapping

Official mapping for **هندسة البرمجيات المكانية: من البيانات الجغرافية إلى التطبيقات الذكية**.

This file maps the 21 book chapters to their companion repository paths. It complements the appendix inside the manuscript.

| Chapter | Primary path | Related components |
|---|---|---|
| 01 | `book/chapter-01/` | `docs/`, `README.md` |
| 02 | `book/chapter-02/` | `data/`, `python/` |
| 03 | `book/chapter-03/` | `data/`, `python/` |
| 04 | `book/chapter-04/` | `tests/`, `docs/` |
| 05 | `book/chapter-05/` | `python/` |
| 06 | `book/chapter-06/` | `database/` |
| 07 | `book/chapter-07/` | `api/`, `web/` |
| 08 | `book/chapter-08/` | `web/` |
| 09 | `book/chapter-09/` | `web/` |
| 10 | `book/chapter-10/` | `api/` |
| 11 | `book/chapter-11/` | `mobile/` |
| 12 | `book/chapter-12/` | `data/`, `mobile/` |
| 13 | `book/chapter-13/` | `web/`, `api/` |
| 14 | `book/chapter-14/` | `python/`, `.github/workflows/` |
| 15 | `book/chapter-15/` | `skills/`, `agents/`, `mcp/` |
| 16 | `book/chapter-16/` | `data/`, `python/` |
| 17 | `book/chapter-17/` | `benchmarks/`, `database/` |
| 18 | `book/chapter-18/` | `api/`, `tests/` |
| 19 | `book/chapter-19/` | `tests/`, `.github/workflows/` |
| 20 | `book/chapter-20/` | `database/`, `api/`, `web/`, `skills/`, `agents/`, `mcp/` |
| 21 | `book/chapter-21/` | `docs/`, `benchmarks/` |

## Intelligent layer

- `skills/`: deterministic, testable spatial capabilities.
- `agents/`: orchestration over skills; no duplicated GIS business logic.
- `mcp/`: provider-agnostic adapter/tool registry for exposing selected skills.
- `docs/agent-architecture.md`: architecture and boundaries.
- `tests/test_agents_skills.py`: skills/agents/MCP integration tests.

## Publication rule

The printed book should eventually point to a frozen release (for example `book-v1.0.0`) rather than relying on the moving `main` branch. Until that release exists, this mapping references the current repository structure only.
