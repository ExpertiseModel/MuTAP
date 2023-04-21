from script_9_cp_few_shot import rolling_max

def test_rolling_max():
    assert rolling_max([]) == []
    assert rolling_max([1]) == [1]
    assert rolling_max([1, 2]) == [1, 2]
    assert rolling_max([2, 1]) == [2, 2]
    assert rolling_max([1, 2, 3]) == [1, 2, 3]
    assert rolling_max([3, 2, 1]) == [3, 3, 3]
    assert rolling_max([1, 3, 2]) == [1, 3, 3]
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
    assert rolling_max([5, 1, 4, 2, 3]) == [5, 5, 5, 5, 5]
    assert rolling_max([5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert rolling_max([5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6]