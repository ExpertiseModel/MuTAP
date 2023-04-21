def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

def test():
    assert next_smallest([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 21
     
    assert next_smallest([1,2,1,1,1]) == 3
     
    assert next_smallest([1,1,1,1,1]) == 2
     
    assert next_smallest([1,2,3,4,5]) == 6
     
    assert next_smallest([1,2,3,4,5,4,4,4]) == 6
     
    assert next_smallest([1,3,3,3,3,3,3,3]) == 4
     
    