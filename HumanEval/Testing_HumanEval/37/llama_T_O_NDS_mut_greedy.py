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


assert sort_even([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
assert sort_even([]) == []
