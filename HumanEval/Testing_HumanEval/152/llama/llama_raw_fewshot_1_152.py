[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 These are two examples of codes and their tests.

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
#</test>

#<original code>



def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]


#</original code>

generate test in the form of above example tests for the original code:

#<test>
def test():
    assert [/INST]  Sure! Here are some tests for the original code:
#<code>

def compare(game, guess):
    return [abs(x - y) for x, y in zip(game, guess)]


#<test>

def test():
    game = [1, 2, 3]
    guess = [4, 5, 6]
    assert compare(game, guess) == [0, 1, 2]
    game = [4, 5, 6]
    guess = [1, 2, 3]
    assert compare(game, guess) == [3, 2, 1]
    game = [4, 5, 6]
    guess = [2, 3, 4]
    assert compare(game, guess) == [2, 3, 4]
    game = [4, 5, 6]
    guess = [1, 2, 3]
    assert compare(game, guess) == [3, 2, 1]


#</test>