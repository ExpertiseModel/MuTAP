[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)


# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `reverse_delete` function:
```python
def test_basic():
    s = "hello"
    c = "ell"
    result, expected = reverse_delete(s, c)
    assert result == "hlelo"
    assert expected is True

def test_empty():
    s = ""
    c = ""
    result, expected = reverse_delete(s, c)
    assert result == ""
    assert expected is True

def test_large():
    s = "aabbccdddeeeeeffggghhhiiii"
    c = "aabbcccdfghjjjjjjjj"
    result, expected = reverse_delete(s, c)
    assert result == "aabbccdfghhjiijjj"
    assert expected is True

def test_uppercase():
    s = "HELLO"
    c = "HOT"
    result, expected = reverse_delete(s, c)
    assert result == "LOHET"
    assert expected is True

def test_