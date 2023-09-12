def strange_sort_list(lst):
    
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res
assert strange_sort_list([1, 2, 2, 3, 3]) == [1, 3, 2, 3, 2]
