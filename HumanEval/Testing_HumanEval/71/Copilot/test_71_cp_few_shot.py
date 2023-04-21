from script_71_cp_few_shot import triangle_area


def test_triangle_area():
    assert triangle_area(2, 2, 2) == 1.73
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(3, 4, 1) == -1
    assert triangle_area(3, 4, 6) == -1
    assert triangle_area(8, 5, 7) == 17.32
    assert triangle_area(1, 1, 3) == -1
    assert triangle_area(2, 2, 1) == -1
    assert triangle_area(2, 5, 4) == -1
    assert triangle_area(5, 2, 4) == -1
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(3, 5, 4) == 6.0
