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
    assert pairs_sum_to_zero([7, 1, 2, -3]) == False
    assert pairs_sum_to_zero([-1, 0, 1]) == False

   # Test that the function returns False for a pair of numbers that sum to 0 when both numbers are negative
    assert pairs_sum_to_zero([-2, -3]) == False

   # Test that the function returns True for a pair of numbers that sum to 0 when both numbers are positive
    assert pairs_sum_to_zero([2, 3]) == True

    assert pairs_sum_to_zero([6, 7, 8, 9, 10]) == False

    # Test that the corrected function returns True for a pair of numbers that sum to 0
    assert pairs_sum_to_zero([-1, -2]) == True

    # Test that the corrected function works for a list of positive and negative numbers
    assert pairs_sum_to_zero([-1, 2, -3, 4, -5]) == False
    assert pairs_sum_to_zero([1, 2, 3, 4, 5]) == False

  


