def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False


METADATA = {}



 # generate test case for the function above

def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([0, 0]) == True
    assert pairs_sum_to_zero([1, 2, 3, 4]) == False
    assert pairs_sum_to_zero([1, 2, 3, -2]) == True
    assert pairs_sum_to_zero([1, 2, 3, -3]) == True
    
