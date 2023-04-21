def test_remove_extras():
    assert remove_extras([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_extras([1, 1, 1, 1, 1]) == [1]
    assert remove_extras([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert remove_extras([1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 3]
    assert remove_extras([1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]