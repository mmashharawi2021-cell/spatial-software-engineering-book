def can_read(user_zones:set[str], asset_zone:str)->bool:
    return asset_zone in user_zones

assert can_read({"Z-A"},"Z-B") is False
