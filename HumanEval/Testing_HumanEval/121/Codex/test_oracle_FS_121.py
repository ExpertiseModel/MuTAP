def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])

def test():
    assert solution([1,2,3]) == 2
    assert solution([1,1,1]) == 0
    assert solution([1,1,1,3,3,3]) == 3
    assert solution([4,4,4,4,4,4]) == 0
    assert solution([4,4,4,3,3,4]) == 1
    assert solution([1,2,3,4,1]) == 3
    assert solution([1,0,5,0,5,5]) == 15
    assert solution([0,0,0]) == 0
