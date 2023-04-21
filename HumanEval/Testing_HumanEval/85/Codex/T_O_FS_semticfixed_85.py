def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


def test():
    assert add([1,2,3,4,5]) == 6
    assert add([2,4,6,8,10]) == 12
    assert add([-2,-4,-6,-8,-10]) == -12
    assert add([3,6,9,12,15]) == 18
    assert add([]) == 0
