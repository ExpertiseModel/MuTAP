def sum_squares(lst):
    
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)



def test():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 153
    assert sum_squares([1, 2, 3, 4, 5, 6, 7]) ==105
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) ==220
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) ==324
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ==440
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]) ==440
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11]) ==580
    assert sum_squares([-1,-2,-3]) == -7
    assert sum_squares([0,0,0]) == 0
    assert sum_