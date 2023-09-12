def add_elements(arr, k):
    
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)


# test case

def test():
    assert add_elements([], 2) == 0
    assert add_elements([1, 2, 3], 5)
