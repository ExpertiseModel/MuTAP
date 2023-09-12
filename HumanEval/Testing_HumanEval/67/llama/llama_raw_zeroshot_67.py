[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `fruit_distribution` function in Python:
```python
def test_fruit_distribution():
    # Test with valid input
    assert fruit_distribution("apple banana orange", 5) == 5
    assert fruit_distribution("apple banana orange", 6) == 1
    # Test with invalid input
    assert fruit_distribution("apple banana orange", 5) == 5
    assert fruit_distribution("apple banana orange", 6) == 0
    # Test with empty string
    assert fruit_distribution("", 5) == 0
    assert fruit_distribution("", 6) == 0
    # Test with null input
    assert fruit_distribution( None, 5) == 0
    assert fruit_distribution( None, 6) == 0
```
Explanation:

* In the first test, we pass the input string "apple banana orange" to the function and assert that the output is 5.
* In the second test, we pass a long input string with more than 3 fruits, and assert that the output is 