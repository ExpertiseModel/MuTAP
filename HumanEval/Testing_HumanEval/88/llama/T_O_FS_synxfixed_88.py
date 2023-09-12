def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 


#</code>
#<test>
def test():
   
    assert sort_array([]) == []

    assert sort_array([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    assert sort_array([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    assert sort_array([-1, -2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2, -1]
