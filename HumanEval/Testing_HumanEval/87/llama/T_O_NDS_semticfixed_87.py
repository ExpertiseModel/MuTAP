def get_row(lst, x):
    
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])


# test case

def test():
    # Test with a simple list

    # Test with a specific element in the list

    assert get_row([1, 2, 3, 4, 5], 2) == [0, 1, 2]
    # Test with multiple elements in the list

    assert get_row([1, 2, 3, 4, 5], [2,3]) == [0, 1, 2, 3, 4]
    # Test with a list with no elements that match the given element

    assert get_row([1, 2, 3, 4, 5], 6) == []
    # Test with a list with multiple elements that match the given element

    assert get_row( [1, 2, 3, 4, 5, 2], 2) == [0, 2, 3, 4]