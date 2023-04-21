def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    """
    return a * h / 2.0


METADATA = {}



 # generate test case for the function above

def test_triangle_area():
    assert triangle_area(2, 2) == 2
    assert triangle_area(2, 3) == 3
    assert triangle_area(2, 4) == 4
    assert triangle_area(2, 5) == 5
    assert triangle_area(2, 6) == 6
    assert triangle_area(2, 7) == 7
    assert triangle_area(2, 8) == 8
    assert triangle_area(2, 9) == 9