from script_5_cp_few_shot import intersperse

def test_intersperse():
    assert intersperse([1, 2, 3, 4], 0) == [1, 0, 2, 0, 3, 0, 4]
    assert intersperse([1, 2, 3, 4], 1) == [1, 1, 2, 1, 3, 1, 4]
    assert intersperse([1, 2, 3, 4], 2) == [1, 2, 2, 2, 3, 2, 4]
    assert intersperse([1, 2, 3, 4], 3) == [1, 3, 2, 3, 3, 3, 4]
    assert intersperse([1, 2, 3, 4], 4) == [1, 4, 2, 4, 3, 4, 4]
    assert intersperse([1, 2, 3, 4], 5) == [1, 5, 2, 5, 3, 5, 4]
    assert intersperse([1, 2, 3, 4], 6) == [1, 6, 2, 6, 3, 6, 4]
    assert intersperse([1, 2, 3, 4], 7) == [1, 7, 2, 7, 3, 7, 4]