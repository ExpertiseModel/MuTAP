def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

 # generate test case for the function above
def test_max_fill():
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 1) == 6
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 2) == 3
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 3) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 4) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 5) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 6) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 7) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 8) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 9) == 2