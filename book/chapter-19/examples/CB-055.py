def test_boundary_case():
    expected = "boundary"
    actual = classify_point(POINT_ON_EDGE)
    assert actual == expected
