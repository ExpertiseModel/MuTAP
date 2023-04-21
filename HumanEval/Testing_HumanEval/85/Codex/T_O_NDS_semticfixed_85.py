def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


def test():
    assert add([1, 2, 3, 4, 5, 6]) == 12
    assert add([1, 2, 3, 4, 5, 6, 5]) == 12
    assert add([1, 2, 3, 4, 5, 6, 5, 4]) == 16
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1]) == 16
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1, 2]) == 18
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1, 2, 3]) == 18
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1, 2, 3, 4]) == 22
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1, 2,3, 4, 5]) == 22
