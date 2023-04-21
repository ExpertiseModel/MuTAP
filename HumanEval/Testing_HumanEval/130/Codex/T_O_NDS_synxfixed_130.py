def tri(n):
    
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri



def test():
    assert tri(0) == [1]
    assert tri(1) == [1, 3]
    assert tri(2) == [1, 3, 3]
    assert tri(3) == [1, 3, 5, 6]
    assert tri(4) == [1, 3, 5, 6, 10, 13]
    assert tri(5) == [1, 3, 5, 6, 10, 13, 21, 28]
    assert tri(6) == [1, 3, 5, 6, 10, 13, 21, 28, 36, 45, 55]
    print("Testing Passed!")