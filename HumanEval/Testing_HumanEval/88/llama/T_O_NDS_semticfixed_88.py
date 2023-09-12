def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 


# test case

def test():
    # Test with empty array
    assert sort_array([]) == []
    # Test with valid array
    assert sort_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    # Test with different number of elements
    arr = [1, 2, 3, 4, 5, 6]
    assert sort_array( [1, 2, 3, 4, 5, 6], reverse=(arr[0] + arr[-1]) % 2 == 0) == [1, 2, 3, 4, 5, 6]    # Test with arrays of different types
    arr = [1, 2, 3, 4, 5]
    assert sort_array(arr = [1, 2, 3, 4, 5], reverse=(arr[0] + arr[-1]) % 2 == 0) == [1, 2, 3, 4, 5]