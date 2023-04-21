from script_45_cp_few_shot import triangle_area


def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 5) == 75
    assert triangle_area(1, 5) == 25
    assert triangle_area(1, 1) == 0.5
    assert triangle_area(1, 0) == 0
    assert triangle_area(0, 1) == 0
    assert triangle_area(0, 0) == 0
    assert triangle_area(2, 0) == 0
    assert triangle_area(3, 3) == 4.5
    assert triangle_area(15, 11) == 82.5



