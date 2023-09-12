def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared



#<test>

def test():
    assert sum_squares([]) == 0
    assert sum_squares([3]) == 9
