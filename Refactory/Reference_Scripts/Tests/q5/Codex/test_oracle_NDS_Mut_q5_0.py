
def top_k(lst, k):
    ls = []
    for i in range(k):
        ls.append(max(lst))
        lst.remove(max(lst))
    return ls



def test():
    assert top_k([3, 8, 1, 0, 5, 7, 2, 10], 0) == []
    assert top_k([], 1) == []
    assert top_k([], 0) == []


