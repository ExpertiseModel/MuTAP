def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])
assert solution([1, 0, 1, 1, 0, 1, 0]) == 2
