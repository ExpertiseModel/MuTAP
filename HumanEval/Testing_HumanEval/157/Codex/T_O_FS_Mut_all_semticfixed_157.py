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




def test():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 4, 3) == False
    assert right_angle_triangle(3, 'a', 5) == True    
    assert right_angle_triangle('1', 2, 3) == False   
    assert right_angle_triangle(2, 4, 3) == False
    assert right_angle_triangle(None, 4, 5) == False   
    assert right_angle_triangle(-1, 0, 5) == False
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(3.1, 4, 5) == False
    assert right_angle_triangle(1, 'b', 3) == False    
    assert right_angle_triangle(1, 'b', 'c') == False   
    assert right_angle_triangle(1, 'c', 3) == False    
    assert right_angle_triangle(0, 1, 2) == False
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(81, 1, 2) == False
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 4, 3) == False
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 1) == False 
    assert right_angle_triangle(2, 3, 2) == False
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(3.14, 4, 5) == False
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 4, 3) == False
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 0.6, 3) == False
    assert right_angle_triangle("a", 2, 3) == False    
    assert right_angle_triangle(0.6, 2, 3) == False
    assert right_angle_triangle(2, "a", 3) == False    
    assert right_angle_triangle(2, 3, "a") == False    
    assert right_angle_triangle('a', 2, 3) == False    
    assert right_angle_triangle(2, 3, 'a') == False    
    assert right_angle_triangle(2, 3, 'a') == False    
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2.2, 3.3, 4.4) == False
    assert right_angle_triangle('1', '1', '1') == False   
    assert right_angle_triangle('a', 'b', 'c') == False    
    assert right_angle_triangle(1, 3, '5') == False  
    assert right_angle_triangle({}, [], {}) == False   
    assert right_angle_triangle(1, 10, 20) == False
    assert right_angle_triangle(2, 4, 3) == False
