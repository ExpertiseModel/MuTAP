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
    assert f(2) == [3, 4, 3, 4]
    assert f(3) == [8, 18, 21, 11]
    assert f(5) == [44, 136, 464, 352, 272]
    assert f(10) == [945, 3876, 16804, 146376, 1302528, 13785968, 122300488, 1312252032, 11704338400]
