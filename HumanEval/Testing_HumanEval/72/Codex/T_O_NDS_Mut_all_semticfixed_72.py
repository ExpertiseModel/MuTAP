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
    assert will_it_fly([1,1,1,1],3) == False
    assert will_it_fly([1,1,1,1],2) == False
    assert will_it_fly([2,2,2,2],3) == False
    assert will_it_fly([2,2,2,2],2) == False
    assert will_it_fly([2,2,2,1],3) == False
    assert will_it_fly([2,2,1,1],3) == False
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([1, 1, 1], 4) == True
    assert will_it_fly([2, 2, 2], 3) == False
    assert will_it_fly([2, 2, 2], 2) == False

    assert will_it_fly([1,1,1,1],3) == False
    assert will_it_fly([1,1,1,1],2) == False
    assert will_it_fly([2,2,2,2],3) == False
    assert will_it_fly([2,2,2,2],2) == False
    assert will_it_fly([2,2,2,1],3) == False
    assert will_it_fly([2,2,1,1],3) == False
    assert will_it_fly([2,2,1,1],3) == False
    assert will_it_fly([1,1,1,1],3) == False
    assert will_it_fly([1,1,1,1],1) == False
    assert will_it_fly([2,2,2,2],3) == False
    assert will_it_fly([2,2,2,2],1) == False
    assert will_it_fly([2,2,2,1],3) == True
    assert will_it_fly([2,2,1,1],3) == True

    assert will_it_fly([1, 1, 1, 1], 3) == False
    assert will_it_fly([1, 1, 1, 1], 2) == False
    assert will_it_fly([2, 2, 2, 2], 3) == False
    assert will_it_fly([2, 2, 2, 2], 2) == False
    assert will_it_fly([2, 2, 2, 1], 3) == False
