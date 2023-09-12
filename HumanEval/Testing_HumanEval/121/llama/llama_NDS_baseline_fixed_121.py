def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])


# test case

def test():
    assert solution([]) == 0
    assert solution([1]) == 1
