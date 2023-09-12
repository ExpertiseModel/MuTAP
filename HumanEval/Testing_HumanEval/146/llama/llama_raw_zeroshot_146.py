[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
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
    assert [/INST]  Sure, here are some test cases for the `specialFilter` function:
```python
def test_specialFilter_emptyList():
    # Test with an empty list
    nums = []
    result = specialFilter(nums)
    assert result == 0

def test_specialFilter_singleDigit():
    # Test with a single digit
    nums = [4]
    result = specialFilter(nums)
    assert result == 0

def test_specialFilter_oddDigitsOnly():
    # Test with odd digits only
    nums = [1, 3, 5, 7, 9]
    result = specialFilter(nums)
    assert result == 5

def test_specialFilter_evenDigitsOnly():
    # Test with even digits only
    nums = [2, 4, 6, 8, 10]
    result = specialFilter(nums)
    assert result == 0

def test_specialFilter_mixedDigits():
    # Test with a mix of odd and even digits
    nums = [1, 