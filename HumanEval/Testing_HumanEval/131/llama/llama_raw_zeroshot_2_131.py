[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit%2 == 1:
            product= product*int_digit
            odd_count+=1
    if odd_count ==0:
        return 0
    else:
        return product


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `digits` function:
```
def test_digits_1():
    n = 1
    result = digits(n)
    assert result == 1

def test_digits_2():
    n = 4
    result = digits(n)
    assert result == 0

def test_digits_3():
    n = 235
    result = digits(n)
    assert result == 15

def test_digits_4():
    n = -1
    result = digits(n)
    assert result == 0

def test_digits_5():
    n = 0
    result = digits(n)
    assert result == 0

def test_digits_6():
    n = 100
    result = digits(n)
    assert result == 100

def test_digits_7():
    n = 1234567890
    result = digits(n)
    assert result == 1234567