def approval_reason(has_photo, gps_accuracy_m):
    if not has_photo: return "missing_photo"
    if gps_accuracy_m is None: return "missing_accuracy"
    if gps_accuracy_m > 15: return "low_gps_quality"
    return "ok"

assert approval_reason(True, 8) == "ok"
