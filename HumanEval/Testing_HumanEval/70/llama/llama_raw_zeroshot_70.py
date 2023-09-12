[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def strange_sort_list(lst):
    
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `strange_sort_list` function:
```python
def test_empty_list():
    lst = [ ]
    assert strange_sort_list(lst) == [ ]

def test_singleton_list():
    lst = [1]
    assert strange_sort_list(lst) == [1]

def test_list_with_ duplicates():
    lst = [1, 2, 2, 3, 3]
    assert strange_sort_list(lst) == [1, 2, 3]

def test_list_with_ties():
    lst = [3, 2, 2, 1, 1]
    assert strange_sort_list(lst) == [1, 2, 2, 3]

def test_list_with_positive_and_negative():
    lst = [-2, -1, 0, 1, 2]
    assert strange_sort_list(lst) == [-2, -1, 0, 1, 2]

def test_list