

def sort_age(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i][1] < lst[j][1]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    return lst



def test():
    assert sort_age([["Quincy", 31], ["Adams", 23], ["Joe", 41]]) == [['Joe', 41], ['Quincy', 31], ['Adams', 23]]
    assert sort_age([["Quincy", 31], ["Adams", 51], ["Joe", 41]]) == [['Adams', 51], ['Joe', 41], ['Quincy', 31]]
    assert sort_age([["Quincy", 31], ["Adams", 51], ["Joe", 10]]) == [['Adams', 51], ['Quincy', 31], ['Joe', 10]]
    assert sort_age([]) == []
    assert sort_age([["Quincy", 31]]) == [["Quincy", 31]]
