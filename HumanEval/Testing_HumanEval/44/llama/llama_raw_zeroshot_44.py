[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret






# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `change_base` function:

```
def test_change_base():
    # Test with positive integers
    assert change_base(5, 10) == "5"
    assert change_base(8, 20) == "8"
    # Test with negative integers
    assert change_base(-5, 10) == "-5"
    assert change_base(-8, 20) == "-8"
    # Test with zero
    assert change_base(0, 10) == ""
    # Test with very large numbers
    assert change_base(1000, 10) == "1000"
    # Test with very small numbers
    assert change_base(0.00001, 10) == "0.00001"

def test_edge_cases():
    # Test with very large numbers
    assert change_base(1000000, 10) == "1000000"
    # Test with very small numbers
    assert