def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared



#<test>

def test():
    assert sum_squares([1, 2, 3, 4]) == 30
    assert sum_squares([-1, -2, -3, -4]) == 30
    assert sum_squares([1, 2, 3, 4, 5]) == 55
    assert sum_squares([-1, -2, -3, -4, -5]) == 55
    assert sum_squares([]) == 0

    assert sum_squares([3]) == 9

    assert sum_squares([3, 5, 7, 3]) == 92
