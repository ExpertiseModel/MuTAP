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


#</code>
#<test>
def test():
    
    assert f(4) == [0, 2, 6, 0]

    assert f(5) == [0, 1, 3, 5, 0]

    assert f(100) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    assert f(2) == [0, 1]

    assert f(-3) == [-2, -1, 0, 1, 2]

    assert f(-1) == [0]
    assert f(0) == [0]
    assert f(1) == [1]