from script_37_cp_few_shot import sort_even


def test_sort_even():
    assert sort_even([]) == []
    assert sort_even([1]) == [1]
    assert sort_even([1, 2]) == [1, 2]
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert sort_even([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_even([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert sort_even([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


