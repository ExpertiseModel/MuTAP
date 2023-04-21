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
    assert get_closest_vowel('ab') == ""
    assert get_closest_vowel('aa') == ""
    assert get_closest_vowel('mb') == ""
    assert get_closest_vowel('abk') == ""
    assert get_closest_vowel('b') == ""
    assert get_closest_vowel('a') == ""
    assert get_closest_vowel('e') == ""
    assert get_closest_vowel('eb') == ""
    assert get_closest_vowel('ee') == ""
    assert get_closest_vowel('o') == ""
    assert get_closest_vowel('i') == ""
    assert get_closest_vowel('abc') == ""
    assert get_closest_vowel('def') == "e"
    assert get_closest_vowel('ghi') == ""
    assert get_closest_vowel('jkl') == ""
    assert get_closest_vowel('mno') == ""
    assert get_closest_vowel('pqr') == ""
    assert get_closest_vowel('stu') == ""
    assert get_closest_vowel('vwxyz') == ""
    assert get_closest_vowel('ABC') == ""
    assert get_closest_vowel('DEF') == "E"
    assert get_closest_vowel('GHI') == ""

    assert get_closest_vowel('ab') == ""
    assert get_closest_vowel('aa') == ""
    assert get_closest_vowel('mb') == ""
    assert get_closest_vowel('abk') == ""
    assert get_closest_vowel('b') == ""
    assert get_closest_vowel('a') == ""
    assert get_closest_vowel('e') == ""
    assert get_closest_vowel('eb') == ""
    assert get_closest_vowel('ee') == ""
    assert get_closest_vowel('o') == ""
    assert get_closest_vowel('i') == ""

    assert get_closest_vowel('eb') == ""
    assert get_closest_vowel('ee') == ""

    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("aa") == ""
    assert get_closest_vowel("mb") == ""
    assert get_closest_vowel("abk") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("e") == ""
    assert get_closest_vowel("eb") == ""
    assert get_closest_vowel("ee") == ""
    assert get_closest_vowel("o") == ""
    assert get_closest_vowel("i") == ""

    assert get_closest_vowel('ab') == ""
    assert get_closest_vowel('aa') == ""
    assert get_closest_vowel('mb') == ""
    assert get_closest_vowel('abk') == ""
    assert get_closest_vowel('b') == ""
    assert get_closest_vowel('a') == ""
    assert get_closest_vowel('e') == ""
    assert get_closest_vowel('eb') == ""
    assert get_closest_vowel('ee') == ""
    assert get_closest_vowel('o') == ""
    assert get_closest_vowel('i') == ""

    assert get_closest_vowel('ab') == ""
    assert get_closest_vowel('aa') == ""
    assert get_closest_vowel('mb') == ""
    assert get_closest_vowel('abk') == ""
    assert get_closest_vowel('b') == ""
    assert get_closest_vowel('a') == ""
    assert get_closest_vowel('e') == ""
    assert get_closest_vowel('eb') == ""
    assert get_closest_vowel('ee') == ""
    assert get_closest_vowel('o') == ""
    assert get_closest_vowel('i') == ""

    assert get_closest_vowel('ab') == ""
    assert get_closest_vowel('aa') == ""
    assert get_closest_vowel('mb') == ""
    assert get_closest_vowel('abk') == ""
    assert get_closest_vowel('b') == ""
    assert get_closest_vowel('a') == ""
    assert get_closest_vowel('e') == ""
    assert get_closest_vowel('eb') == ""
    assert get_closest_vowel('ee') == ""
    assert get_closest_vowel('o') == ""
    assert get_closest_vowel('i') == ""

    assert get_closest_vowel('u') == ""

    assert get_closest_vowel('ab') == ""
    assert get_closest_vowel('aa') == ""
    assert get_closest_vowel('mb') == ""
    assert get_closest_vowel('abk') == ""
    assert get_closest_vowel('a') == ""
    assert get_closest_vowel('e') == ""
    assert get_closest_vowel('eb') == ""
    assert get_closest_vowel('ee') == ""
    assert get_closest_vowel('i') == ""

    assert get_closest_vowel('bb') == ""
    assert get_closest_vowel('be') == "e"
    assert get_closest_vowel('ad') == ""
    assert get_closest_vowel('d') == ""
    assert get_closest_vowel('j') == ""
    assert get_closest_vowel('b') == ""
    assert get_closest_vowel('i') == "i"

    assert get_closest_vowel('ab') == ""
