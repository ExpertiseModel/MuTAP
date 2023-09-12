[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def order_by_points(nums):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `order_by_points` function:
```scss
def test_empty_list():
    nums = [ ]
    result = order_by_points(nums)
    assert result == []

def test_single_digit():
    nums = [1]
    result = order_by_points(nums)
    assert result == [1]

def test_negative_digit():
    nums = [-1]
    result = order_by_points(nums)
    assert result == [-1]

def test_digit_with_leading_zero():
    nums = [0.1]
    result = order_by_points(nums)
    assert result == [0.1]

def test_digit_with_trailing_zero():
    nums = [-0.1]
    result = order_by_points(nums)
    assert result == [-0.1]

def test_list_of_digits():
    nums = [2, 3, -4, 5, 