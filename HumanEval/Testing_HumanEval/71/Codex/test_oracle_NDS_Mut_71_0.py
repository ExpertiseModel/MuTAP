def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area



def test():
    assert triangle_area(-1, -1, -1) == -1
    assert triangle_area(-1, -1, 2) == -1
    assert triangle_area(2, -1, -1) == -1
    assert triangle_area(-1, 2, -1) == -1
    assert triangle_area(-1, 2, 2) == -1
    assert triangle_area(2, -1, 2) == -1
    assert -1.0 < triangle_area(1, 1, 2) <= 0.001
    assert -1.0 < triangle_area(2, 2, 1) <= 0.001
    assert -1.0 < triangle_area(1, 2, 2) <= 0.001
    assert triangle_area(4, 4, 4) == 6.0

