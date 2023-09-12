def unique(l: list):
    
    return sorted(list(set(l)))




# test case
def test():
    #test_empty_list
    assert unique([]) == [ ]

    #test_empty_set()
    assert unique([]) == [ ]

    #test_list_with_unique_elements
    assert unique([1, 2, 2, 3, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

    #test_list_with_duplicates
    assert unique([1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]

    #test_list_with_irrelevant_elements():
    assert unique([1, 2, 2, 3, 3, 4, 4, 5, 'apple', 'banana']) ==