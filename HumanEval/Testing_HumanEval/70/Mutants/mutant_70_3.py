def strange_sort_list(lst):
    
    res, switch = [], True
    while not lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res
