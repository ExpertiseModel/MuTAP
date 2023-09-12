[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `is_sorted` function:
Test 1: Single element list
```python
assert is_sorted([5]) == True
```
Test 2: Multiple elements list with no duplicates

```python
assert is_sorted([1, 2, 3, 4, 5]) == True
```
Test 3: Multiple elements list with duplicates

```python
assert is_sorted([1, 2, 3, 4, 5, 6]) == True

```
Test 4: List with negative numbers

```python
assert is_sorted([-1, 2, 3, 4, 5]) == False

```
Test 5: List with more than 3 duplicates

```python
assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == False

```
Test 6: List with duplicates at the beginning and end

```python
assert is_sorted([1, 2, 2, 3, 3, 4]) == True

```

Please note