def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


# test case

def test():
    assert next_smallest([1, 2, 3]) == 2
    assert next_smallest([1, 2, 3, 4, 5]) == 2
