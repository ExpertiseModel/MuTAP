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
       summation -= i
    return bin(round(summation/(m - n + 1)))

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] Sure! Here's a new test case that can detect the change in the function:
```python
def test():
    assert rounded_avg(3, 2) == -1
    assert rounded_avg(5, 3) == -1
    assert rounded_avg(7, 4) == -1
    assert rounded_avg(10, 5) == -1
    assert rounded_avg(12, 6) == -1
    assert rounded_avg(15, 7) == -1
    assert rounded_avg(18, 8) == -1
    assert rounded_avg(20, 9) == -1

    # Test the new case
    assert rounded_avg(3, 0) == -1

```
The new test case added the case of `m = 0`, which is not handled by the original test cases. When `m = 0`, the function should return `-1`, as the sum of the numbers from `n` to `m` is not defined.