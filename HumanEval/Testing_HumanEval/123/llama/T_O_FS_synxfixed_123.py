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


#</code>
#<test>
def test():
    
    assert get_odd_collatz(0) == []

    assert get_odd_collatz(2) == [2]

    assert get_odd_collatz(3) == [3]

    assert get_odd_collatz(10) == [1, 3, 9, 10, 16, 22, 28, 34, 42, 46, 50]