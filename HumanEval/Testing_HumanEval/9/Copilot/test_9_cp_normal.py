from script_9_cp_few_shot import rolling_max

def test_rolling_max():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert rolling_max([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert rolling_max([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]