def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 



def test():
    sort_array([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    assert sort_array([3, 4, 5, 6, 7, 8, 1, 2]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_array([-1, 2, 3, 4, -5, -6]) == [-6, -5, -1, 2, 3, 4]
    assert sort_array([3, 4, 5, 6, 7, 8, 1, 2]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_array([]) == []
  
    print("all test finished")
    
    return
