from pyproj import CRS
from shapely.geometry import shape

def validate_feature(feature):
    geom = shape(feature["geometry"])
    if geom.is_empty:
        raise ValueError("empty geometry")
    if not geom.is_valid:
        raise ValueError("invalid geometry")
    crs = CRS.from_epsg(4326)
    return {"valid": True, "crs": crs.to_string()}
