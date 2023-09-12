def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])




def test():
    assert double_the_difference([1, 2, 3, 4, 5, 6]) == 35
    
    assert double_the_difference([0, 2, 4, 6, 8, 10]) == 0
    
    assert double_the_difference([3, 6, 9, 12, 15, 18]) == 315
    
    assert double_the_difference([0, 0, 0, 0, 0, 0]) == 0

