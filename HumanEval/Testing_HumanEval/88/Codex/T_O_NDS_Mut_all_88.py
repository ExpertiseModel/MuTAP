def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 



def test():

    assert sort_array([1]) == [1]
    assert sort_array([3, 2, 1]) == [3, 2, 1]
    assert sort_array([1, 2, 3]) == [3, 2, 1]
    assert sort_array([1, 1, 3, 3, 3, 2, 4, 2, 1]) == [4, 3, 3, 3, 2, 2, 1, 1, 1]
    assert sort_array([1, 2]) == [1, 2]
    assert sort_array([2, 1]) == [1, 2]
    assert sort_array([-1, -1]) == [-1, -1]
    assert sort_array([-1, -2]) == [-2, -1]
    assert sort_array([-1, -2]) == [-1, -2]
    assert sort_array([1, 2]) == [1, 2]
    assert sort_array([1, 2]) == [1, 2]
    assert sort_array([]) == []
    assert sort_array([1, 2]) == [1, 1]
    assert sort_array([1, 1]) == [1, 1]

