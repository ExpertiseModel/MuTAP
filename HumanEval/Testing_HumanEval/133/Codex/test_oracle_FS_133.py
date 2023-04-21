def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared

def test():
    assert sum_squares([2, 3, 4]) == 7  
    assert sum_squares([1, 2, 3, 4, 5])== 9 
    assert sum_squares([1, 2, 1, 2, 1]) == 6
