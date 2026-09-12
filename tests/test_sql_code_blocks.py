from __future__ import annotations

import os
from pathlib import Path

import psycopg
import pytest

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
    "CB-017": "",
    "CB-018": """
        CREATE TABLE facilities (
          id text PRIMARY KEY,
          name text NOT NULL,
          geom geometry(Point, 4326) NOT NULL
        );
    """,
    "CB-019": """
        CREATE TABLE features (
          id uuid PRIMARY KEY,
          status text NOT NULL,
          version integer NOT NULL DEFAULT 1,
          updated_at timestamptz NOT NULL DEFAULT now()
        );
        INSERT INTO features (id, status, version)
        VALUES ('00000000-0000-0000-0000-000000000001', 'draft', 1);
    """,
    "CB-020": "",
    "CB-021": """
        CREATE TABLE assets (
          id uuid PRIMARY KEY,
          geom geometry(MultiPolygon, 4326) NOT NULL
        );
    """,
    "CB-035": "",
    "CB-040": """
        CREATE TABLE assets (
          id uuid PRIMARY KEY,
          zone_id text,
          review_status text NOT NULL
        );
    """,
    "CB-050": """
        CREATE TABLE assets (
          id uuid PRIMARY KEY,
          lifecycle_status text NOT NULL,
          geom geometry(MultiPolygon, 4326) NOT NULL
        );
    """,
    "CB-052": """
        CREATE TABLE assets (id uuid PRIMARY KEY);
        CREATE ROLE app_reader;
        CREATE ROLE app_editor;
    """,
}

REPLACEMENTS = {
    ":lon": "35.21",
    ":lat": "31.90",
    ":status": "'verified'",
    ":id": "'00000000-0000-0000-0000-000000000001'",
    ":expected_version": "1",
}


@pytest.mark.parametrize("block_id", sorted(SQL_BLOCKS))
def test_runnable_sql_block_executes(block_id: str) -> None:
    sql = SQL_BLOCKS[block_id].read_text(encoding="utf-8")
    for old, new in REPLACEMENTS.items():
        sql = sql.replace(old, new)

    with psycopg.connect(DATABASE_URL) as conn:
        try:
            conn.execute("CREATE EXTENSION IF NOT EXISTS postgis", prepare=False)
            context = CONTEXT[block_id].strip()
            if context:
                conn.execute(context, prepare=False)
            conn.execute(sql, prepare=False)
        finally:
            conn.rollback()
