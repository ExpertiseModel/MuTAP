def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

def test():
    assert max_fill([[4,4,4,4,4,4,4], [5,5,5,5,5,5,5], [1,1,1,1,1,1,1]], 4) == 10
    assert max_fill([[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]], 0) == 0
    assert max_fill([[1,2,3,4,8], [1,2,3,4,8], [1,2,3,4,9], [1,2,3,4,8], [1,2,3,4,8]], 4) == 20