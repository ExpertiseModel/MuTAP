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
    assert get_odd_collatz(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert get_odd_collatz(9) == [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    pass


def get_even_collatz(n):
    even_collatz = []
    while n > 1:
        if n % 2 == 1:
            n = n * 3 + 1
            even_collatz.append(int(n))
        else:
            n = n // 2
            even_collatz.append(int(n))
    return sorted(even_collatz)


def get_odd_collatz(n):
   