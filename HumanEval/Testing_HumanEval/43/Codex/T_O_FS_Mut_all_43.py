def pairs_sum_to_zero(l):
    
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False





def test():

    assert pairs_sum_to_zero([2, 3, -7, -8, -9, -1]) == False
    assert pairs_sum_to_zero([-2, -3, -7, -8, -9, -1]) == False
    assert pairs_sum_to_zero([-1, -2, -7, -8, -9, -2]) == False
    assert pairs_sum_to_zero([-2, -3, -1, -8, -9, -1]) == False
    assert pairs_sum_to_zero([-2, -3, -1, -8, -9, -1, -4]) == False
    assert pairs_sum_to_zero([-2, -3, -1, -3, -8, -9, -1]) == False
    assert pairs_sum_to_zero([-2, -3, -7, -8, -9, -1]) == False
    assert pairs_sum_to_zero([-1, -2, -7, -8, -9, -2]) == False
    assert pairs_sum_to_zero([-2, -3, -1, -8, -9, -1]) == True
    assert pairs_sum_to_zero([-2, -3, -1, -8, -9, -1, -4]) == True

