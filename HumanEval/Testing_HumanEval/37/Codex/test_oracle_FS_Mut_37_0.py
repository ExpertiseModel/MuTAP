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
    assert sort_even([2, 1, 3, 4, 5, 7, 8, 10, 12]) == [1, 2, 3, 4, 5, 7, 8, 10, 12]
    # the new code
    assert sort_even([]) == []
    assert sort_even([2, 1, 3, 4, 5, 7, 8, 10, 12]) == [1, 2, 3, 4, 5, 7, 8, 10, 12]
    assert sort_even([2, 1, 3, 4, 5, 7, 8, 10, 12]) == [1, 2, 3, 4, 5, 7, 8, 10, 12]


