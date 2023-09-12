def add_elements(arr, k):
    
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)
assert add_elements([1, 2, 3, 4, 5], 2) == 3
