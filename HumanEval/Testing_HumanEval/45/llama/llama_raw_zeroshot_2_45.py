[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def triangle_area(a, h):
    
    return a * h / 2.0




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `triangle_area` function:
```
def test_triangle_area_negative_values(self):
    with self.assertRaisesRegex(ValueError, 'Must be non-negative'):
        triangle_area(-1, 2)

def test_triangle_area_zero_base(self):
    with self.assertRaisesRegex(ValueError, 'Must be non-zero'):
        triangle_area(0, 2)

def test_triangle_area_small_height(self):
    assert triangle_area(3, 1) == 3.0
    assert triangle_area(3, 0.1) == 0.3

def test_triangle_area_large_height(self):
    assert triangle_area(10, 5) == 50.0
    assert triangle_area(10, 10) == 100.0

def test_triangle_area_edge_cases(self):
    assert triangle_area(1.5, 2