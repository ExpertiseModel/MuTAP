from script_105_cp_few_shot import by_length

def test_by_length():
    assert by_length([1, 3, 5, 7, 9]) == ["Nine", "Seven", "Five", "Three", "One"]
    assert by_length([2, 4, 6, 8]) == ["Eight", "Six", "Four", "Two"]
    assert by_length([1, 2, 3, 5, 3, 2, 9, 1, 2, 3]) == ["Nine", "Three", "Three", "Three", "Two", "Two", "Two", "One", "One"]
    assert by_length([]) == []
    assert by_length([1]) == ["One"]
    assert by_length([-1]) == []
    assert by_length([0]) == []
    assert by_length([1, -1, 55, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]