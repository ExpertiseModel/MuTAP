def specialFilter(nums):
    
    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 




#<test>
def test():
    
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4

    assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4
    
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0