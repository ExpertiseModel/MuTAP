
def specialFilter(nums):
    
    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 


# test case

def test():
    assert specialFilter([]) == 0


    assert specialFilter([4]) == 0


    assert specialFilter([1, 3, 5, 7, 9]) == 0


    assert specialFilter([2, 4, 6, 8, 10]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
    assert specialFilter([1, 3, 5, 7, 9]) == 0
    assert specialFilter([1, 3, 5, 7, 9]) == 2

    assert specialFilter([2, 4, 6, 8]) == 0

    assert specialFilter([1, 3, 5, 7, 9, 11]) == 2
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 6

    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 8
    assert specialFilter([1, 3, 5, 7, 9, 11]) == 3

    # Test with a list of even integers
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

    # Test with a list of mixed integers
    assert specialFilter([1, 3, 5, 7, 9, 11, 13]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 0
    assert specialFilter([1, 3, 5, 7, 9]) == 2
    assert specialFilter([-4]) == 0

    # Test when the number is greater than 10
    assert specialFilter([10, 20, 30, 40, 50]) == 0

    # Test when the number is less than 10
    assert specialFilter([-2, -3, -4, -5, -6]) == 2
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15]) == 4

    # Test when the input list contains both odd and even numbers
    assert specialFilter([1, 2, 3, 4, 5, 7, 9, 11, 13]) == 3

    # Test when the input list is empty
    assert specialFilter([]) == 0

