def sorted_list_sum(lst):
    
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)


#</code>
#<test>

def test():
    assert sorted_list_sum([]) == []


    assert sorted_list_sum([1]) == [1]

    assert sorted_list_sum([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert sorted_list_sum([3, 5, 7, 9]) == [3, 5, 7, 9]
    assert sorted_list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]