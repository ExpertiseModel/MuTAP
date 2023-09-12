def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])
assert max_fill([1, 2, 3, 4, 5], 2) == 7
