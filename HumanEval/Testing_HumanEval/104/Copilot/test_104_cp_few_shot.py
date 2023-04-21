from script_104_cp_few_shot import unique_digits
def test_unique_digits():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
    assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
    assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 3, 5, 7, 9, 11]
    assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]) == [1, 3, 5, 7, 9, 11, 13]