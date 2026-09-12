def validate_lon_lat(lon, lat):
    if not (-180 <= lon <= 180):
        raise ValueError('longitude out of range')
    if not (-90 <= lat <= 90):
        raise ValueError('latitude out of range')
    return True
