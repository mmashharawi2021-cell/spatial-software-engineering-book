from __future__ import annotations

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATABASE_URL = os.environ["DATABASE_URL"]

SQL_BLOCKS = {
    "CB-017": ROOT / "book/chapter-06/examples/CB-017.sql",
    "CB-018": ROOT / "book/chapter-06/examples/CB-018.sql",
    "CB-019": ROOT / "book/chapter-06/examples/CB-019.sql",
    "CB-020": ROOT / "book/chapter-06/examples/CB-020.sql",
    "CB-021": ROOT / "book/chapter-06/examples/CB-021.sql",
    "CB-035": ROOT / "book/chapter-11/examples/CB-035.sql",
    "CB-040": ROOT / "book/chapter-13/examples/CB-040.sql",
    "CB-050": ROOT / "book/chapter-17/examples/CB-050.sql",
    "CB-052": ROOT / "book/chapter-18/examples/CB-052.sql",
}

CONTEXT = {
    "CB-017": "CREATE SCHEMA cb_tmp; SET search_path = cb_tmp, public;",
    "CB-018": "",
    "CB-019": """
        CREATE TEMP TABLE features (
          id uuid PRIMARY KEY,
          status text NOT NULL,
          version integer NOT NULL DEFAULT 1,
          updated_at timestamptz NOT NULL DEFAULT now()
        );
        INSERT INTO features (id, status, version)
        VALUES ('00000000-0000-0000-0000-000000000001', 'draft', 1);
    """,
    "CB-020": "CREATE SCHEMA cb_tmp; SET search_path = cb_tmp, public;",
    "CB-021": "",
    "CB-035": "CREATE SCHEMA cb_tmp; SET search_path = cb_tmp, public;",
    "CB-040": "",
    "CB-050": "",
    "CB-052": "CREATE ROLE app_reader; CREATE ROLE app_editor;",
}

PSQL_VARS = [
    "-v", "lon=35.21",
    "-v", "lat=31.90",
    "-v", "status='verified'",
    "-v", "id='00000000-0000-0000-0000-000000000001'",
    "-v", "expected_version=1",
]

for block_id, path in SQL_BLOCKS.items():
    sql = path.read_text(encoding="utf-8")
    wrapped = f"BEGIN;\n{CONTEXT[block_id]}\n{sql}\nROLLBACK;\n"
    result = subprocess.run(
        ["psql", DATABASE_URL, "-X", "-v", "ON_ERROR_STOP=1", *PSQL_VARS],
        input=wrapped,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise SystemExit(
            f"{block_id} failed against its declared execution context.\n"
            f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    print(f"{block_id}: PASS")

print(f"Executed {len(SQL_BLOCKS)} runnable SQL code blocks")
