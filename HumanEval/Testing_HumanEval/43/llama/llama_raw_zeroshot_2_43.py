[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def pairs_sum_to_zero(l):
    
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False




# test case
def test():
    assert [/INST]  Here are some test cases for the `pairs_sum_to_zero` function:
```
def test_empty_list():
    res = pairs_sum_to_zero([])
    assert res is False

def test_single_element_list():
    res = pairs_sum_to_zero([1])
    assert res is False

def test_two_element_list_sum_to_zero():
    res = pairs_sum_to_zero([1, 2])
    assert res is True

def test_three_element_list_sum_to_zero():
    res = pairs_sum_to_zero([1, 2, 3])
    assert res is False

def test_four_element_list_sum_to_zero():
    res = pairs_sum_to_zero([1, 2, 3, 4])
    assert res is False

def test_list_of_negative_numbers():
    res = pairs_sum_to_zero([-1, -2, -3])
    assert res is False

def test_list_