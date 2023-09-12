[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `largest_smallest_integers` function in Python:

**Test 1: Empty list**
```python
assert largest_smallest_integers([]) == (None, None)
```
**Test 2: Single positive integer**
```python
assert largest_smallest_integers([1]) == (1, 1)
```
**Test 3: Single negative integer**
```python
assert largest_smallest_integers([-1]) == (-1, 1)
```
**Test 4: List with mix of positive and negative integers**
```python
assert largest_smallest_integers([1, -2, 3, -4]) == (3, -4)
```
**Test 5: List with only positive integers**
```python
assert largest_smallest_integers([1, 2, 3, 4]) == (4, 3)
```
**Test 6: List with only negative integers**
```python
assert largest_smallest_integers([-1, -2, -3, -4])