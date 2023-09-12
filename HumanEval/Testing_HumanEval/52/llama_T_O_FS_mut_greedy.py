def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True


assert below_threshold([1, 2, 3], 4) == True
assert below_threshold([1, 2, 3], 3) == False
