[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `do_algebra` function:
```
test_cases = [
    # Test basic addition
    (['+', '*', '-'], [2, 3, 4, 5]),
    # Test basic multiplication
    (['*', '/'], [4, 5]),
    # Test complex multiplication
    (['*', '/'], [4, 5, 6, 7]),
    # Test complex division
    (['/', '**'], [4, 5, 6, 7]),
    # Test exponentiation
    (['**'], [4, 5, 6, 7]),
    # Test mixing operators
    (['+', '*', '-'], [2, 3, 4, 5]),
    # Test invalid operator
    (['abc', '*'], [2, 3, 4, 5]),
    # Test invalid operand
    (['+', '*'], [2,]),
]

for t in test_cases:
    operand = t[1]
    result = do_algebra(t