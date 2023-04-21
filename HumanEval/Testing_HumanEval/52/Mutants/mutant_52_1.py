def below_threshold(l: list, t: int):
    
    for e in l:
        if e <= t:
            return False
    return True


