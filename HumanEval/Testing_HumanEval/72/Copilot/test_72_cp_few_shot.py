from script_72_cp_few_shot import will_it_fly


def test_will_it_fly():
    assert will_it_fly([1, 2, 3, 2, 1], 10) == True
    assert will_it_fly([1, 2, 3, 2, 1], 5) == False
    assert will_it_fly([1, 2, 3, 2, 1], 6) == True
    assert will_it_fly([1, 2, 3, 2, 1], 7) == True
    assert will_it_fly([1, 2, 3, 2, 1], 8) == True
    assert will_it_fly([1, 2, 3, 2, 1], 9) == True
    assert will_it_fly([1, 2, 3, 2, 1], 4) == False
    assert will_it_fly([1, 2, 3, 2, 1], 3) == False
    assert will_it_fly([1, 2, 3, 2, 1], 2) == False
    assert will_it_fly([1, 2, 3, 2, 1], 1) == False
    assert will_it_fly([1, 2, 3, 2, 1], 0) == False
    assert will_it_fly([1, 2, 3, 2, 1], -1) == False
    assert will_it_fly([1, 2, 3, 2, 1], -2) == False
    assert will_it_fly([1, 2, 3, 2, 1], -3) == False
    assert will_it_fly([1, 2, 3, 2, 1], -4) == False
    assert will_it_fly([1, 2, 3, 2, 1], -5) == False
    assert will_it_fly([1, 2, 3, 2, 1], -6) == False
    assert will_it_fly([1, 2, 3, 2, 1], -7) == False


