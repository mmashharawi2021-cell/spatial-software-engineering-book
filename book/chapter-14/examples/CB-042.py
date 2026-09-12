def run_job(run_id, source_version):
    log_event(run_id, "started", source_version=source_version)
    try:
        result = refresh_quality_metrics()
        log_event(run_id, "succeeded", rows=result.rows)
    except Exception as exc:
        log_event(run_id, "failed", error=str(exc))
        raise
