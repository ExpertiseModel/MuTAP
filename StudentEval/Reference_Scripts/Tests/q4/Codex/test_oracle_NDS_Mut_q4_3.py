

def sort_age(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i][1] < lst[j][1]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    return lst



def test():
    assert sort_age(None) == ValueError("Exception: argument must be list")
    assert sort_age([]) == []
    assert sort_age(["a", "b"]) == ["a", "b"]
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [("M", 30), ("M", 23), ("F", 19)]

