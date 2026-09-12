budget = {"db_ms":120,"api_ms":200,"payload_kb":400,"render_ms":120}
observed = {"db_ms":80,"api_ms":160,"payload_kb":620,"render_ms":100}
violations = {k:v for k,v in observed.items() if v > budget[k]}
assert "payload_kb" in violations
