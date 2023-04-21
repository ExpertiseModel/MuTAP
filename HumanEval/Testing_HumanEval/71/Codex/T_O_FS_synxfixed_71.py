def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

def test():
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(3, 3, 3) == 3.0
    assert triangle_area(2.5, 2, 2.5) == 2.25
    assert triangle_area(2.5, 3, 2) == 2.25
    assert triangle_area(1, 2, 2) == 0.5
    assert triangle_area(1, 3, 2) == 0.5
