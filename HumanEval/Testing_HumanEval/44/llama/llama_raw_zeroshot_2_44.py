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
```markdown
def test():
    # Positive case
    assert change_base(10, 10) == "01"
    # Negative case
    assert change_base(-10, 10) == "-01"
    # Base 2 case
    assert change_base(10, 2) == "10"
    # Base 16 case
    assert change_base(10, 16) == "a"
    # Zero case
    assert change_base(0, 10) == ""
    # Edge cases
    assert change_base(-1, 10) == "-0"
    assert change_base(10, -1) == "-10"
    # Large numbers
    assert change_base(1000, 10) == "1000"
    assert change_base(-1000, 10) == "-1000"
```

Note: The `assert` statement in the test function is used to