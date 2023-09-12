[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `words_in_sentence` function:
```

def test():
    # Test 1: Valid sentence
    sentence = "This is a test"
    assert words_in_sentence(sentence) == "is"

    # Test 2: Valid sentence with multiple words
    sentence = "lets go for swimming"
    assert words_in_sentence(sentence) == "go for swimming"

    # Test 3: Invalid sentence
    sentence = "This is not a test"
    assert words_in_sentence(sentence) == ""

    # Test 4: Edge case - very short sentence
    sentence = "x"
    assert words_in_sentence(sentence) == ""

    # Test 5: Edge case - very long sentence
    sentence = "This is a very very very very very very very very very very long sentence"
    assert words_in_sentence(sentence) == "very very very very very very very very long"


# Test 6: Special cases
sentence = "Hello "