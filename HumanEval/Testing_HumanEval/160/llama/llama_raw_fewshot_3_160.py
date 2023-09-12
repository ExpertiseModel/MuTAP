[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

Generate test cases. [/INST] These are examples of function code and test functions:

#<code> 

def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
#</code>

#<test>

def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>

#<code>

from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>

#<test>

def test():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>  [INST] Based on the examples of function code and their test function, generate test cases for the following function:
#<code>
def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


#</code>
#<test>
def test():
    assert [/INST]  Here are some test cases for the `do_algebra` function:

Test 1: Basic operation
```
operator = "+"
operand = [1, 2, 3]
result = do_algebra(operator, operand)
assert result == 6
```
Test 2: Multiple operations
```
operator = "*"
operand = [2, 3, 4]
result = do_algebra(operator, operand)
assert result == 24
```
Test 3: Negative number
```
operator = "-"
operand = [-2, -3, -4]
result = do_algebra(operator, operand)
assert result == -12
```
Test 4: Non-numeric operand
```
operator = "*"
operand = ["apple", 5]
result = do_algebra(operator, operand)
assert result == 25
```
Test 5: Expressions with parentheses
```
operator = "+"
operand = [1, (2, 3), 4]
result = do_algebra(operator, operand)
assert result ==