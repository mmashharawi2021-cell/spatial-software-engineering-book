# Code Block Audit — Pre-release

Book: **هندسة البرمجيات المكانية — من البيانات الجغرافية إلى التطبيقات الذكية**

Repository: `mmashharawi2021-cell/spatial-software-engineering-book`

Audit scope: all `Spatial Code` blocks in the v0.4 manuscript.

## Summary

- Total code blocks: **60**
- Syntax failures found in automated checks: **0**
- Python snippets were parsed with Python AST.
- JSON blocks were parsed as JSON.
- YAML/config blocks were parsed with PyYAML when applicable.
- TypeScript blocks were checked with `tsc` for parser/syntax errors; no TS1xxx parse errors were found.
- SQL/PostGIS blocks require PostgreSQL/PostGIS execution context; repository CI covers migrations/seed/smoke tests, but not every manuscript SQL fragment independently.
- Dart/Flutter block requires Dart SDK and remains a review item.

### Languages
- dart: 1
- json: 2
- python: 29
- sql: 9
- text: 10
- typescript: 5
- yaml: 4

### Classification
- Runnable/Near-runnable: 23
- Runnable with fixture: 4
- Runnable with database context: 9
- Runnable data: 2
- Configuration/Illustrative: 3
- Illustrative: 13
- Illustrative or module snippet: 5
- Illustrative/module snippet: 1

## Release blockers

1. **Not every manuscript block is file-backed yet.** The chapter folders mostly contain mapping/readme material, while several manuscript examples exist only in the book.
2. **Dart/Flutter snippet is not compiler-verified in CI.** Add Flutter/Dart CI or explicitly mark it Illustrative.
3. **Several SQL fragments are pedagogical fragments, not standalone migrations.** They must be marked Illustrative or copied into executable fixtures/tests.
4. **Textual HTTP examples, shell commands, architecture arrows, and folder trees are illustrative by nature and must be labeled as such in the manuscript.
5. Do not create `book-v1.0.0` until every Runnable block has an exact repository path and a verification method.

## Acceptance rule for v1.0.0

Each block must have one of two explicit statuses:

- **Runnable** — exact repository file + dependency/data requirements + automated or documented verification.
- **Illustrative / Pseudocode** — clearly labeled in the manuscript and not presented as copy-paste runnable code.

## Chapter-level repository areas

| Chapter | Primary repository area |
|---:|---|
| 1 | `book/chapter-01/`, `docs/` |
| 2 | `book/chapter-02/`, `python/` |
| 3 | `book/chapter-03/`, `data/` |
| 4 | `book/chapter-04/`, `tests/` |
| 5 | `book/chapter-05/`, `python/` |
| 6 | `book/chapter-06/`, `database/` |
| 7 | `book/chapter-07/`, `api/`, `web/` |
| 8 | `book/chapter-08/`, `web/` |
| 9 | `book/chapter-09/`, `web/` |
| 10 | `book/chapter-10/`, `api/` |
| 11 | `book/chapter-11/`, `mobile/` |
| 12 | `book/chapter-12/`, `mobile/`, `data/` |
| 13 | `book/chapter-13/`, `database/`, `api/` |
| 14 | `book/chapter-14/`, `python/`, `.github/workflows/` |
| 15 | `book/chapter-15/`, `skills/`, `agents/`, `mcp/` |
| 16 | `book/chapter-16/`, `python/`, `data/` |
| 17 | `book/chapter-17/`, `benchmarks/`, `database/` |
| 18 | `book/chapter-18/`, `api/`, `tests/` |
| 19 | `book/chapter-19/`, `tests/`, `.github/workflows/` |
| 20 | `book/chapter-20/`, `database/`, `api/`, `web/`, `skills/`, `agents/`, `mcp/` |
| 21 | `book/chapter-21/`, `docs/`, `benchmarks/` |

## Verification note

The authoritative clean-checkout verification is GitHub Actions because it performs `actions/checkout` on a fresh hosted runner, installs dependencies, runs the Web build, Python/Skills/Agents/MCP checks, ETL/validation, PostgreSQL/PostGIS migration, seed, and spatial smoke tests. Local `git clone` could not be executed in the audit sandbox because outbound DNS to `github.com` is unavailable; this is an environment limitation, not a repository failure.
