def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared
assert sum_squares([1, 2, 3, 4, 5]) == 55
