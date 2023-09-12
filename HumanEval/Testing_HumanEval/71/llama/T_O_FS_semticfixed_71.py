def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area


#</code>
#<test>

def test():
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(4, 5, 6) == 9.92
    assert triangle_area(5, 6, 7) == 14.7
#</test>
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(1, 2, 0) == -1
    assert triangle_area(1, 0, 3) == -1
    assert triangle_area(0, 1, 3) == -1
