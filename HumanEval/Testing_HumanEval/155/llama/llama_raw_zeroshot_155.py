[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def even_odd_count(num):
    
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
# Test even count
def test_even_count():
    num = 12
    result = even_odd_count(num)
    assert result == (3, 0)

# Test odd count
def test_odd_count():
    num = 13
    result = even_odd_count(num)
    assert result == (0, 3)

# Test edge cases
def test_edge_cases():
    num = -1
    result = even_odd_count(num)
    assert result == (0, 0)

# Test invalid input
def test_invalid_input():
    num = " Hello, world!"
    result = even_odd_count(num)
    assert result == (0, 0)

# Test multiple inputs
def test_multiple_inputs():
    nums = [12, 13, 14]
    results = [even_odd_count(num) for num in nums]
    assert all(result[0