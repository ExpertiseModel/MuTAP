
def top_k(lst, k):
    ls = []
    for i in range(k):
        ls.append(max(lst))
        lst.remove(max(lst))
    return ls

def test():
    assert top_k([3, 8, 1, 0, 5, 7, 2, 10], 4) == [10, 8, 7, 3]
    assert top_k([10, 1, 12, 9, 2], 2) == [12, 10]
    assert top_k([12, 10, 8, 7, 3], 5) == [12, 10, 8, 7, 3]
    print("All tests passed!")

test()