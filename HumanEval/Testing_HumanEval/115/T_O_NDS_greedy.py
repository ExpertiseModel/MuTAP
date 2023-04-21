def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])
assert max_fill([[4,4,4,4,4,4,4], [5,5,5,5,5,5,5], [1,1,1,1,1,1,1]], 4) == 18
