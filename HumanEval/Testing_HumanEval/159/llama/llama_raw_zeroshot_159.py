[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `eat` function:
```
def test_eat_basic():
    assert eat(10, 5, 15) == [10 + 5, 10]

def test_eat_negative_need():
    assert eat(-5, 10, 20) == [0, 20]

def test_eat_negative_remaining():
    assert eat(10, -5, 15) == [10, 0]

def test_eat_greater_need():
    assert eat(10, 20, 10) == [20, 0]

def test_eat_zero_need():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_negative_number():
    assert eat(-5, 10, 20) == [0, 20]
```
These test cases cover a variety of edge cases and inputs that the `eat` function may encounter, such as