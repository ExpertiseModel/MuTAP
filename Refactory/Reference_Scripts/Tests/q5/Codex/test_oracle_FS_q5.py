def top_k(lst, k):
    ls = []
    for i in range(k):
        ls.append(max(lst))
        lst.remove(max(lst))
    return ls

def test():
    assert top_k([10,1,12,9,9],5)==[12,10,9,9,10]
    assert top_k([10,1,12,9,-9],5)==[12,10,9,-9,10]
    assert top_k([10,1,12,9,-9],4)==[12,10,9,-9]
    assert top_k([10,1,12,9,-9],3)==[12,10,9]
    assert top_k([10,1,12,9,-9],2)==[12,10]
    assert top_k([10,1,12,9,-9],1)==[12]
