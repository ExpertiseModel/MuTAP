def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


#</code>
#<test>

def test():
    assert fruit_distribution("banana 3 apple 2 orange 1", 5) == -1
    assert fruit_distribution("banana 3 orange 2 apple 1", 7) == 1
    assert fruit_distribution("orange 3 apple 2 banana 1", 5) == -1
    assert fruit_distribution("orange 3 orange 2 banana 1", 6) == 0
    assert fruit_distribution("banana 3 banana 2 apple 1", 5) == -1
#</test>
