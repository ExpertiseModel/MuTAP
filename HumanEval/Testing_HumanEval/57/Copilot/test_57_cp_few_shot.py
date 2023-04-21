from script_57_cp_few_shot import monotonic


def test_monotonic():
    assert monotonic([1, 2, 3, 4, 5]) == True
    assert monotonic([5, 4, 3, 2, 1]) == True
    assert monotonic([1, 5, 2, 3, 4]) == False
    assert monotonic([1, 5, 2, 3, 4, 4]) == False
    assert monotonic([1, 2, 2, 3, 4]) == True
    assert monotonic([1, 2, 2, 3, 4, 4]) == True
    assert monotonic([1, 2, 2, 3, 4, 4, 5]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8]) == False
    assert monotonic([1]) == True
    assert monotonic([]) == True


