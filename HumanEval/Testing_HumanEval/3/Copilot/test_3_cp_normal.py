from script_3_cp_few_shot import below_zero

def test_below_zero():
    assert below_zero([1, 2, 3, -1, -2, -3]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1, 2]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1, 2, 3]) == False