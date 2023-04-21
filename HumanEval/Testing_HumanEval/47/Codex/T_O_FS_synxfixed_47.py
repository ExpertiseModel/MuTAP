def median(l: list):
    
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0



def test():
    assert median([1, 2, 3, 4]) == 2.5
    assert median([1, 5, 3, 4, 2, 6, 9]) == 3.5
    assert median([1]) == 1
    assert median([]) == None
