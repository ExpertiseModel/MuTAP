from script_71_cp_normal import triangle_area

def test_triangle_area():
    assert triangle_area(3, 4, 5) == 6
    assert triangle_area(5, 12, 13) == 30
    assert triangle_area(1, 1, 1) == 0.43
    assert triangle_area(2, 2, 2) == 1.73
    assert triangle_area(3, 3, 3) == 3.9
    assert triangle_area(4, 4, 4) == 6.93
    assert triangle_area(5, 5, 5) == 10.83
    assert triangle_area(6, 6, 6) == 15.59
    assert triangle_area(7, 7, 7) == 21.22
    assert triangle_area(8, 8, 8) == 27.72
    assert triangle_area(9, 9, 9) == 35.09
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(11, 11, 11) == 52.36
    assert triangle_area(12, 12, 12) == 62.27
    