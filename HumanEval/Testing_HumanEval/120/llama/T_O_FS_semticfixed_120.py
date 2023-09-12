def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


#</code>
#<test>

def test():
    assert maximum([], 0) == []

    assert maximum([3], 1) == [3]

    assert maximum( [1, 2, 3], 1) == [3]

    assert maximum([3, 2, 1], 1) == [3]

    assert maximum([-1, 0, 1, 2, -3], 1) == [2]
