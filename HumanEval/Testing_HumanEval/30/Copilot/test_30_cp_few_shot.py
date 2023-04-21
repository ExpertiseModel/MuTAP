from script_30_cp_few_shot import get_positive


def test_get_positive():
    assert get_positive([]) == []
    assert get_positive([1, 2, 3]) == [1, 2, 3]
    assert get_positive([-1, -2, -3]) == []
    assert get_positive([1, -2, -3]) == [1]
    assert get_positive([-1, 2, -3]) == [2]
    assert get_positive([-1, -2, 3]) == [3]
    assert get_positive([1, 2, -3]) == [1, 2]
    assert get_positive([-1, 2, 3]) == [2, 3]
    assert get_positive([1, -2, 3]) == [1, 3]


