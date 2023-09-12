def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


#</code>
#<test>

def test():
    assert fruit_distribution("orange 3 orange 2 banana 1", 6) == 0
