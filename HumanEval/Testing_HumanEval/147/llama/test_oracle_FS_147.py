def get_max_triples(n):
    
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)



def test():
   
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 2
    assert get_max_triples(3) == 3
    assert get_max_triples(4) == 6
    assert get_max_triples(5) == 10
#</test>
    assert get_max_triples(10) == 10
    assert get_max_triples(20) == 35
    assert get_max_triples(30) == 90
    assert get_max_triples(40) == 175
    assert get_max_triples(50) == 340

    assert get_max_triples(0) == 0