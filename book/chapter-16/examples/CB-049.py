import rasterio
with rasterio.open("data/hazard.tif") as src:
    meta = {"crs": str(src.crs), "res": src.res, "nodata": src.nodata}
    assert meta["crs"] is not None
