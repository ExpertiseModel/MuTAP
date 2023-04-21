from script_43_cp_normal import pairs_sum_to_zero

def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([0, 0]) == True
    assert pairs_sum_to_zero([1, 2, 3, 4]) == False
    assert pairs_sum_to_zero([1, 2, 3, -2]) == True
    assert pairs_sum_to_zero([1, 2, 3, -3]) == True
    
