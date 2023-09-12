[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    
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
    assert [/INST]  Sure! Here are some test cases for the `specialFilter` function:
```python
test_cases = [
    # Empty list
    ([], 0),
    # List with only one number
    ([1], 1),
    # List with multiple numbers, none of them greater than 10
    ([1, 2, 3], 0),
    # List with multiple numbers, one of them greater than 10
    (["10", 20, 30], 1),
    # List with only odd numbers
    (["1", "3", "5", "7"], 3),
    # List with only even numbers
    (["2", "4", "6"], 0),
    # List with mix of odd and even numbers
    (["1", "3", "5", "7", "2", "4"], 2),
]
for test_case in test_cases:
    print(f"Testing {test_case}")
def specialFilter(*nums):
    # Call the function and check the result
    result = specialFilter(nums)
