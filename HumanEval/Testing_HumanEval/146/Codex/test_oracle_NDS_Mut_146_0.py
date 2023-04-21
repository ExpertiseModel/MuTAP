def specialFilter(nums):
    
    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 



def test():
    assert specialFilter([11, 13, 15, 107, 109]) == 0
    assert specialFilter([1, 3, 5, 7, 10]) == 0
    assert specialFilter([16, 18, 20, 222, 224, 226, 228]) == 8
