from shapely import make_valid

invalid = ~gdf.geometry.is_valid
gdf.loc[invalid, 'geometry_original_wkt'] = gdf.loc[invalid, 'geometry'].to_wkt()
gdf.loc[invalid, 'geometry'] = gdf.loc[invalid, 'geometry'].map(make_valid)

# audit the effect
print('repaired:', int(invalid.sum()))
print(gdf.geom_type.value_counts())
