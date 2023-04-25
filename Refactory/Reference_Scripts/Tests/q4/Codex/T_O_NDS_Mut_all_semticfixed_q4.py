

def sort_age(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i][1] < lst[j][1]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    return lst



def test():
    assert sort_age([("M", 30), ("F", 19), ("M", 23)]) == [('M', 30), ('M', 23), ('F', 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30)])== [("M", 30), ("M", 23), ("F", 19)] 
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [("M", 30), ("M", 23), ("F", 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [("M", 30), ("M", 23), ("F", 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30)])== [('M', 30), ('M', 23), ('F', 19)]
    assert sort_age([("M", 30), ("F", 19), ("M", 23)]) == [('M', 30), ('M', 23), ('F', 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30)])== [("M", 30), ("M", 23), ("F", 19)] 
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [("M", 30), ("M", 23), ("F", 19)]
    assert sort_age([('M', 23), ('F', 19), ('M', 30)]) == [('M', 30), ('M', 23), ('F', 19)]
    assert sort_age([('M', 23), ('F', 19), ('M', 30)]) == [('M', 30), ('M', 23), ('F', 19)]
    assert sort_age([('M', 23), ('F', 19), ('M', 30)]) == [('M', 30), ('M', 23), ('F', 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [("M", 30), ("M", 23), ("F", 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30)])== [('M', 30), ('M', 23), ('F', 19)]
    assert sort_age([("M", 30), ("F", 19), ("M", 23)]) == [('M', 30), ('M', 23), ('F', 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30)])== [("M", 30), ("M", 23), ("F", 19)] 
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [("M", 30), ("M", 23), ("F", 19)]
