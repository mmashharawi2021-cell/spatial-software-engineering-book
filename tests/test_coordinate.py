"""Exercise the actual CB-010 class, including construction-time rejection."""
import runpy
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

Coordinate = runpy.run_path(str(
    Path(__file__).resolve().parents[1] / "book/chapter-04/examples/CB-010.py"
))["Coordinate"]


@pytest.mark.parametrize("lon,lat", [(0, 0), (-180, -90), (180, 90), (35.2, 31.9)])
def test_valid_coordinate(lon, lat):
    coordinate = Coordinate(lon=lon, lat=lat)
    assert (coordinate.lon, coordinate.lat) == (lon, lat)


@pytest.mark.parametrize("lon,lat", [
    (300, 150), (-180.01, 0), (180.01, 0), (0, -90.01), (0, 90.01),
    (float("nan"), 0), (0, float("nan")), (float("inf"), 0),
    (0, float("-inf")),
])
def test_invalid_coordinate_rejected_at_construction(lon, lat):
    with pytest.raises(ValueError, match="invalid coordinate"):
        Coordinate(lon=lon, lat=lat)


def test_coordinate_cannot_be_mutated_after_validation():
    coordinate = Coordinate(lon=0, lat=0)
    with pytest.raises(FrozenInstanceError):
        coordinate.lon = 300
