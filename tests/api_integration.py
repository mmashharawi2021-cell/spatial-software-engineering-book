from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request

BASE = os.getenv("API_BASE", "http://127.0.0.1:8000")


def get(path: str, expected: int = 200):
    try:
        with urllib.request.urlopen(BASE + path, timeout=5) as response:
            status = response.status
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        status = exc.code
        body = exc.read().decode("utf-8")
    assert status == expected, (path, status, body)
    return json.loads(body)


health = get("/health")
assert health == {"status": "ok"}

ready = get("/ready")
assert ready == {"status": "ready"}

invalid = get("/assets?bbox=bad", expected=400)
assert invalid["detail"]["code"] == "invalid_bbox"

bbox = urllib.parse.quote("35.20,31.89,35.22,31.91")
collection = get(f"/assets?bbox={bbox}&limit=10")
assert collection["type"] == "FeatureCollection"
assert len(collection["features"]) == 3
assert all(feature["geometry"] for feature in collection["features"])

page1 = get(f"/assets?bbox={bbox}&limit=1&offset=0")
assert len(page1["features"]) == 1
assert any(link["rel"] == "next" for link in page1["links"])

approved = get(f"/assets?bbox={bbox}&status=approved")
assert len(approved["features"]) == 1
assert approved["features"][0]["properties"]["review_status"] == "approved"

print("API integration checks passed")
