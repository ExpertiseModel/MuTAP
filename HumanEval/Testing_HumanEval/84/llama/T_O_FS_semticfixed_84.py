def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]


#</original code>


#<test>

def test():
    assert solve(2) == 10

# Test 2

    assert solve(3) == 11

# Test 3
    assert solve(23) == 101

    assert solve(2) == 10

# Test 2
    assert solve(3) == 11

# Test 3
    assert solve(23) == 101
