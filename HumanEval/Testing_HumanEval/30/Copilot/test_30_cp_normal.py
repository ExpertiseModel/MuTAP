from script_30_cp_normal import get_positive

def test_get_positive():
    assert get_positive([1, 2, 3]) == [1, 2, 3]
    assert get_positive([1, 2, 3, 0]) == [1, 2, 3]
    assert get_positive([1, 2, 3, 0, -1, -2]) == [1, 2, 3]
    assert get_positive([1, 2, 3, 0, -1, -2, 4]) == [1, 2, 3, 4]
    assert get_positive([1, 2, 3, 0, -1, -2, 4, 5]) == [1, 2, 3, 4, 5]
    assert get_positive([1, 2, 3, 0, -1, -2, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert get_positive([1, 2, 3, 0, -1, -2, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert get_positive([1, 2, 3, 0, -1, -2, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert get_positive([1, 2, 3, 0, -1, -2, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert get_positive([1, 2, 3, 0, -1, -2, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]