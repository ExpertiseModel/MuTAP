def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]



def test():
    assert pluck([3, 8, 10]) == [8, 1]
    assert pluck([3, 8, 10, 16]) == [8, 1]
    assert pluck([1, 2, 7, 10, 15]) == [2, 1]
    assert pluck([1, 2, -1, 0, -2, -3, -4, -5]) == [-1, 7]
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert pluck([]) == []
