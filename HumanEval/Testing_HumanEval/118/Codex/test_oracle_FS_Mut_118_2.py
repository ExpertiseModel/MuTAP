def get_closest_vowel(word):

    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""



def test():
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("aw") == ""
    assert get_closest_vowel("a w") == ""
    assert get_closest_vowel("a wl") == ""
    assert get_closest_vowel("al") == ""
    assert get_closest_vowel("a l") == ""
    assert get_closest_vowel("wal") == "w"
    assert get_closest_vowel("w a l") == "w"
    assert get_closest_vowel("w a l ") == "w"
    assert get_closest_vowel("awl") == ""
    assert get_closest_vowel("awl