def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True


assert below_threshold([1.0, 2.0, 3.0, 4.0, 5.0], 10) == True
