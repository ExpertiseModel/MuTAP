def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False




def test():
    assert monotonic([2,3,3,2,2,5]) == False
    assert monotonic([1,2,1,1,1,1]) == False
    assert monotonic([-1, -2, -3, -4, -4, -5]) == True
    assert monotonic([1,1,1,1,2,2,3,3,3]) == True
    assert monotonic(['a','a','a','a','b','b','c']) == True
    assert monotonic(['a','a','a','b','b','c']) == True
    assert monotonic(['a','a','a','a','b','c']) == True
    assert monotonic(['a','b','c','c']) == True
