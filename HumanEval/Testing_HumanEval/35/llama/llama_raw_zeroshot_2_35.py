[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `max_element` function:
```
def test_empty_list():
    l = []
    assert max_element(l) is None

def test_single_element_list():
    l = [10]
    assert max_element(l) == 10

def test_multiple_Elements():
    l = [10, 5, 2, 3]
    assert max_element(l) == 3

def test_negative_values():
    l = [-1, 0, 1, 2, -3]
    assert max_element(l) == -3

def test_large_positive_values():
    l = [100, 50, 20, 30, 40]
    assert max_element(l) == 100

def test_edge_cases():
    l = [0, 1, -1, 10, -10]
    assert max_element(l) == 10

def test_None_list():