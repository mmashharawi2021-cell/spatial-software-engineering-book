from pyproj import Transformer
tr = Transformer.from_crs(4326, 32636, always_xy=True)
x, y = tr.transform(35.22, 31.90)
assert 0 < x < 1_000_000
assert 0 < y < 10_000_000
