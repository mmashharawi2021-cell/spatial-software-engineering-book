import geopandas as gpd
from pathlib import Path

raw = gpd.read_file("data/raw/buildings.geojson")
assert raw.crs is not None
raw = raw.drop_duplicates("external_id")
Path("data/processed").mkdir(exist_ok=True)
raw.to_parquet("data/processed/buildings.parquet", index=False)
