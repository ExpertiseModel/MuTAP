def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]

def test():
    assert pluck(['a','b','c','b','d']) == ['b','c','d','b','d','b']
    assert pluck([1,2,3,4,5]) == [3,5,5,5,5]
    assert pluck([1,2,3,4,5,6]) == [3,5,5,5,5,5]
    assert pluck([4]) == [4,0]
    assert pluck([]) == []
