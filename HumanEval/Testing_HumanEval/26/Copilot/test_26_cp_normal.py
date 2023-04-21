from script_26_cp_normal import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1]) == [2, 3, 4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1, 2]) == [3, 4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3]) == [4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3, 4]) == [5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [2]
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == []
    assert remove_duplicates([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == []