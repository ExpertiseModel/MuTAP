def sort_age(lst):
    sort=[]
    while lst:
        biggest=0
        for i in lst:
            if i[1]>biggest:
                biggest=i[1]
        lst.remove(i)
        sort.append(i)
    return sort# Fill in your code here
    
