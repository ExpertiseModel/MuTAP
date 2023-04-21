from script_70_cp_few_shot import strange_sort_list


def test_strange_sort_list():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert strange_sort_list([1, 2, 3]) == [1, 3, 2]
    assert strange_sort_list([1, 2]) == [1, 2]
    assert strange_sort_list([1]) == [1]
    assert strange_sort_list([]) == []


