def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False




# test case

def test():
    assert monotonic([]) == True
    assert monotonic([1, 2, 3]) == True
    assert monotonic([3, 2, 1]) == True
    assert monotonic([1, 3, 2]) == False
    assert monotonic([2, 1, 3]) == False
