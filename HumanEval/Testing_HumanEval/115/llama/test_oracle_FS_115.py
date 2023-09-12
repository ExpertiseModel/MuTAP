def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])


#</code>
#<test>
def test():


    assert max_fill([[1, 2, 3]], 2) == 3

    assert max_fill( [[1, 2, 3], [4, 5, 6]], 3) == 6


    assert max_fill([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4) == 10

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11,