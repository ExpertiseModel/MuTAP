def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m




# test case

def test():
    # Test 1: Valid list
    assert max_element([1, 2, 3, 4, 5]) == 5

    # Test 2: Multiple maximum elements
    assert max_element([1, 2, 3, 4, 5, 5]) == 5

    # Test 3: Negative values
    assert max_element([1, -2, -3, -4, -5]) == 1

    # Test 4: List with no elements
    assert max_element([]) == None
    # Test 5: List with duplicates
    assert max_element([1, 2, 2, 3, 3, 3]) == 3

    # Test 6: List with leading duplicates
    assert max_element([1, 2, 2, 3, 3, 3]) == 3

# Test 7: List with
