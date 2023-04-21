def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])




def test():
    assert double_the_difference([-0.5, -1, -2.5,0,0.5]) == 0
    assert double_the_difference([3,3,3,3]) == 36
    assert double_the_difference([8,6,7,5,3,0,1]) == 84
    assert double_the_difference([2,2,2,2,2,2,2,2,2,2,2,2,2]) == 0
    assert double_the_difference([-0.5, 0, 0.5, 1, 2.5, 3]) == 10
    assert double_the_difference([8,6,7,5,3,0,1,8,6,7,5,3,0,1]) == 168
    assert double_the_difference([-0.5, -1, -2.5,0,0.5]) == 0
    assert double_the_difference([3,3,3,3]) == 36
    assert double_the_difference([8,6,7,5,3,0,1]) == 84
    assert double_the_difference([2,2,2,2,2,2,2,2,2,2,2,2,2]) == 0
    assert double_the_difference([-0.5, 0, 0.5, 1, 2.5, 3]) == 10
    assert double_the_difference([8,6,7,5,3,0,1,8,6,7,5,3,0,1]) == 168
