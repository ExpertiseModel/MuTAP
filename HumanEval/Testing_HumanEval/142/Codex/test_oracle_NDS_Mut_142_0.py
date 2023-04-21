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
    assert sum_squares([1,2,3,4,5,6,7]) == 202
    assert sum_squares([1,2,3,5,6,7,8,9]) == 327
    assert sum_squares([1,2,3]) == 3
    assert sum_squares([-1,2,-3]) == -1
    assert sum_squares([-1,0,3]) == 0
    assert sum_squares([1,2,3,-4,-5,6,7]) ==327
    assert sum_squares([-1,-2,-3]) == -6
    assert sum_squares([0,0,0]) == 0
    print ('done testing')


test()
