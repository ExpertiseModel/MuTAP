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
    # Test with a right-angled triangle
    assert right_angle_triangle(3, 4, 5) == True
    # Test with a non-right-angled triangle
    assert right_angle_triangle(1, 2, 3) == False

    # Test with a triangle where two sides are equal
    assert right_angle_triangle(3, 3, 4) == False

    # Test with a triangle where one side is zero
    assert right_angle_triangle(0, 1, 2) == False

    # Test with a triangle where one side is negative
    assert right_angle_triangle(3, -4, 5) == True
