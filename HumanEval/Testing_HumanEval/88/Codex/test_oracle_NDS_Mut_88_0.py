def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 



def test():
    sort_array([-1, -2])
    assert sort_array([-1, -2]) == [-1, -2]
    assert sort_array([1, 2]) == [1, 2]
    assert sort_array([1, 2]) == [1, 2]
    assert sort_array([]) == []
    assert sort_array([1, 2]) == [1, 1]
    assert sort_array([1, 1]) == [1, 1]
    
    ValueError: invalid literal for int() with base 10: