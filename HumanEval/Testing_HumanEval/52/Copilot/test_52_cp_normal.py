from script_52_cp_normal import below_threshold

def test_below_threshold():
    assert below_threshold([1, 2, 3, 4, 5], 6) == True
    assert below_threshold([1, 2, 3, 4, 5], 5) == False
    assert below_threshold([1, 2, 3, 4, 5], 4) == False
    assert below_threshold([1, 2, 3, 4, 5], 3) == False
    assert below_threshold([1, 2, 3, 4, 5], 2) == False
    assert below_threshold([1, 2, 3, 4, 5], 1) == False
    assert below_threshold([1, 2, 3, 4, 5], 0) == False
    assert below_threshold([1, 2, 3, 4, 5], -1) == False
    assert below_threshold([1, 2, 3, 4, 5], -2) == False
    assert below_threshold([1, 2, 3, 4, 5], -3) == False
    assert below_threshold([1, 2, 3, 4, 5], -4) == False
    assert below_threshold([1, 2, 3, 4, 5], -5) == False
    assert below_threshold([1, 2, 3, 4, 5], -6) == False
    assert below_threshold([1, 2, 3, 4, 5], -7) == False
    assert below_threshold([1, 2, 3, 4, 5], -8) == False
    assert below_threshold([1, 2, 3, 4, 5], -9) == False
    assert below_threshold([1, 2, 3, 4, 5], -10) == False
    assert below_threshold([1, 2, 3, 4, 5], -11) == False
    assert below_threshold([1, 2, 3, 4, 5], -12) == False
    assert below_threshold([1, 2, 3, 4, 5], -13) == False