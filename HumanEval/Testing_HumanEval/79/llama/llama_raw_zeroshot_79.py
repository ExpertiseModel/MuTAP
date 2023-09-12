[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"


# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `decimal_to_binary` function in Python:
```python
def test_decimal_to_binary_zero():
    result = decimal_to_binary(0)
    expected = "db0000000"
    assert result == expected

def test_decimal_to_binary_positive():
    result = decimal_to_binary(123)
    expected = "db1100111"
    assert result == expected

def test_decimal_to_binary_negative():
    result = decimal_to_binary(-123)
    expected = "db1110100"
    assert result == expected

def test_decimal_to_binary_small():
    result = decimal_to_binary(-6)
    expected = "db1100111"
    assert result == expected

def test_decimal_to_binary_large():
    result = decimal_to_binary(65535)
    expected = "db111111