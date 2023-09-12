def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False






def test():
    assert monotonic([3, 2, 1, 4, 5, 6]) == False
   
    assert monotonic([3, 2, 1, 4, 5, 6, 10]) == False
   
    assert monotonic([3, 2, 1, 4, 5, 6, 10, 7]) == False
    
    assert monotonic([1, 2, 3, 4, 5, 6, 7]) == True
   
    assert monotonic([3, 2, 1, 4, 5, 6, 10, 7, 8]) == False
