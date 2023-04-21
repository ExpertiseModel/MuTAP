def strange_sort_list(lst):
    
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

def test():
    assert len(strange_sort_list([1, 2, 3, 4])) == 4
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([5]) == [5]
    assert strange_sort_list([100, 15, 16, 17, 1]) == [1, 100, 15, 16, 17]
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    return 'tests pass'

print(test())
