from script_26_cp_few_shot import remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2]) == [1, 2]
    assert remove_duplicates([1, 2, 2]) == [1]
    assert remove_duplicates([1, 1, 2, 2]) == []
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 2, 3, 4, 1, 2, 3, 4]) == []
    assert remove_duplicates([1, 2, 3, 4, 1, 2, 3, 4, 5]) == [5]



