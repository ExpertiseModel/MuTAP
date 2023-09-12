def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])
assert double_the_difference([1, 3, 5, 7, 9]) == 165
assert double_the_difference([2, 4, 6, 8, 10]) == 0
