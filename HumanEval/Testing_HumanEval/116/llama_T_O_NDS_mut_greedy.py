def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
assert sort_array([2, 6, 3, 1, 4]) == [1, 2, 3, 4, 6]
