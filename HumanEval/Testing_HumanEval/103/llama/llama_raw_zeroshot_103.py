[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `rounded_avg` function in Python:
```python
def test_rounded_avg_positive_inputs():
    # Test with positive numbers
    assert rounded_avg(5, 10) == 7
    assert rounded_avg(10, 15) == 12
    assert rounded_avg(20, 25) == 23

def test_rounded_avg_negative_inputs():
    # Test with negative numbers
    assert rounded_avg(-5, 10) == -7
    assert rounded_avg(-10, 15) == -12
    assert rounded_avg(-20, 25) == -23

def test_rounded_avg_edge_cases():
    # Test edge cases
    assert rounded_avg(0, 1) == 0
    assert rounded_avg(0, 0) == 0
    assert rounded_avg(1, 0) == 1

def test_rounded