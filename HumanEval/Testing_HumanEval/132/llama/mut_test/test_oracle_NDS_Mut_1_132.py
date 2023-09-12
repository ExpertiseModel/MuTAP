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

 ```  [INST] #The test cases that you generated in test(), cannot detect the mutation in the following code snippet.
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
    assert [/INST] Sure, here's a new test case to detect the mutation in the `is_nested` function:
```python
def test():
    # Test for the mutation where an extra closing bracket is added
    assert is_nested('[[]]') == True
    assert is_nested('[]][]]') == False
    # Test for the mutation where an extra opening bracket is added
    assert is_nested('[][]') == False
    assert is_nested('[][][]') == True
    # Test for the mutation where the order of the closing bracket is changed
    assert is_nested('[[]]') == True
    assert is_nested('[][][]') == False
    # Test for the mutation where the closing bracket is missing
    assert is_nested('[]') == False


```
This new test case checks for the following mutations:

* Extra closing bracket is added
* Extra opening bracket is added
* The order of the closing bracket is changed
* A closing bracket is missing

By adding these test cases, we can cover more mutations and make the test