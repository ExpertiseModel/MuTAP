def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


def test():
    assert add([2,4,6,8,10]) == 12
    assert add([]) == 0
