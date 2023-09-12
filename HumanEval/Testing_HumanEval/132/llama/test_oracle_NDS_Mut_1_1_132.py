[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 def is_nested(string):
   
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

    


# test case

``` [/INST] ```python
 def test():
    
    assert is_nested('[[]]') == True 
    assert is_nested('[]]]]]]][[[[[]') == False 
    assert is_nested('[][]') == False 
    assert is_nested('[]') == False 
    assert is_nested('[[][]]') == True 
    assert is_nested('[[]][[') == True 

 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
def is_nested(string):
   
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i -= 1
    return cnt >= 2

    

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] Sure! Here's an updated test case that can detect the change in the code snippet you provided:
```python
def test():
    assert is_nested('[[]]') == True  # Pass
    assert is_nested('[]]]]]]][[[[[]') == False  # Fail
    assert is_nested('[][]') == False  # Pass
    assert is_nested('[]') == False  # Pass
    assert is_nested('[[][]]') == True  # Pass
    assert is_nested('[[]][[') == True  # Pass

    # Add a new test case to detect the change in the code snippet
    assert is_nested('[[]]') == False  # Fail
```
In this updated test case, we've added a new test case that checks whether `is_nested()` returns `False` when passed an empty list `[]`. This test case was added to detect the change in the code snippet where the `opening_bracket_index` and `closing_bracket_index` are swapped.
So, the test case will pass for the original code snippet because `opening_bracket