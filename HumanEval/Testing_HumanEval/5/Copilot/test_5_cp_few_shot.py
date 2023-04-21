from script_5_cp_few_shot import intersperse


def test_intersperse():
    assert intersperse([], 0) == []
    assert intersperse([1], 0) == [1]
    assert intersperse([1, 2], 0) == [1, 0, 2]
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert intersperse([1, 2, 3, 4], 0) == [1, 0, 2, 0, 3, 0, 4]
    assert intersperse([1, 2, 3, 4, 5], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5]
    assert intersperse([1, 2, 3, 4, 5, 6], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]
    assert intersperse([1, 2, 3, 4, 5, 6, 7], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7]
    assert intersperse([1, 2, 3, 4, 5, 6, 7, 8], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8]
    assert intersperse([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]
