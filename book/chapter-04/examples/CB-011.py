class ValidationError(Exception):
    pass

def can_approve(has_photo: bool, gps_accuracy_m: float) -> bool:
    if not has_photo:
        return False
    if gps_accuracy_m > 15:
        return False
    return True
