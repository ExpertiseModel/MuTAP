def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 
assert sort_array( [1, 2, 3, 4, 5, 6], reverse=(arr[0] + arr[-1]) % 2 == 0) == [1, 2, 3, 4, 5, 6]# Test with arrays of different types
