import geopandas as gpd

buildings = gpd.read_file("data/buildings.geojson")
zones = gpd.read_file("data/zones.geojson")
assert buildings.crs == zones.crs
joined = gpd.sjoin(buildings, zones[["zone_id", "geometry"]], predicate="within")
joined.to_parquet("output/buildings_enriched.parquet", index=False)
