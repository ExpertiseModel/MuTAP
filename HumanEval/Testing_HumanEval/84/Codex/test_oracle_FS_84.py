def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]

def test():
    assert solve(19) == "10111"
    assert solve(20) == "101111"
    assert solve(21) == "1011101"
    assert solve(22) == "10111011"
    assert solve(23) == "101110110"
    assert solve(24) == "1011101110"
    assert solve(25) == "10111011100"
    assert solve(26) == "101110111010"
    assert solve(27) == "1011101110101"
    assert solve(28) == "10111011101011"
    assert solve(29) == "101110111010110"
    assert solve(30) == "1011101110101110"
