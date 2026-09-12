modules = {
  "assets": ["repository", "service", "routes"],
  "review": ["policy", "service", "routes"],
  "reports": ["queries", "service"]
}
assert "database" not in modules["review"]
