[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `right_angle_triangle` function:
```
def test_right_angle_triangle():
    # Test positive cases
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 6, 8) == True
    # Test negative cases
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 5, 6) == False
    # Test corner cases
    assert right_angle_triangle(1, 1, 1) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 3, 4) == False

# Run the test cases
if __name__ == "__main__":
    test.main()
```
In this code, we define a `test_right_angle_triangle` function that contains a list of test cases for the `right_angle_triangle` function. Each test case is defined using the `assert` statement,