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

    assert sort_even([1,2,3,4,5,6,7,8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_even([]) == []
    assert sort_even([1,2,3,4,5,6,7,8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_even([]) == []
    assert sort_even([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_even([1, 3, 5]) == [1, 3, 5]
    assert sort_even([5, 3, 1]) == [5, 3, 1]
    assert sort_even([3, 1, 5]) == [3, 1, 5]
    assert sort_even([2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]
    assert sort_even([1, 2, 3, 4,

    assert sort_even([1,2,3,4,5,6,7,8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_even([]) == []

