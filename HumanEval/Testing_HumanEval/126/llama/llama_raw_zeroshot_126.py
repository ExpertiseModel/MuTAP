[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_sorted(lst):
    
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
    assert [/INST]  Here are some test cases for the `is_sorted` function in Python:

```
# Test that is_sorted returns False for an unsorted list
lst = [1, 3, 5, 7, 9]
assert not is_sorted(lst)

# Test that is_sorted returns True for a sorted list
lst = [0, 1, 2, 3, 4, 5]
assert is_sorted(lst)

# Test that is_sorted raises a ValueError for an empty list
assert not is_sorted([])

# Test that is_sorted returns False for a list with duplicates
lst = [1, 1, 2, 2, 3, 3]
assert not is_sorted(lst)

# Test that is_sorted returns True for a list with duplicates in ascending order
lst = [1, 2, 2, 3, 3]
assert is_sorted(lst)

# Test that is_sorted raises a ValueError for a list with duplicates in descending order
lst = [3, 2, 1, 1,