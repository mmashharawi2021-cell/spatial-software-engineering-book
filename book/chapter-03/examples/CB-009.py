status_dictionary = {
  "pending": {"final": False},
  "approved": {"final": True},
  "rejected": {"final": True}
}
assert all("final" in v for v in status_dictionary.values())
