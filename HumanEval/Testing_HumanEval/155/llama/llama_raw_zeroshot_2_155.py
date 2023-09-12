[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `even_odd_count` function:
```
def test_even_odd_count():
    # Test with negative numbers
    assert even_odd_count(-12) == tuple((1, 1))
    assert even_odd_count(-5) == tuple((1, 1))
    # Test with positive integers
    assert even_odd_count(123) == tuple((1, 2))
    assert even_odd_count(987) == tuple((2, 3))
    # Test with decimal numbers
    assert even_odd_count(3.14) == tuple((1, 1))
    assert even_odd_count(-3.14) == tuple((1, 1))
    # Test with very large numbers
    assert even_odd_count(1000000000) == tuple((2, 7))
    assert even_odd_count(-1000000000) == tuple((1, 7))

# Test with edge cases
assert even_odd_count(-