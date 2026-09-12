from pyproj import Geod
geod = Geod(ellps='WGS84')

# distance on the ellipsoid
az12, az21, dist_m = geod.inv(34.45, 31.50, 34.47, 31.52)
print(round(dist_m, 2), 'm')
