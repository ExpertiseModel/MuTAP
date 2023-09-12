def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]




#<test>

def test():
    assert pluck([]) == []
    assert pluck([1, 2, 3, 4, 5]) == [2, 1]
    assert pluck([2, 4, 6, 8, 10]) == [2, 0]
    assert pluck([3, 5, 7, 9, 11]) == []
    assert pluck([1, 2, 3, 4, 5]) == [2, 1]
