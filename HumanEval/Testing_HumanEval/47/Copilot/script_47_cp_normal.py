def median(l: list):
    """Return median of elements in the list l.
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


METADATA = {}



 # generate test case for the function above

def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4, 5, 6]) == 3.5
    assert median([1, 1, 3, 3, 5, 5]) == 3
    assert median([1, 1, 3, 3, 5, 5, 7, 7]) == 3.5
    assert median([1, 1, 3, 3, 5, 5, 7, 7, 9, 9]) == 5
    assert median([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11]) == 5.5
    assert median([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13]) == 7
    assert median([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]) == 8
    assert median([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17]) == 9
    assert median([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19]) == 10
    assert median([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21]) == 11