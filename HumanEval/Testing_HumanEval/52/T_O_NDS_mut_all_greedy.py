def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True


assert below_threshold([2, 2, 2], 2) == False
assert below_threshold([3, 3, 3], 2) == False
