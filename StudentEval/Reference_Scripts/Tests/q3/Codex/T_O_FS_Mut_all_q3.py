

def remove_extras(lst):
    newlist = []
    for i in lst:
        if i not in newlist:
            newlist.append(i)
    return newlist


def test():
    assert remove_extras([1, 1, 2, 1, 1]) == [1, 2]
    assert remove_extras([1, 1, 2, 2, 3, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_extras([1, 1, 2, 2, 3, 3, 4, 4]) == [1, 2, 3, 4]
    assert remove_extras([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5]) == [1, 2, 3, 4, 5]
    assert remove_extras([1, 1, 1, 1, 1]) == [1]
    assert remove_extras([1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == [1, 2, 3, 4, 5]
    assert remove_extras([]) == []
   