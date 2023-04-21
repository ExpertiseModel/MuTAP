from script_62_cp_few_shot import derivative


def test_derivative():
    assert derivative([1]) == []
    assert derivative([1, 2]) == [2]
    assert derivative([1, 1, 1]) == [1, 2]
    assert derivative([1, 1, 1, 1]) == [1, 2, 3]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([1, 2, 3, 4]) == [2, 6, 12]
    assert derivative([1, 0, 0, 0, 0]) == [0, 0, 0]
    assert derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 6, 12, 20, 30, 42, 56, 72, 90]




