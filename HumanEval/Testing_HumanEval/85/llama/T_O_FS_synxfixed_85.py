def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


#</original code>


def test():
    assert add([]) == []
    assert add([1, 2, 3, 4, 5, 6]) == 15
    assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 38
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 66
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 106