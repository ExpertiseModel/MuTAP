def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])
assert add([1, 2, 3, 4, 5, 6]) == 12
