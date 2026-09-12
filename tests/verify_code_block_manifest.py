from __future__ import annotations

import ast
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "CODE_BLOCK_MANIFEST.md"
RUNNABLE_SUFFIXES = {".py", ".json", ".yaml", ".yml", ".sql"}

rows: dict[str, tuple[str, str]] = {}
for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
    if not raw.startswith("| CB-"):
        continue
    cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
    if len(cells) < 7:
        raise AssertionError(f"Malformed manifest row: {raw}")
    block_id, _chapter, _lang, status, path_cell, _requirements, _verification = cells[:7]
    path = path_cell.strip("`")
    if status not in {"Runnable", "Illustrative / Pseudocode"}:
        raise AssertionError(f"Unexpected status for {block_id}: {status}")
    rows[block_id] = (status, path)

expected = {f"CB-{i:03d}" for i in range(1, 61)}
actual = set(rows)
assert actual == expected, f"Manifest IDs differ. Missing={sorted(expected-actual)} extra={sorted(actual-expected)}"

for block_id, (status, rel_path) in sorted(rows.items()):
    path = ROOT / rel_path
    assert path.is_file(), f"{block_id}: missing repository file {rel_path}"
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8")

    if status == "Runnable" and suffix not in RUNNABLE_SUFFIXES:
        raise AssertionError(
            f"{block_id}: Runnable file type {suffix!r} has no verification path"
        )

    if suffix == ".py":
        ast.parse(text, filename=str(path))
    elif suffix == ".json":
        json.loads(text)
    elif suffix in {".yaml", ".yml"}:
        yaml.safe_load(text)
    elif suffix == ".sql":
        assert text.strip(), f"{block_id}: SQL file is empty"
        # Runnable SQL is executed against PostgreSQL/PostGIS later in CI by
        # tests/sql_code_block_integration.py after the repository schema/seed
        # has been loaded.
    elif status == "Runnable":
        raise AssertionError(f"{block_id}: unhandled Runnable suffix {suffix}")

print(f"Verified {len(rows)} manuscript code-block mappings")
