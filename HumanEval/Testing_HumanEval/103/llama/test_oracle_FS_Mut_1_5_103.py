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
    
    if m <= n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] I apologize for the oversight in my previous response. You are correct that the test cases I generated do not detect the change in the code snippet you provided. Here is a new test case that should detect the change:
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
    # Test the updated code with a different input
    assert rounded_avg(3, 2) == -1
```
In this test case, we are testing the `rounded_avg` function with a variety of input values to ensure that it produces the correct output. We are also testing the updated code with