from script_110_cp_normal  import exchange
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