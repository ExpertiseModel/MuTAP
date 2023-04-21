def sort_third(l: list):
    
    l = list(l)
    l[::3] = sorted(l[::3])
    return l




def test():
    assert sort_third([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_third([5, 3, 4, 2, 1, 0]) == [2, 3, 4, 5, 1, 0]
    assert sort_third([3, 1, 5, 2, 0, 4]) == [2, 1, 5, 3, 0, 4]
    assert sort_third([1, 5, 3, 0, 2, 4]) == [0, 5, 3, 1, 2, 4]
