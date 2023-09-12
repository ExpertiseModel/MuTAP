def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


# test case

def test():
    assert fruit_distribution("apple banana orange", 5) == 5
    assert fruit_distribution("apple banana orange", 5) == 5
