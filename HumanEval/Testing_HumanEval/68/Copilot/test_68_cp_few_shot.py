from script_68_cp_few_shot import pluck


def test_pluck():
    assert pluck([1, 2, 3, 4, 5]) == [2, 1]
    assert pluck([1, 3, 5, 7]) == []
    assert pluck([2, 4, 6, 8]) == [2, 0]
    assert pluck([2, 4, 6, 8, 10]) == [2, 0]
    assert pluck([1, 3, 5, 7, 9]) == []
    assert pluck([1, 3, 5, 7, 2]) == [2, 4]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14]) == [14, 7]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4, 6]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4, 6, 8]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4, 6, 8, 10]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4, 6, 8, 10, 12]) == [2, 8]
    