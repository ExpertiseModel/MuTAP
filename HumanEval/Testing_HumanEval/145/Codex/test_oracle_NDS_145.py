def order_by_points(nums):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)

def test():
    assert order_by_points([1,2,3,4,5]) == [1,2,3,4,5]
    assert order_by_points([10,13,13,10,15,21,22,25,26,26]) == [10, 10, 13, 13, 15, 21, 22, 25, 26, 26]
    assert order_by_points([4,3,2,1,0]) == [0,1,2,3,4]
    assert order_by_points([-2,-1,0,1,2]) == [-2,-1,0,1,2]
    assert order_by_points([5,5,5,5,5]) == [5,5,5,5,5]
    print("All Tests Passed!")
test()
