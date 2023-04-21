def sort_even(l: list):
    
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans


assert sort_even([1,2,3,4,5,6,7,8]) == [1, 2, 3, 4, 5, 6, 7, 8]
