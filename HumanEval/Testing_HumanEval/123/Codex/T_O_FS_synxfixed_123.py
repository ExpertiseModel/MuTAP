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
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(2) == [1, 2]
    assert get_odd_collatz(6) == [1, 2, 3, 4, 5, 6]
    assert get_odd_collatz(15) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
