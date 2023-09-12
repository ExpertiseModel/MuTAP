def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])




#<test>
def test():
    assert solution([]) == 0
    assert solution([1]) == 1
    assert solution([1, 2, 3, 4, 5, 6]) == 3
    assert solution([1, 2, 3, 4, 5, 6, 7]) == 4
    assert solution([1, 2, 3, 4, 5, 6, 7, 8]) == 5
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 6

    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10