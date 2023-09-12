def sorted_list_sum(lst):
    
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)


# test case

def test():
    # Test case 1: Valid list
    assert sorted_list_sum([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Test case 2: List with odd-length elements
    assert sorted_list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Test case 3: List with even-length elements
    assert sorted_list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Test case 4:
