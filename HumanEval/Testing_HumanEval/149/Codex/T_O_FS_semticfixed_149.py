def sorted_list_sum(lst):
    
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)


def test():
    assert sorted_list_sum([1, 10]) == 10    
    assert sorted_list_sum([2, 3, -6, -1]) == 0    
    assert sorted_list_sum([0, 3, -3, -5]) == -3    
    assert sorted_list_sum([-5, -1, -6, -4]) == -4    
    assert sorted_list_sum([]) == []
    assert sorted_list_sum([1, 1, 1, 1, 1, 1]) == 0