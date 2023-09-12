
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
    assert get_odd_collatz(2) == [1]

    # Test 3: Passing a large number
    assert get_odd_collatz(1000) == [1, 5, 23, 35, 47, 53, 61, 71, 91, 103, 107, 121, 125, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]

    # Test 4: Testing the loop termination

