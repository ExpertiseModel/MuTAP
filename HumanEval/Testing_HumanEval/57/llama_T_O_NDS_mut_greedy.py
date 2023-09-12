def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


assert monotonic([1, 2, 3]) == True
assert monotonic([3, 2, 1]) == True
