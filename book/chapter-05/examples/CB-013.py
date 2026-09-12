from dataclasses import dataclass
from pathlib import Path
import geopandas as gpd

@dataclass
class PipelineConfig:
    source: Path
    output: Path
    target_crs: str

def run_pipeline(cfg: PipelineConfig):
    gdf = gpd.read_file(cfg.source)
    validate_schema(gdf)
    clean = transform_features(gdf, cfg.target_crs)
    clean.to_file(cfg.output, driver='GPKG')
