def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False



def test():
    assert monotonic([]) == True
    assert monotonic([1]) == True
    assert monotonic([1, 2, 3]) == True
    assert monotonic([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]) == True
    assert monotonic([3, 2, 1, 1, 5, 7, 6, 5, 5]) == False
    assert monotonic([1, 1, 1, 1, 1, 2, 3, 4, 5]) == False
