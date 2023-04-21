def strange_sort_list(lst):
    
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res


def test():
    assert strange_sort_list([3,4,4,1,1,3]) == [1, 4, 1, 4, 3, 3]
