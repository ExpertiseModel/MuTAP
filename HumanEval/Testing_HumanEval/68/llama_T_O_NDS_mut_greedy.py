def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]
assert pluck([]) == []
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 1]
