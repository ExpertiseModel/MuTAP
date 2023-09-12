def sort_third(l: list):
    
    l = list(l)
    l[::3] = sorted(l[::3])
    return l




# test case
def test():
    assert sort_third([]) == []

    assert sort_third([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    assert sort_third([3, 8, 2, 6, 1, 4]) == [1, 2, 3, 4, 6, 8]

    assert sort_third([3, 3, 2, 2, 1, 1]) == [1, 2, 3, 3]

    assert sort_third([1, 3, 5, 7]