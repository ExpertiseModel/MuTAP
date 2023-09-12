[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `triangle_area` function:
```
def test_ InvalidInputs():
    # Test with negative numbers
    assert triangle_area(-1, -2, -3) == -1
    # Test with negative numbers
    assert triangle_area(1, 2, 3) == 4.0
    # Test with empty lists
    assert triangle_area([], [], []) == 0.0

def test_ ValidInputs():
    # Test with small triangles
    assert triangle_area(1, 2, 3) == 3.0
    # Test with medium triangles
    assert triangle_area(5, 10, 15) == 50.0
    # Test with large triangles
    assert triangle_area(10, 20, 30) == 900.0
```
Explanation:

* `test_InvalidInputs()`: Tests the function with negative numbers and empty lists.
* `test_ValidInputs()`: Tests the function with small, medium, and large triangles.