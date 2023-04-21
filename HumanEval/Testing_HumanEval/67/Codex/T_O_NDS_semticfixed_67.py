def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


def test():
    assert fruit_distribution('10 apple 11 orange',1) == -20
    assert fruit_distribution('1 orange 2 apple',0) == -3
