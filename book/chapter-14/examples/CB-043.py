def should_run(last_success, source_version, current_version):
    return last_success is None or source_version != current_version

assert should_run(None, "v1", "v1")
