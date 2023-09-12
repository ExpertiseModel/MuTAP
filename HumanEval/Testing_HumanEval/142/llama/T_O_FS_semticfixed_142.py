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


#</code>
#<test>

def test():
    assert sum_squares([1, 2, 3, 4, 5]) == 147
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 153
    assert sum_squares([1, 2, 3, 4, 5, 6, 7]) == 202
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 210
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039
