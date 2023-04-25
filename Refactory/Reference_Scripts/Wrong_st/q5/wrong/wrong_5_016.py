def top_k(lst, k):
    
    if lst == []:
        return lst
    
    lower = []
    higher = []
    plist = []
    
    pivot = lst[0]
    for e in lst:
        if e < pivot:
            lower.append(e)
        if e == pivot:
            plist.append(e)
        if e > pivot:
            higher.append(e)
    sort_list = lower + plist + higher
    sort_list = sort_list[::-1]
    
    if k == len(lst):
        return sort_list[:k-1]
    elif k > len(lst):
        return sort_list
    else:
        return sort_list[:k]
