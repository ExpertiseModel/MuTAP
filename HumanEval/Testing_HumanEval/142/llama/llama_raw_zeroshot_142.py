[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sum_squares(lst):
    
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `sum_squares` function:
```
# Test 1:empty list
 lst = []
assert sum_squares(lst) == 0

# Test 2:non-empty list with only one element
lst = [1, 2, 3, 4, 5]
assert sum_squares(lst) == 45

# Test 3:non-empty list with multiple elements, some of which are squared
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sum_squares(lst) == 1225

# Test 4:non-empty list with elements that are not numbers
lst = ['apple', 'banana', 3, 'orange']
assert sum_squares(lst) == 0

# Test 5:empty list with a bad argument
lst = []
assert sum_squares(lst, 5) == 0

# Test 6:non-empty list with a mix of numbers and strings
lst = [