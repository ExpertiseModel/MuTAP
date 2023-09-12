
def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared


# test case

def test():
    # Test 1: Simple list with positive integers
    assert sum_squares([1, 2, 3, 4, 5]) == 55

    # Test 2: List with negative integers
    assert sum_squares([-1, -2, -3, -4, -5]) == 55

    # Test 3: List with floating-point numbers
    assert sum_squares([3.14, 2.7, 1.8, 0.5, -0.2]) == 30

    # Test 4: List with empty list
    assert sum_squares([]) == 0

    # Test 5: List with invalid element
    assert sum_squares([1, 2, 3, 4, "apple"]) == None
    # Test 6: List with large numbers
