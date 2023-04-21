def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])
assert double_the_difference([8,6,7,5,3,0,1]) == 84
