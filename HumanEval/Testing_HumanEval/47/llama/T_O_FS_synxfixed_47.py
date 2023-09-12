def median(l: list):
    
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0




#</code>
#<test>
def test():
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 3
    assert median([1, 2, 3, 4, 5]) == 4

    assert median([]) == None

    assert median(['a']) == 'a'

    assert median(['a', 'b', 'c']) == 'b'

    assert median(['a', 'b', 'c', 'd']) == 'c'

    assert median(['a', 'b', 'c', 'd', 'e']) == 'c + d / 2.0'

    assert median([1, 2, 3, 'a', 4, 5]) == '3 + (2 + 4) / 2.0'