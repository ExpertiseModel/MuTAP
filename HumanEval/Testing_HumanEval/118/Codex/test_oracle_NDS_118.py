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
    assert(get_closest_vowel('ab') == 'a')
    assert(get_closest_vowel('aa') == 'a')
    assert(get_closest_vowel('mb') == 'm')
    assert(get_closest_vowel('abk') == 'a')
    assert(get_closest_vowel('b') == 'b')
    assert(get_closest_vowel('a') == 'a')
    assert(get_closest_vowel('e') == 'e')
    assert(get_closest_vowel('eb') == 'e')
    assert(get_closest_vowel('ee') == 'e')
    assert(get_closest_vowel('o') == 'o