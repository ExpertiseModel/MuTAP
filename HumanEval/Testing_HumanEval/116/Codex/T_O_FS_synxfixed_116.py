def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

def test():
    assert sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 5, 3, 6, 7]
    assert sort_array([4, 6, 2, 1, 7, 9, 8]) == [1, 2, 4, 6, 8, 7, 9]
