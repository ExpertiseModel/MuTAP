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


# test case
def test():
   

    assert tri(0) == [1]

    assert tri(4) == [1, 3, 11, 17]

    assert tri(5) == [1, 3, 11, 17, 29]

    assert tri(2) == [1, 3]

    assert tri(3) == [1, 3, 6]

    assert tri(100) == [1, 3, 11, 17, 29, 47, 76, 105, 1