from script_22_cp_few_shot import filter_integers


def test_filter_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([1.0, 2.0, 3.0, 4.0, 5.0]) == []
    assert filter_integers([1.0, 2, 3.0, 4, 5.0]) == [2, 4]
    assert filter_integers(["1", "2", "3", "4", "5"]) == []
    assert filter_integers(["1", "2", "3", "4", "5", 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([True, False, 1, 0]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0"]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0", "True", "False"]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0", "True", "False", 0.0, 0.1]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0", "True", "False", 0.0, 0.1, 1.0, 2.0, 3.0]) == [1, 0]


