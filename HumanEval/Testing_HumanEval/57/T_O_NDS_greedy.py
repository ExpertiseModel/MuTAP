def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


assert monotonic([2,3,3,2,2,5]) == False
assert monotonic([-1, -2, -3, -4, -4, -5]) == True
