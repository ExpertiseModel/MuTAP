[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 
def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False


# test case

``` [/INST] ```python
 def test():
    
    ### Test 1: Multiple equal numbers

    assert any_int(1, 2, 3) == True
    assert any_int(3, 2, 3) == False
    assert any_int(2, 1, 3) == True

    ### Test 2: Non-equal numbers

    assert any_int(1, 2, 4) == False
    assert any_int(3, 2, 5) == True
    assert any_int(2, 1, 6) == False

    ### Test 3: Order of operands matters

    assert any_int(1, 2 + 3, 4) == True
    assert any_int(3, 2, 4 + 1) == True
    assert any_int(2, 1 + 3, 4) == False

    ### Test 4: Multiple comparisons

 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x + y == z or x + z == y or y - z == x):
            return True
        return False
    return False

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] ```python
def test():
    ### Test 5: Edge case for multiple comparisons

    assert any_int(1, 2, 3) == True
    assert any_int(3, 2, 3) == False
    assert any_int(2, 1, 3) == True

    # Add a new edge case to detect the change in the function signature
    assert any_int(1, 2, 3) == True
    assert any_int(3, 2, -1) == False

    ### Test 6: Alternate order of operands

    assert any_int(1, 2 + 3, 4) == True
    assert any_int(3, 2, 4 + 1) == True
    assert any_int(2, 1 + 3, 4) == False

    ```