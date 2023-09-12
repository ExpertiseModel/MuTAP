def pairs_sum_to_zero(l):
    
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False




# test case

def test():
    # Test that the function returns True for a pair of numbers that sum to 0
    assert pairs_sum_to_zero([1, 2, 3, 4, 5]) == False

   # Test that the function returns False for a non-existent pair of numbers that sum to 0
    assert pairs_sum_to_zero([6, 7, 8, 9, 10]) == False

   # Test that the function works for a list of negative numbers
    assert pairs_sum_to_zero([-1, -2, -3, -4, -5]) == False

# Test that the function works for a list of positive and negative
