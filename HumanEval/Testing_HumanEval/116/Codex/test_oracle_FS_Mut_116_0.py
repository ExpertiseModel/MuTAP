def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))



def test():
    assert sort_array([-1, -6]) == [-6, -1]
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]

