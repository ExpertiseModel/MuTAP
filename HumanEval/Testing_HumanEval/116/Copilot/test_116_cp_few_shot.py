from script_116_cp_few_shot import sort_array
def test_sort_array():
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 4, 8, 3, 5, 6, 9, 10, 7]
    assert sort_array([2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 8, 3, 5, 6, 9, 10, 7]
    assert sort_array([2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 8, 3, 5, 6, 9, 7]
    assert sort_array([2, 3, 4, 5, 6, 7, 8]) == [2, 4, 8, 3, 5, 6, 7]
    assert sort_array([2, 3, 4, 5, 6, 7]) == [2, 4, 3, 5, 6, 7]
    assert sort_array([2, 3, 4, 5, 6]) == [2, 4, 3, 5, 6]
    assert sort_array([2, 3, 4, 5]) == [2, 4, 3, 5]
    assert sort_array([2, 3, 4]) == [2, 4, 3]
    assert sort_array([2, 3]) == [2, 3]
    assert sort_array([2]) == [2]
    assert sort_array([3]) == [3]
    assert sort_array([]) == []