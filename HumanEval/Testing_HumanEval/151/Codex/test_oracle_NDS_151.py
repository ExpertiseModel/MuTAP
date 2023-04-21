def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])

def test():
    assert double_the_difference([-0.5, -1, -2.5,0,0.5]) == 6.25
    assert double_the_difference([3,3,3,3]) == 0
    assert double_the_difference([8,6,7,5,3,0,1]) == 6
    assert double_the_difference([2,2,2,2,2,2,2,2,2,2,2,2,2]) == 0
    assert double_the_difference([-0.5, 0, 0.5, 1, 2.5, 3]) == 18.5
    assert double_the_difference([8,6,7,5,3,0,1,8,6,7,5,3,0,1]) == 6
    print('Success: test()')
