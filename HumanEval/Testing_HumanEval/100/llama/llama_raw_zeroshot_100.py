[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def make_a_pile(n):
    
    return [n + 2*i for i in range(n)]


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `make_a_pile` function:
```
def test_make_a_pile_single_digit():
    assert make_a_pile(1) == [2, 3, 4, 5, 6]

def test_make_a_pile_small_num():
    assert make_a_pile(2) == [4, 6, 8, 10, 12]

def test_make_a_pile_medium_num():
    assert make_a_pile(5) == [10, 15, 20, 25, 30]

def test_make_a_pile_large_num():
    assert make_a_pile(10) == [20, 40, 60, 80, 100]

def test_make_a_pile_negative_num():
    with pytest.raises(ValueError):
        assert make_a_pile(-1) == []

def