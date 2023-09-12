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
    assert [/INST]  Sure, here are some test cases for the `strange_sort_list` function:
```
def test_empty_list():
    lst = []
    res = strange_sort_list(lst)
    assert res == []

def test_single_element_list():
    lst = [1]
    res = strange_sort_list(lst)
    assert res == [1]

def test_neg_element_list():
    lst = [1, -2, 3, 4]
    res = strange_sort_list(lst)
    assert res == [1, -2, 3, 4]

def test_twosided_list():
    lst = [1, 2, 2, 3, 4]
    res = strange_sort_list(lst)
    assert res == [1, 2, 2, 3, 4]

def test_sorted_list():
    lst = [3, 2, 1, 4]
    res = strange_sort_list(lst)
    assert res == [1, 2