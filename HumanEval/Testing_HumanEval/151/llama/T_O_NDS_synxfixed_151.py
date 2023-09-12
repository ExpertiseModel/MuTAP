def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])


# test case
def test():
   
    # Simple list with odd numbers
    assert double_the_difference([1, 3, 5, 7, 9]) == 71


    # Empty list
    assert double_the_difference([]) == 0

    # List with even numbers
    assert double_the_difference([2, 4, 6, 8, 10]) == 16

    # List with decimals
    assert double_the_difference([1.5, 3.7, 0.5, 2.1, 4.3]) == 15.5