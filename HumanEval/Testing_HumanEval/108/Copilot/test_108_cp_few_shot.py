from script_108_cp_normal import count_nums
def test_count_nums():
    assert count_nums([1, 2, 3, 4, 5]) == 5
    assert count_nums([-1, 2, 3, 4, 5]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([-1, -2, -3, -4, -5, 100]) == 1
    assert count_nums([1, 2, 3, 4, 5, -100]) == 5
    assert count_nums([1, 2, 3, 4, 5, -100, -1000, 1000]) == 6
    assert count_nums([-1, -2, -3, -4, -5, -100, -1000, -1000]) == 0
    assert count_nums([1, 2, 3, 4, 5, -100, -1000, -1000, 1000, 10000]) == 7
    assert count_nums([1, 2, 3, 4, 5, -100, -1000, -1000, 1000, 10000, -12345]) == 7
    assert count_nums([1, 2, 3, 4, 5, -100, -1000, -1000, 1000, 10000, -12345, 12345]) == 8
