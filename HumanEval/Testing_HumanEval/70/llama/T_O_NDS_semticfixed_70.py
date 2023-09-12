def strange_sort_list(lst):
    
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res


# test case

def test():
    assert strange_sort_list([ ]) == [ ]

    assert strange_sort_list([1]) == [1]

    assert strange_sort_list([1, 2, 2, 3, 3]) == [1, 3, 2, 3, 2]

    assert strange_sort_list([3, 2, 2, 1, 1]) == [1, 3, 1, 2, 2]

    assert strange_sort_list([-2, -1, 0, 1, 2]) == [-2, 2, -1, 1, 0]


