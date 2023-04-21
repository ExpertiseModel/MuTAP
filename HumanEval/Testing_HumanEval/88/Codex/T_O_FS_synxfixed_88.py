def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 

def test():
    assert sort_array([1, 2, 3, 4, 5, 6]) == [1, 3, 5, 6, 2, 4]
    assert sort_array([3, 4, 5, 6, 7, 8, 1, 2]) == [1, 2, 3, 4, 5, 6, 7, 8]
