def median(l: list):
    
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0




# test case

def test():
    assert median([1]) == 1
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([5, 4, 3, 2, 1]) == 3
