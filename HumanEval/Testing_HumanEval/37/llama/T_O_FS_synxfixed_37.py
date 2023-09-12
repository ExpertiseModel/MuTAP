def sort_even(l: list):
    
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans




def test():
    assert sort_even([]) == []

    assert sort_even([1]) == [1]

    assert sort_even([1, 2, 3, 4, 5]) == [1, 3, 5, 2, 4]

    assert sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_even( [1, 3, 5, 7]) == [1, 3, 5, 7]
    assert sort_even([2, 4, 6, 8]) == [2, 4, 6, 8]
