def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    It is assumed that the input lists will be non-empty.
    """
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
            

 # generate test case for the function above

def test_exchange():
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5]) == "YES"
    assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == "NO"
    assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 4]) == "NO"
    assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]) == "YES"
    assert exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == "YES"
    assert exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5]) == "NO"
    assert exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]) == "YES"
    assert exchange([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]) == "YES"
    assert exchange([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6]) == "NO"
    assert exchange([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8]) == "YES"
    assert exchange([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]) == "YES"