from __future__ import annotations

import ast
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "CODE_BLOCK_MANIFEST.md"

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

for block_id, (_status, rel_path) in sorted(rows.items()):
    path = ROOT / rel_path
    assert path.is_file(), f"{block_id}: missing repository file {rel_path}"
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8")
    if suffix == ".py":
        ast.parse(text, filename=str(path))
    elif suffix == ".json":
        json.loads(text)
    elif suffix in {".yaml", ".yml"}:
        yaml.safe_load(text)

print(f"Verified {len(rows)} manuscript code-block mappings")
