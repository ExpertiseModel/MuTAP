def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])


# test case
def test():
    
    # Test 1: Valid grid, valid capacity

    assert max_fill([1, 2, 3, 4, 5], 2) == 7

    # Test 2: Valid grid, invalid capacity

    assert max_fill([1, 2, 3, 4, 5], 3) == 5

    # Test 3: Invalid grid

    assert max_fill([1, 2, 3, 4, 5, 6, 7, 8], 2) == 6

    # Test 4: Valid grid, valid capacity

    assert max_fill([1, 2, 3, 4, 5], 3) == 6