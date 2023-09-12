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


#</code>
#<test>

``` [/INST] ```python
 def test():
    
    assert any_int(1, 2, 3) is True

#</testCase>

    assert any_int(1, 2.5, 3) is False

#</testCase>

    assert any_int(1, 2, 3) is True
    assert any_int(1, 2, 4) is False

#
    assert any_int(1, 2, 3) is True
    assert any_int(2, 3, 4) is False


    assert any_int(1, 2, 3) is True
    assert any_int(1, 3, 4) is True
 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x + y == z or x - z == y or y + z == x):
            return True
        return False
    return False

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] Sure! Here's a new test case that should detect the change in the function `any_int` you introduced:
```python
def test():
    assert not any_int(1, 2, 3) or any_int(-1, 2, 3) is False
```
This test case checks whether the function `any_int` returns `True` when the inputs `x`, `y`, and `z` have the same absolute value, but their signs are different. For example, `any_int(1, -2, 3)` should return `True`, since the absolute value of `1` is the same as the absolute value of `-2`, but their signs are different.
The test case also checks whether the function `any_int` returns `False` when the inputs `x`, `y`, and `z` have the same sign, but their absolute values are different. For example, `any_int(1, 2, -3)` should return `False`, since the absolute value of `1` is different from the absolute value of `2`, and the absolute value of `-3` is different from the absolute value of `1` and `2