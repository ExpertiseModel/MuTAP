def f(n):
    
    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret



def test():

    assert f(2) == [2]    assert f(10) == [1, 2, 6, 24, 15, 120, 210, 300, 365, 462, 596]

    assert f(2) == [2]

    assert f(0) == []

    assert f(3) == [2, 3, 2]

    assert f(3) == [0]

    assert f(2) == [4]

    assert f(4) == [4]
    assert f(5) == [5]

    assert f(3) == [1, 3, 3]
    assert f(1) == [1]
    assert f(0) == []

