from script_72_cp_normal import will_it_fly

def test_will_it_fly():
    assert will_it_fly([1, 2, 3, 4, 5], 15) == False
    assert will_it_fly([1, 2, 3, 4, 5], 14) == False
    assert will_it_fly([1, 2, 3, 4, 5], 13) == False
    assert will_it_fly([1, 2, 3, 4, 5], 12) == False
    assert will_it_fly([1, 2, 3, 4, 5], 11) == False
    assert will_it_fly([1, 2, 3, 4, 5], 10) == False
    assert will_it_fly([1, 2, 3, 4, 5], 9) == False
    assert will_it_fly([1, 2, 3, 4, 5], 8) == False
    assert will_it_fly([1, 2, 3, 4, 5], 7) == False
    assert will_it_fly([1, 2, 3, 4, 5], 6) == False
    assert will_it_fly([1, 2, 3, 4, 5], 5) == False
    assert will_it_fly([1, 2, 3, 4, 5], 4) == False
    assert will_it_fly([1, 2, 3, 4, 5], 3) == False
    assert will_it_fly([1, 2, 3, 4, 5], 2) == False
    assert will_it_fly([1, 2, 3, 4, 5], 1) == False
    assert will_it_fly([1, 2, 3, 4, 5], 0) == False
    assert will_it_fly([1, 2, 3, 4, 5], -1) == False
    assert will_it_fly([1, 2, 3, 4, 5], -2) == False