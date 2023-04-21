from script_43_cp_few_shot import pairs_sum_to_zero



def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([0, 0]) == True
    assert pairs_sum_to_zero([0]) == False
    assert pairs_sum_to_zero([]) == False
    assert pairs_sum_to_zero([1, 2, 3, 4]) == False
    assert pairs_sum_to_zero([1, 2, 3, -2]) == True
    assert pairs_sum_to_zero([1, 2, 3, -3]) == True
    assert pairs_sum_to_zero([1, 2, 3, -1]) == True
    assert pairs_sum_to_zero([1, 2, 3, 0]) == False
    assert pairs_sum_to_zero([1, 2, 3, -4]) == False
    assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -4]) == False
    assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -4, -8]) == True





