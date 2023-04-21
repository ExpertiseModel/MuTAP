def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area



def test():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(5, 1, 4) == -1
    assert triangle_area(5, 6, 1) == -1
    assert triangle_area(-1, -1, -1) == -1
    assert triangle_area(-1, -1, 2) == -1
    assert triangle_area(2, -1, -1) == -1
    assert triangle_area(-1, 2, -1) == -1
    assert triangle_area(-1, 2, 2) == -1
    assert triangle_area(2, -1, 2) == -1
    assert triangle_area(4, 4, 4) == 6.0
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(5, 1, 4) == -1
    assert triangle_area(5, 6, 1) == -1
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(1, 2, 2) == -1
    assert triangle_area(5, 1, 4) == -1
    assert triangle_area(5, 6, 1) == -1