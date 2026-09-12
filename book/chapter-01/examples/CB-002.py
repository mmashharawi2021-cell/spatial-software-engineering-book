decision = {
  "user": "field_collector",
  "task": "submit observation",
  "source_of_truth": "PostGIS",
  "offline": True,
  "approval_required": True
}
assert decision["source_of_truth"] != "map_state"
