def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


# test case


def test():
    # Test 1: Valid list, valid result
    assert next_smallest([1, 2, 3]) == 2

    # Test 2: Valid list, invalid result
    assert next_smallest([1, 2, 3, 4]) == 2

    # Test 3: Invalid list, invalid result
    assert next_smallest([1, 2, 3]) == 2

    # Test 4: Valid list, valid result (second smallest)
    assert next_smallest([1, 2, 3, 4, 5]) == 2

    # Test 5: Valid list, valid result (third smallest)
    assert next_smallest([1, 2, 3, 4, 5, 6]) == 2

