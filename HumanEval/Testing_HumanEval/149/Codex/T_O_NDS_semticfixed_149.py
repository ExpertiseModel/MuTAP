def sorted_list_sum(lst):
    
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)


def test():
    assert sorted_list_sum([[1, 2, 3], [4, 5, 6], [1], [9, 9, 9, 9]]) == [[9, 9, 9, 9]]
