def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 



def test():
    assert sort_array([3,4,5]) == [5,4,3]
    assert sort_array([4,5,1,2]) == [5,4,2,1]
    assert sort_array([1,2,3,4,5,6]) == [1,2,3,4,5,6]
    assert sort_array([3,4,5,6,7,8,1,2]) == [1,2,3,4,5,6,7,8]
  
