from collections import OrderedDict


def remove_extras ( lst ) :
    return list ( OrderedDict . fromkeys ( lst ) )


def test():
    assert remove_extras([1, 2, 3]) == [1, 2, 3]
    assert remove_extras([1, 2, 2]) == [1, 2]
    assert remove_extras([1, 2, 3, 3]) == [1, 2, 3]
    assert remove_extras([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert remove_extras([5, 5, 1, 7, 7]) == [5, 1, 7]

test()