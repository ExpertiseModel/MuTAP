def monotonic(l: list):
    
    if not ((l == sorted(l) or l == sorted(l, reverse=True))):
        return True
    return False


