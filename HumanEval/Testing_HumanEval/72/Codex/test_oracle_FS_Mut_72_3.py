def will_it_fly(q,w):
   
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True



def test():
    assert will_it_fly( [1,2], 5) == False 
    assert will_it_fly( [3, 2, 3], 9) == True 
    assert will_it_fly( [3, 2, 3], 1) == False 
    assert will_it_fly( [3, 2], 5) == True 
    assert will_it_fly( [3], 5) == True 

test()
