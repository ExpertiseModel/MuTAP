def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]


def test():
    assert solve(19) == "1010"
    assert solve(20) == "10"
    assert solve(21) == "11"
    assert solve(22) == "100"
    assert solve(23) == "101"
    assert solve(24) == "110"
    assert solve(25) == "111"
    assert solve(26) == "1000"
    assert solve(27) == "1001"
    assert solve(28) == "1010"
    assert solve(29) == "1011"
    assert solve(30) == "11"
