def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]


#</original code>


#<test>
def test():
   
    assert solve(2) == "101"

# Test 2

    assert solve(3) == "1001"

# Test 3
    assert solve(23) == "531223"

    assert solve(2) == "101"

# Test 2
    assert solve(3) == "1001"

# Test 3
    assert solve(23) == "531223"