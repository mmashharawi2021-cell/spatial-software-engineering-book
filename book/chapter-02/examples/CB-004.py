# Correct sequence when source CRS is known but missing from metadata
gdf = gpd.read_file('data/source.gpkg')
gdf = gdf.set_crs('EPSG:4326', allow_override=True)
gdf_metric = gdf.to_crs('EPSG:32636')
