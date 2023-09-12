def get_closest_vowel(word):

    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""


#</code>
#<test>
def test():
    
    assert get_closest_vowel("hello") == "e"
    assert get_closest_vowel("apple") == "a"
    assert get_closest_vowel("box") == ""

    assert get_closest_vowel("a") == "a"
    assert get_closest_vowel("e") == "e"


    assert get_closest_vowel("banana") == "a"
    assert get_closest_vowel("oranges") == "a"


    assert get_closest_vowel("hellohowareyou") == "o"
    assert get_closest_vowel("tigers") == "a"