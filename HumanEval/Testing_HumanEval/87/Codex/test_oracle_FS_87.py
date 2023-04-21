def get_row(lst, x):
    
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

def test():
    assert get_row([[1, 2, 3, 4], [5, 4, 3, 2], [2, 3, 4, 1], [3, 5, 4, 2]], 2) == [1, 2, 3, 4]
    assert get_row([[1, 2, 3, 4], [5, 4, 3, 2], [2, 3, 4, 1], [3, 5, 4, 2]], 1) == [5, 4, 3, 2]
