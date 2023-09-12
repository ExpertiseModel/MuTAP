
def exchange(lst1, lst2):
    
    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            odd += 1
    for i in lst2:
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"
            


# test case

def test():
    # Test with lists of different sizes
    assert exchange([1, 2, 3], [4, 5, 6]) == "YES"
    assert exchange([1, 2, 3], [4, 5, 6, 7]) == "YES"
    # Test with odd and even elements
    assert exchange([1, 2, 3], [4, 5, 6]) == "YES"
    assert exchange([1, 2, 3], [4, 5, 6, 7]) == "YES"
    # Test with lists of different types
    assert exchange([1, 2, 3], [True, False, True]) == "NO"
    assert exchange([1, 2, 3], [False, True, False]) == "YES"
    # Test with negative inputs
