def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


# test case
def test():
    assert sort_array([]) == []
    
    assert sort_array(arr[2, 6, 3, 1, 4]) == [1, 2, 3, 4, 6]

    assert sort_array([2, 2, 6, 3, 1, 4]) == [1, 2, 2, 3, 4, 6]

    assert sort_array(['a', 'b', 'c', 'd', 'e', 'f']) == ['a', '