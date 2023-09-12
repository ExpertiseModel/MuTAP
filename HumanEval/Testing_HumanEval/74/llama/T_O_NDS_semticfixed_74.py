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


# test case

def test():
    assert total_match(['hello', 'world'], ['world', 'hello']) == ['hello', 'world']

    assert total_match(['hello', 'world'], ['apple', 'banana']) == ['hello', 'world']

    assert total_match(['hello', 'world'], ['hello', 'world']) == ['hello', 'world']

