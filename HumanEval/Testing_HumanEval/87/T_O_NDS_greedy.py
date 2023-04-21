def get_row(lst, x):
    
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
assert get_row([1, 2, 3, 4], 0) == [(0, 0), (0, 1), (0, 2), (0, 3)]
