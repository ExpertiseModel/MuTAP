def monotonic(l: list):
    
    if (l == sorted(l) and l == sorted(l, reverse=True)):
        return True
    return False


