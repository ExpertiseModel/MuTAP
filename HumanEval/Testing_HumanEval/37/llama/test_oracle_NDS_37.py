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




# test case
def test():
    #empty list
    assert sort_even([]) == []
    
    #single element list
    assert sort_even([1]) == [1]
    
    #list with odd elements
    assert sort_even([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    
    #list with even elements
    assert sort_even([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    
    #list with mix of odd and even elements
    assert sort_even([1, 3, 5, 7, 2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 10]