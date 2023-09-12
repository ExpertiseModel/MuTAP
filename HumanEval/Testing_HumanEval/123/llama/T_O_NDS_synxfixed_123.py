
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


# test case
def test():
   
    # Test 1: Passing small numbers
    assert get_odd_collatz(1) == [1]

    # Test 2: Passing even number
    assert get_odd_collatz(2) == []

    # Test 3: Passing a large number
    assert get_odd_collatz(1000) == [1001, 500, 250, 125, 63, 31, 16, 8, 4, 2, 1]

    # Test 4: Testing the loop termination