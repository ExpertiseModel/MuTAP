from script_34_cp_normal import unique


def test_unique():
    assert unique([]) == []
    assert unique([1]) == [1]
    assert unique([1, 1]) == [1]
    assert unique([1, 2]) == [1, 2]
    assert unique([1, 1, 2]) == [1, 2]
    assert unique([1, 2, 1]) == [1, 2]
    assert unique([1, 2, 2]) == [1, 2]
    assert unique([1, 2, 2, 1]) == [1, 2]
