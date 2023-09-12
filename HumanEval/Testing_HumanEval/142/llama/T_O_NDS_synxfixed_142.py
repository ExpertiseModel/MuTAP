
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


# test case
def test():
   
    # Test 1:empty list
    assert sum_squares([]) == 0

    # Test 2:non-empty list with only one element
    assert sum_squares([1, 2, 3, 4, 5]) == 45

    # Test 3:non-empty list with multiple elements, some of which are squared
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1225

    # Test 4:non-empty list with elements that are not numbers
    assert sum_squares(['apple', 'banana', 3, 'orange']) == 0

    # Test 5:empty list with a bad argument
    assert sum_squares([], 5) == 0

    # Test 6:non-empty list with a mix of numbers and strings
    
    lst = [ [1, 2, 3, "hello", 5], ]
