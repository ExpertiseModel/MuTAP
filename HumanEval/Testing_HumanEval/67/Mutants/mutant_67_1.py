def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
       if not (i.isdigit()):
            lis.append(int(i))
    return n - sum(lis)
