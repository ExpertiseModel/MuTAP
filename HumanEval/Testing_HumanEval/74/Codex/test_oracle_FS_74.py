def total_match(lst1, lst2):
   
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2

def test():
    assert total_match(["abc"], ["abc"]) == ["abc"]
    assert total_match(["abc", "a"], ["abc"]) == ["abc"]
    assert total_match(["abc", "a"], ["abc", ""]) == ["abc", ""]
