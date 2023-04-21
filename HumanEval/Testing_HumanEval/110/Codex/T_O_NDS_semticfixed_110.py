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
            


def test():
    assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == "NO"
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5]) == "YES"
    assert exchange([1, 2,3,4], [1, 2, 3, 4, 5]) == "YES"
