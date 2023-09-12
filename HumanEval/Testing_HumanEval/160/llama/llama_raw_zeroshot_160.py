[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `do_algebra` function:
```
def test_positive():
    operator = "++"
    operand = ["a", "b", "c"]
    result = do_algebra(operator, operand)
    assert result == "a+b+c"

def test_negative():
    operator = "-+"
    operand = ["a", "b", "c"]
    result = do_algebra(operator, operand)
    assert result == "-a-b-c"

def test_mixed():
    operator = "*"
    operand = ["a", "b", "c"]
    result = do_algebra(operator, operand)
    assert result == "a*b*c"

def test_empty():
    operator = "/"
    operand = []
    result = do_algebra(operator, operand)
    assert result == ""

def test_nonexistent():
    operator = "not-a-real-op"
    operand = ["a", "b", "c"]
    with pytest.