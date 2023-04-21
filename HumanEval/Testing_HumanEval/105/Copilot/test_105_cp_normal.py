from script_105_cp_few_shot import by_length
def test_by_length():
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        "Nine",
        "Eight",
        "Seven",
        "Six",
        "Five",
        "Four",
        "Three",
        "Two",
        "One",
    ]
    assert by_length([1, 3, 5, 7, 9]) == [
        "Nine",
        "Seven",
        "Five",
        "Three",
        "One",
    ]
    assert by_length([2, 4, 6, 8]) == [
        "Eight",
        "Six",
        "Four",
        "Two",
    ]
    assert by_length([5, 6, 8, 9]) == [
        "Nine",
        "Eight",
        "Six",
        "Five",
    ]
    assert by_length([1, -1, 55]) == ["One"]
    assert by_length([0, 1, 2]) == ["Two", "One"]
