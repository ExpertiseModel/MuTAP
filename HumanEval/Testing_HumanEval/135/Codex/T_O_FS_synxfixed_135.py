def can_arrange(arr):
    
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind

def test():
    assert can_arrange([3, 2, 1]) == None
    assert can_arrange([4, 3, 2, 1]) == None
    assert can_arrange([4, 3, 2, 1, 10, 5, 6, 7, 8, 9]) == 1
    assert can_arrange([4, 3, 2, 1, 10, 5, 6, 7, 8, 9, -1]) == 8
    assert can_arrange([]) == None
