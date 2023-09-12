def get_row(lst, x):
    
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])


#</code>
#<test>

def test():
    assert get_row([1, 2, 3, 4, 5], 2) == [(2, 2)]
#<test>

    assert get_row([], 2) == []

#<test>
    assert get_row([1, 2, 3, 4, 5], 6) == []
#<test
    assert get_row([1, 2, 3, 4, 5], 6) == []

    assert get_row([], 2, True)