def will_it_fly(q,w):
   
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while not (i < j):
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True
