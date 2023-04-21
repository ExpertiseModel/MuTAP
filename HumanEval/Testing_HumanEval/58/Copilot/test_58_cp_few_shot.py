from script_58_cp_few_shot import common


def test_common():
    assert common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert common([1, 2, 3, 4], [5, 6]) == []
    assert common([1, 2, 3, 4], [1, 2, 3, 4]) == [1, 2, 3, 4]
    assert common([1, 1, 1, 1], [1, 1, 1, 1]) == [1]
    assert common([1, 1, 1, 1], [2, 2, 2, 2]) == []
    assert common([1, 2, 3, 4], [1, 1, 1, 1]) == [1]
    assert common([1, 1, 1, 1], [1, 2, 3, 4]) == [1]
    assert common([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4]
    assert common([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4]) == [1, 2, 3, 4]
    assert common([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert common([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8,


