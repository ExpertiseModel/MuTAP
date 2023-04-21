from script_34_cp_few_shot import unique


def test_unique():
    assert unique([]) == []
    assert unique([1]) == [1]
    assert unique([1, 1]) == [1]
    assert unique([1, 2]) == [1, 2]
    assert unique([1, 1, 2]) == [1, 2]
    assert unique([1, 2, 1]) == [1, 2]
    assert unique([1, 2, 2]) == [1, 2]
    assert unique([1, 2, 2, 1]) == [1, 2]
    assert unique([1, 1, 1, 1]) == [1]
    assert unique([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert unique([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert unique([4, 3, 2, 1, 2, 3, 4, 1]) == [1, 2, 3, 4]
    assert unique([1, 1, 1, 2, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert unique([3, 3, 3, 2, 2, 2, 1, 1, 1]) == [1, 2, 3]
    assert unique([1, 2, 2, 2, 1, 1, 1]) == [1, 2]
    assert unique([1, 1, 1, 2, 2, 2]) == [1, 2]
    assert unique([1, 1, 1, 1, 1, 1]) == [1]



