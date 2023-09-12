[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `split_words` function:
```
test_cases = [
    # Test with a string containing only whitespace
    ("   Hello   ", []),
    # Test with a string containing only commas
    ("Hello,world!", []),
    # Test with a string containing both whitespace and commas
    ("Hello world, nice day!", ["Hello", "world", "nice", "day"]),
    # Test with a string of odd length
    ("abcdefghijklmnop", [9]),
    # Test with a string of even length
    ("Hello world!", ["Hello", "world"]),
    # Test with a string containing letters of different cases
    ("HeLlO woRlD", ["H", "e", "l", "o", "w", "r", "l", "d"]),
    # Test with a string containing numbers and punctuation
    ("1 Hello world!", ["1", "Hello", "world"]),
    # Test with a string containing multiple consecutive whitespaces
    ("   Hello   ", ["Hello"]),
]

