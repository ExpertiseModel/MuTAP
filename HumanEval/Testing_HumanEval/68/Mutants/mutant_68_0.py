def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    evens = list(filter((lambda x: (x * 2 == 0)), arr))
    return [min(evens), arr.index(min(evens))]