from script_108_cp_normal  import count_nums
def test_count_nums():
    assert count_nums([1, 2, 3]) == 3
    assert count_nums([1, -2, 3]) == 2
    assert count_nums([-1, -2, -3]) == 0
    assert count_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 11
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 13
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 14
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 17
