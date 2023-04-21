from script_52_cp_few_shot import below_threshold


def test_below_threshold():
    assert below_threshold([1, 2, 3], 4) == True
    assert below_threshold([1, 2, 3], 3) == False
    assert below_threshold([1, 2, 3], 2) == False
    assert below_threshold([1, 2, 3], 1) == False
    assert below_threshold([1, 2, 3], 0) == False
    assert below_threshold([1, 2, 3], -1) == False
    assert below_threshold([], 0) == True
    assert below_threshold([], 1) == True
    assert below_threshold([], -1) == True


