[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def get_closest_vowel(word):

    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `get_closest_vowel` function:
```
def test_empty_input():
    word = ""
    result = get_closest_vowel(word)
    assert result == ""

def test_short_word():
    word = "cat"
    result = get_closest_vowel(word)
    assert result == "a"

def test_vowel_at_beginning():
    word = "a"
    result = get_closest_vowel(word)
    assert result == "a"

def test_vowel_at_end():
    word = "ocean"
    result = get_closest_vowel(word)
    assert result == "o"

def test_vowel_midword():
    word = "hello"
    result = get_closest_vowel(word)
    assert result == "e"

def test_not_vowel():
    word = "not"
    result = get_closest_vowel(word)
    assert result == ""
