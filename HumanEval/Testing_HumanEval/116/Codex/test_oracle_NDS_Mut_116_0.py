def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))



def test():
    assert sort_array([9, 9, 5, 5, 1, 1, 3, 3, 1, 3, 5, 5, 9, 9, 5, 5, 1, 1, 5, 5, 1, 1])   == [1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9, 9, 9, 9]

