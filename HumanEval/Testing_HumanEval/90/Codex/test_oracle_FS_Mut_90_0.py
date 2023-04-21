def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]



def test():
    assert next_smallest([-1, 0, 1, 2, 3]) == 0
    assert next_smallest([1,1,1,1,1]) == None
    assert next_smallest([1,2,3,4,5]) == 2
    assert next_smallest([5,5,5,5,1]) == 2

