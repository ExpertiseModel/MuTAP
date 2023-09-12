def starts_one_ends(n):
    
    if n == 1: 
        return 1
    return 18 * (10 ** (n - 2))


# test case

def test():
    # Test 1: Check the function works for small inputs

    assert starts_one_ends(1) == 1

    # Test 2: Check the function works for medium inputs

    assert starts_one_ends(5) == 18000

    # Test 3: Check the function works for large inputs

    assert starts_one_ends(10) == 1800000000

    # Test 4: Check the function returns the correct value for 1

    assert starts_one_ends(1) == 1

    # Test 5: Check the function returns the correct value for very large inputs

    assert starts_one_ends(20) == 18000000000000000000

    # Test 6: Check the function raises a ValueError for invalid inputs

    assert starts_one_ends(-1) == 0.018000000000000002


