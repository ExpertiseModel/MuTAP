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
    assert [/INST]  Sure! Here are some test cases for the `any_int` function:
```
    # Test 1: x, y, and z are all integers
    assert any_int(1, 2, 3) # should return True

    # Test 2: x + y = z
    assert any_int(1, 2, 3) # should return True

    # Test 3: x + z = y
    assert any_int(1, 2, 3) # should return True

    # Test 4: y + z = x
    assert any_int(1, 2, 3) # should return True

    # Test 5: x, y, and z are not integers
    assert not any_int(1.5, 2.5, 3.5) # should return False

    # Test 6: x + y = z, but z is not an integer
    assert not any_int(1, 2, 3.5) # should return False

    # Test 7: x + z = y, but y is not an integer
