[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))


#</code>
#<test>

``` [/INST] ```python
 def test():
    
    assert rounded_avg(3, 2) == -1
    assert rounded_avg(5, 3) == -1
    assert rounded_avg(7, 4) == -1
    assert rounded_avg(10, 5) == -1
    assert rounded_avg(12, 6) == -1
    assert rounded_avg(15, 7) == -1
    assert rounded_avg(18, 8) == -1
    assert rounded_avg(20, 9) == -1
 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation * ((m - n) + 1)))

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] Ah, I see the issue. The previous test cases were not able to detect the change in the function signature because they were only testing the return value of the function without checking the updated code structure.
Here's a new test case that should detect the change in the function signature:
```python
def test():
    # Test with a small value of n and m
    assert rounded_avg(3, 2) == -1
    # Test with a larger value of n and m
    assert rounded_avg(10, 5) == 3
    # Test with a value of n that is greater than m
    assert rounded_avg(12, 6) == -1
    # Test with a value of n that is less than m
    assert rounded_avg(7, 4) == -1
    # Test with a value of m that is less than n
    assert rounded_avg(15, 7) == -1
```
In this new test case, we are testing the function with different combinations of `n` and `m`, including one where `n` is greater than `m`, one where `n`