def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


def test():
    assert fruit_distribution('a 1 b 2 c 3', 5) == -1
    assert fruit_distribution('a a b b c c', 7) == 7
