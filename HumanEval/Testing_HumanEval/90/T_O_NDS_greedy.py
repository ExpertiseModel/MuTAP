def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]
assert next_smallest([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 2
assert next_smallest([1,2,1,1,1]) == 2
