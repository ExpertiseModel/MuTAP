
def can_arrange(arr):
    
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind


# test case
def test():
    
    # Test with a properly sorted list
    assert can_arrange([3, 2, 1, 4]) == 1

    # Test with a list that is not sorted
    assert can_arrange([4, 1, 2, 3]) == -1

    # Test with a list that is almost sorted
    assert can_arrange([3, 2, 1, 4, 4]) == 2

    # Test with an empty list
    assert can_arrange([]) == -1

    # Test with a list that goes out of range