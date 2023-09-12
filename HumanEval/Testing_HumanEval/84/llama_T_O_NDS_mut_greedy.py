def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]
assert solve(3) == 11
