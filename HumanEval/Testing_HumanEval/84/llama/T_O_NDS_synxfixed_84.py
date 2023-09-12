
def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]


# test case
def test():
    # Test with small numbers
    assert solve(3) == "011"
    assert solve(4) == "100"
    assert solve(5) == "10101"
    # Test with larger numbers
    assert solve(10) == "1000000001"
    assert solve(100) == "100000000000000000000000000000001"
    # Test with negative numbers
    assert solve(-3) == "-111"
    assert solve(-4) == "-1000"
    assert solve(-5) == "-101010"
    # Test with zero
    assert solve(0) == "0"

    # Test with extremely large numbers