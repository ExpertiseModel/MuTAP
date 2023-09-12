[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result



# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `select_words` function:
```
def test():
    # Test empty string
    assert select_words("", 3) == []

    # Test single word
    assert select_words("Mary", 2) == ["Mary"]

    # Test multiple words
    assert select_words("Mary had a little lamb", 4) == ["little", "Mary", "lamb"]

    # Test incorrect input
    assert select_words("Not a valid string", 3) == []

    # Test edge cases
    assert select_words("", 0) == []
    assert select_words("Hello", 4) == ["Hello"]

    # Test special cases
    assert select_words("Uncle Sam", 3) == ["Uncle"]

    # Test all combinations
    assert select_words("Hello world", 4) == ["world", "Hello"]

    # Test with negative value
    assert select_words("Mary had a little lamb", -3) == []

    # Test with a large input
