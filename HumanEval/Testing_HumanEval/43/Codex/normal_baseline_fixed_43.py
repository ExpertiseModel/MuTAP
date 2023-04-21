def pairs_sum_to_zero(l):
    
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False




def test():
    # all of the test cases should pass
    assert pairs_sum_to_zero([1, 3, -1]) == True
    assert pairs_sum_to_zero([1, 3, 5]) == False
