[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])


# test case
def test():
    assert [/INST]  Certainly! Here are some test cases for the `max_fill` function:
```
def test_empty_grid():
    grid = [[]] * 3
    assert max_fill(grid, 1) == 0

def test_single_bucket():
    grid = [ [0,0,1,0] ]
    bucket_capacity = 1
    assert max_fill(grid, bucket_capacity) == 1

def test_one_bucket_full():
    grid = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
    bucket_capacity = 1
    assert max_fill(grid, bucket_capacity) == 2

def test_two_buckets():
    grid = [ [0,0,1,0], [0,1,0,0], [1,1,1,1], [0,1,1,1] ]
    bucket_capacity = 2
    assert max_fill(grid, bucket_capacity) == 5

def test