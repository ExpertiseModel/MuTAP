def get_max_triples(n):
    
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)


# test case
def test():
   
    # Test 1: Valid input
    assert get_max_triples(1) == 0

    # Test 2: Small input
    assert get_max_triples(3) == 3

    # Test 3: Large input
    assert get_max_triples(100) == 27

    # Test 4: Edge case
    assert get_max_triples(2) == 1

    # Test 5: Input not in the range of [1,n]
    assert get_max_triples(-1) == 0

    # Test 6: Input equal to n
    assert get_max_triples(1) == 0

    # Test 1: Valid input

    assert get_max_triples(1) == 0
