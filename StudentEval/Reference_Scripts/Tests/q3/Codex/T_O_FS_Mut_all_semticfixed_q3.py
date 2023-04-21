

def remove_extras(lst):
    newlist = []
    for i in lst:
        if i not in newlist:
            newlist.append(i)
    return newlist



def test():
    assert remove_extras([1, 2, 3]) == [1, 2, 3]
    assert remove_extras([1, 2, 2]) == [1, 2]
    assert remove_extras([1, 2, 3, 3]) == [1, 2, 3]
    assert remove_extras([5, 5, 1, 7, 7]) == [5, 1, 7]
    assert remove_extras([1, 2, 'b', 'b']) == [1, 2, 'b']
    assert remove_extras([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert remove_extras(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert remove_extras([]) == []
    assert remove_extras([1, 2, 2]) == [1, 2]
    assert remove_extras([1, 2, 3, 3]) == [1, 2, 3]
    assert remove_extras([1, 2, 3]) == [1, 2, 3]
    assert remove_extras([1, 2, 2]) == [1, 2]
    assert remove_extras([1, 2, 3, 3]) == [1, 2, 3]
    assert remove_extras([1, 1, 1, 1, 1]) == [1]
    assert remove_extras([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert remove_extras([5, 5, 1, 7, 7]) == [5, 1, 7]