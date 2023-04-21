def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


def test():
    assert next_smallest([0, 1, 2, 3]) == 1
    assert next_smallest([-1, 0, 1, 2, 3]) == 0
    assert next_smallest([4, 5, 6, 1, 2, 3]) == 2
