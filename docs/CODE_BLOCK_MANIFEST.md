# Code Block Manifest

Canonical mapping between manuscript code blocks and repository files.

Each manuscript block has exactly one release status:
- **Runnable** — file-backed and accompanied by execution requirements / verification.
- **Illustrative / Pseudocode** — file-backed for traceability but not presented as standalone copy-paste code.

| ID | Chapter | Language | Status | Repository path | Requirements | Verification |
|---|---:|---|---|---|---|---|
| CB-001 | 1 | yaml | Illustrative / Pseudocode | `book/chapter-01/examples/CB-001.yaml` | None | yaml syntax/parser check |
| CB-002 | 1 | python | Runnable | `book/chapter-01/examples/CB-002.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-003 | 2 | python | Runnable | `book/chapter-02/examples/CB-003.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-004 | 2 | python | Runnable | `book/chapter-02/examples/CB-004.py` | Chapter fixture/training dataset | Syntax-checked; run with the documented chapter fixture |
| CB-005 | 2 | python | Runnable | `book/chapter-02/examples/CB-005.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-006 | 2 | python | Runnable | `book/chapter-02/examples/CB-006.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-007 | 2 | python | Runnable | `book/chapter-02/examples/CB-007.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-008 | 3 | json | Runnable | `book/chapter-03/examples/CB-008.json` | None | JSON parser |
| CB-009 | 3 | python | Runnable | `book/chapter-03/examples/CB-009.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-010 | 4 | python | Runnable | `book/chapter-04/examples/CB-010.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-011 | 4 | python | Runnable | `book/chapter-04/examples/CB-011.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-012 | 4 | python | Runnable | `book/chapter-04/examples/CB-012.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-013 | 5 | python | Runnable | `book/chapter-05/examples/CB-013.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-014 | 5 | python | Illustrative / Pseudocode | `book/chapter-05/examples/CB-014.py` | None | python syntax/parser check |
| CB-015 | 5 | python | Runnable | `book/chapter-05/examples/CB-015.py` | Chapter fixture/training dataset | Syntax-checked; run with the documented chapter fixture |
| CB-016 | 5 | python | Runnable | `book/chapter-05/examples/CB-016.py` | Chapter fixture/training dataset | Syntax-checked; run with the documented chapter fixture |
| CB-017 | 6 | sql | Runnable | `book/chapter-06/examples/CB-017.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-018 | 6 | sql | Runnable | `book/chapter-06/examples/CB-018.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-019 | 6 | sql | Runnable | `book/chapter-06/examples/CB-019.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-020 | 6 | sql | Runnable | `book/chapter-06/examples/CB-020.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-021 | 6 | sql | Runnable | `book/chapter-06/examples/CB-021.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-022 | 7 | yaml | Illustrative / Pseudocode | `book/chapter-07/examples/CB-022.yaml` | None | yaml syntax/parser check |
| CB-023 | 7 | python | Illustrative / Pseudocode | `book/chapter-07/examples/CB-023.py` | None | python syntax/parser check |
| CB-024 | 8 | text | Illustrative / Pseudocode | `book/chapter-08/examples/CB-024.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-025 | 8 | typescript | Illustrative / Pseudocode | `book/chapter-08/examples/CB-025.ts` | None | typescript syntax/parser check |
| CB-026 | - | typescript | Illustrative / Pseudocode | `book/appendices/examples/CB-026.ts` | None | typescript syntax/parser check |
| CB-027 | 8 | typescript | Illustrative / Pseudocode | `book/chapter-08/examples/CB-027.ts` | None | typescript syntax/parser check |
| CB-028 | 9 | typescript | Illustrative / Pseudocode | `book/chapter-09/examples/CB-028.ts` | None | typescript syntax/parser check |
| CB-029 | 9 | typescript | Illustrative / Pseudocode | `book/chapter-09/examples/CB-029.ts` | None | typescript syntax/parser check |
| CB-030 | 10 | text | Illustrative / Pseudocode | `book/chapter-10/examples/CB-030.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-031 | 10 | json | Runnable | `book/chapter-10/examples/CB-031.json` | None | JSON parser |
| CB-032 | 10 | text | Illustrative / Pseudocode | `book/chapter-10/examples/CB-032.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-033 | 10 | python | Runnable | `book/chapter-10/examples/CB-033.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-034 | 11 | text | Illustrative / Pseudocode | `book/chapter-11/examples/CB-034.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-035 | 11 | sql | Runnable | `book/chapter-11/examples/CB-035.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-036 | - | dart | Illustrative / Pseudocode | `book/appendices/examples/CB-036.dart` | None | Dart parser/formatter in CI |
| CB-037 | 11 | python | Runnable | `book/chapter-11/examples/CB-037.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-038 | 12 | python | Runnable | `book/chapter-12/examples/CB-038.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-039 | 12 | python | Runnable | `book/chapter-12/examples/CB-039.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-040 | 13 | sql | Runnable | `book/chapter-13/examples/CB-040.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-041 | 13 | python | Runnable | `book/chapter-13/examples/CB-041.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-042 | 14 | python | Runnable | `book/chapter-14/examples/CB-042.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-043 | 14 | python | Runnable | `book/chapter-14/examples/CB-043.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-044 | 15 | text | Illustrative / Pseudocode | `book/chapter-15/examples/CB-044.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-045 | 15 | text | Illustrative / Pseudocode | `book/chapter-15/examples/CB-045.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-046 | 15 | python | Runnable | `book/chapter-15/examples/CB-046.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-047 | 15 | python | Runnable | `book/chapter-15/examples/CB-047.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-048 | 16 | text | Illustrative / Pseudocode | `book/chapter-16/examples/CB-048.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-049 | 16 | python | Runnable | `book/chapter-16/examples/CB-049.py` | Chapter fixture/training dataset | Syntax-checked; run with the documented chapter fixture |
| CB-050 | 17 | sql | Runnable | `book/chapter-17/examples/CB-050.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-051 | 17 | python | Runnable | `book/chapter-17/examples/CB-051.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-052 | 18 | sql | Runnable | `book/chapter-18/examples/CB-052.sql` | PostgreSQL/PostGIS + repository schema/seed | PostGIS context; see database smoke tests / chapter notes |
| CB-053 | 18 | python | Runnable | `book/chapter-18/examples/CB-053.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-054 | 19 | yaml | Illustrative / Pseudocode | `book/chapter-19/examples/CB-054.yaml` | None | yaml syntax/parser check |
| CB-055 | 19 | python | Runnable | `book/chapter-19/examples/CB-055.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-056 | 20 | text | Illustrative / Pseudocode | `book/chapter-20/examples/CB-056.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-057 | 20 | python | Runnable | `book/chapter-20/examples/CB-057.py` | Python + imports/data shown in chapter when applicable | Python AST/compile syntax check; chapter context for execution |
| CB-058 | 21 | text | Illustrative / Pseudocode | `book/chapter-21/examples/CB-058.md` | None | Documentation-only; not presented as copy-paste runnable |
| CB-059 | 21 | python | Illustrative / Pseudocode | `book/chapter-21/examples/CB-059.py` | None | python syntax/parser check |
| CB-060 | - | text | Illustrative / Pseudocode | `book/appendices/examples/CB-060.md` | None | Documentation-only; not presented as copy-paste runnable |
