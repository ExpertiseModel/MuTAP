def add_elements(arr, k):
    
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)


# test case
def test():
    
    # Basic case

    assert add_elements([1, 2, 3, 4, 5], 2) == 7

    # Empty list
    
    assert add_elements([], 2) == 0

    # Outside range
    
    assert add_elements([1, 2, 3], 5)