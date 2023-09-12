[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


# test case

``` [/INST] ```python
 def test():
    
    assert largest_smallest_integers([]) == (None, None)

    assert largest_smallest_integers([1]) == (None, 1)

    assert largest_smallest_integers([-1]) == (-1, None)

    assert largest_smallest_integers([1, -2, 3, -4]) == (-2, 1)

    assert largest_smallest_integers([1, 2, 3, 4]) == (None, 1)

    assert largest_smallest_integers([-1, -2, -3, -4])
 ```  [INST] #The test cases that you generated in test(), cannot detect the mutation in the following code snippet.
```python
def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter((lambda x: (x >= 0)), lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] Yes, you're correct. The test cases I provided earlier do not detect the mutation in the code snippet you provided. Here's a new test case that should detect the change:
```python
def test():
    lst = [1, -2, 3, -4, 5]
    expected = (3, 5)
    result = largest_smallest_integers(lst)
    assert result == expected

```
This test case should pass when the function is called with the original input `lst = [1, -2, 3, -4, 5]`, and fail when the function is called with the modified input `lst = [1, 2, 3, -4, 5]`.
Note that the `assert` statement in the test case compares the expected output `expected` with the actual output `result`, and returns `False` if they are different.