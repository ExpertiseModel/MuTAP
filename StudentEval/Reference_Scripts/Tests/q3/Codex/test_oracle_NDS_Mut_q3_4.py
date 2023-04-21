

def remove_extras(lst):
    newlist = []
    for i in lst:
        if i not in newlist:
            newlist.append(i)
    return newlist



def test():
    assert remove_extras([1, 2, 2]) == [1, 2]
    assert remove_extras([1, 2, 3, 3]) == [1, 2, 3]
    try:
        assert remove_extras([5, 5, 1, 7, 7]) == [5, 1, 7]
        print("Good")
    except:
        print("Bad")
