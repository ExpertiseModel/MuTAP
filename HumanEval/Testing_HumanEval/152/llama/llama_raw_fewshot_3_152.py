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
def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]


#</code>
#<test>
def test():
    assert [/INST]  Sure! Here are some test cases for the `compare` function:
#<test>
def test_function_returns_list_of_differences():
    with pytest.raises(TypeError):
        compare("apple", "orange")
    with pytest.raises(TypeError):
        compare([1, 2, 3], [4, 5, 6])
    assert compare("apple", "apple") == []
    assert compare([1, 2, 3], [1, 2, 3]) == []
    assert compare("apple", ["apple", "banana"]) == [(3,)]
    assert compare([1, 2, 3], [4, 5, 6]) == [(2,), (3,), (5,)]
#</test>

#<code>

def test():
    apple = ["apple", "banana", "orange"]
    guess = ["apple", "orange"]
    assert compare(apple, guess) == ([0,], [1,], [2,])
    apple = ["apple", "banana"]