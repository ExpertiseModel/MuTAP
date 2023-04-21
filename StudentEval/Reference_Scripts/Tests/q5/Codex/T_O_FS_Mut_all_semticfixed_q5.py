
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
    assert top_k([10,1,12,9,9],5)== [12, 10, 9, 9, 1]
    assert top_k([10,1,12,9,-9],5)== [12, 10, 9, 1, -9]
    assert top_k([10,1,12,9,-9],4)== [12, 10, 9, 1]
    assert(top_k([10,1,12,9,-9],3)==[12,10,9])
    assert(top_k([10,1,12,9,-9],2)==[12,10])
    assert(top_k([10,1,12,9,-9],1)==[12])
    assert top_k(lst=-1, k=-1) == []
    assert top_k(lst=-1, k=0) == []
    assert top_k(lst=[], k=0) == []
    assert top_k(lst=[], k=1) == []    
    assert top_k(lst=[], k=2) == []    
    assert top_k(lst=[], k=3) == []   
    assert top_k(lst=[1], k=0) == []
    assert top_k(lst=[1], k=1) == [1]
    assert top_k(lst=[1], k=2) == [1]    
    assert top_k(lst=[1], k=3) == [1]    
    assert top_k([3, 8, 1, 0, 5, 7, 2, 10], 4) == [10, 8, 7, 5]
    assert top_k([10, 1, 12, 9, 2], 2) == [12, 10]
    assert top_k([12, 10, 8, 7, 3], 5) == [12, 10, 8, 7, 3]


    