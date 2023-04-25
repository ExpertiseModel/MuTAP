
def top_k(lst, k):
    ls = []
    for i in range(k):
        ls.append(max(lst))
        lst.remove(max(lst))
    return ls



def test():
    assert top_k(lst=-1, k=-1) == None
    assert top_k(lst=-1, k=0) == []
    assert top_k(lst=[], k=0) == []
    assert top_k(lst=[], k=1) == []
    assert top_k(lst=[], k=2) == []
    assert top_k(lst=[], k=3) == []
    assert top_k(lst=[1], k=0) == []
    assert top_k(lst=[1], k=1) == [1]
    assert top_k(lst=[1], k=2) == [1]
    assert top_k(lst=[1], k=3) == [1]
    assert top_k(lst=[1, 2], k=0) ==