def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

 # generate test case for the function above

def test_triangle_area():
    assert triangle_area(3, 4, 5) == 6
    assert triangle_area(5, 12, 13) == 30
    assert triangle_area(1, 1, 1) == 0.43
    assert triangle_area(2, 2, 2) == 1.73
    assert triangle_area(3, 3, 3) == 3.9
    assert triangle_area(4, 4, 4) == 6.93
    assert triangle_area(5, 5, 5) == 10.83
    assert triangle_area(6, 6, 6) == 15.59
    assert triangle_area(7, 7, 7) == 21.22
    assert triangle_area(8, 8, 8) == 27.72
    assert triangle_area(9, 9, 9) == 35.09
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(11, 11, 11) == 52.36
    assert triangle_area(12, 12, 12) == 62.27
    