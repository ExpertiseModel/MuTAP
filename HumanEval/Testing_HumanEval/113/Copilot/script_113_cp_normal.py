def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    """
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res

 # generate test case for the function above
def test_odd_count():
    assert odd_count(["123", "456", "789"]) == ["the number of odd elements 3n the str3ng 3 of the 3nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 3n the str3ng 3 of the 3nput."]
    assert odd_count(["2", "4", "6"]) == ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str0ng 0 of the 0nput."]
    assert odd_count(["13579", "24680", "86420", "35791"]) == ["the number of odd elements 5n the str5ng 5 of the 5nput.", "the number of odd elements 3n the str3ng 3 of the 3nput.", "the number of odd elements 4n the str4ng 4 of the 4nput.", "the number of odd elements 5n the str5ng 5 of the 5nput."]
    assert odd_count(["1", "2", "3", "4", "5", "6", "7", "8", "9"]) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput."]
    assert odd_count(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) == ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str1ng 1 of the 1nput."]