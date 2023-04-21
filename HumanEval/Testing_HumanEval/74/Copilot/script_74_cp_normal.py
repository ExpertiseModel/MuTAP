def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    '''
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

 # generate test case for the function above

def test_total_match():
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d"], ["a", "b", "c", "d"]) == ["a", "b", "c", "d"]
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d", "e"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d", "e"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d", "e", "f"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d", "e", "f"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d", "e", "f", "g"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d", "e", "f", "g"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d", "e", "f", "g", "h"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d", "e", "f", "g", "h"], ["a", "b", "c"]) == ["a", "b", "c"]