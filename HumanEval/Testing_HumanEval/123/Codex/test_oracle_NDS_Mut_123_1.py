def get_odd_collatz(n):
    
    if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
            
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)



def test():
    assert get_odd_collatz(13) == [1,5,13]
    assert get_odd_collatz(9) == [1,5,7,9,11,13,17]
    assert get_odd_collatz(4) == [4]
    assert get_odd_collatz(5) == [5]
    assert get_odd_collatz(8) == [8,16]
    assert get_odd_collatz(24) == [24,12]
    assert get_odd_collatz(3) == [3,10,5]
    assert get_odd_collatz(10000) == [10000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, 9, 4, 2, 1]
