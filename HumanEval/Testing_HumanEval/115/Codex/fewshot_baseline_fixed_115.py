def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])


def test():
    assert max_fill([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 6) == 3
