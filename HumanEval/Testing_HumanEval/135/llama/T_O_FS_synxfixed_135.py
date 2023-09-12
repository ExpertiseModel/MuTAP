def can_arrange(arr):
    
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind




#<test>
def test():
 
    assert can_arrange([3, 2, 1, 4, 5, 6]) == 3
    
    assert can_arrange([1, 2, 3, 4, 5, 6]) == 2
    
    assert can_arrange([3, 4, 5, 2, 1, 6]) == 2
    
    assert can_arrange([3, 2, 1, 4, 5, 6]) == 3