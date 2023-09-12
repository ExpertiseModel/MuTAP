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
```python
def test_small_triangles():
    assert triangle_area(1, 2, 3) == 6
def test_equal_side_triangles():
    assert triangle_area(3, 3, 3) == 3 * 3
def test_large_triangles():
    assert triangle_area(10, 20, 30) == 50
def test_edge_cases():
    assert triangle_area(0, 0, 0) == 0
    assert triangle_area(1, 0, 0) == 1
    assert triangle_area(0, 1, 0) == 1
    assert triangle_area(0, 0, 1) == 0
def test_tolerance():
    assert abs(triangle_area(1, 2, 3) - 6) < 0.01
```
Explanation:

* `test_small_triangles`: Tests the case where all sides are small, i.e