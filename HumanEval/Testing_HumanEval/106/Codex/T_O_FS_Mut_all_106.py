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

    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(10) == [1, 2, 6, 24, 15, 720, 28, 40320, 45, 3628800]
