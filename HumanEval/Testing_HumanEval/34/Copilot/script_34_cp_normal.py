def unique(l: list):
    """Return sorted unique elements in a list
    """
    return sorted(list(set(l)))


METADATA = {}



 # generate test case for the function above


def test_unique():
    assert unique([]) == []
    assert unique([1]) == [1]
    assert unique([1, 1]) == [1]
    assert unique([1, 2]) == [1, 2]
    assert unique([1, 1, 2]) == [1, 2]
    assert unique([1, 2, 1]) == [1, 2]
    assert unique([1, 2, 2]) == [1, 2]
    assert unique([1, 2, 2, 1]) == [1, 2]
