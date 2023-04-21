def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.
    '''
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

 # generate test case for the function above

def test_strange_sort_list():
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert strange_sort_list([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7]) == [1, 7, 2, 6, 3, 5, 4]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 8, 2, 7, 3, 6, 4, 5]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7]