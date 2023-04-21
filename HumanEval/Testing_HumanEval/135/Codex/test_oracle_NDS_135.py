def can_arrange(arr):
    
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind

def test():
    assert not
    assert 
    assert 
    assert 
    assert not 
    assert 
    assert not 
    assert 

test()
