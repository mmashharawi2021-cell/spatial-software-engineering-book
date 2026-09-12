from pathlib import Path

import geopandas as gpd

buildings = gpd.read_file("data/raw/buildings.geojson")
zones = gpd.read_file("data/raw/zones.geojson")
assert buildings.crs == zones.crs

joined = gpd.sjoin(
    buildings,
    zones[["zone_id", "geometry"]],
    predicate="within",
)

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)
joined.to_parquet(output_dir / "buildings_enriched.parquet", index=False)
