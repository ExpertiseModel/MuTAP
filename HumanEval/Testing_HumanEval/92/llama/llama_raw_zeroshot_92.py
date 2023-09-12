[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False


# test case
def test():
    assert [/INST]  Sure, I can help you generate test cases for the `any_int` function. Here are some examples:
### Test 1: Multiple equal numbers
```python
 assert any_int(1, 2, 3) == True
 assert any_int(3, 2, 3) == True
 assert any_int(2, 1, 3) == True
```
### Test 2: Non-equal numbers
```python
 assert any_int(1, 2, 4) == False
 assert any_int(3, 2, 5) == False
 assert any_int(2, 1, 6) == False
```
### Test 3: Order of operands matters
```python
 assert any_int(1, 2 + 3, 4) == True
 assert any_int(3, 2, 4 + 1) == True
 assert any_int(2, 1 + 3, 4) == True
```
### Test 4: Multiple comparisons
```python
 assert any_int(1, 2 == 3, 4 == 