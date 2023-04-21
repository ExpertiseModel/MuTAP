def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

 # generate test case for the function above

def test_vowels_count():
    assert vowels_count("a") == 1
    assert vowels_count("b") == 0
    assert vowels_count("aeiou") == 5
    assert vowels_count("aeiouAEIOU") == 10
    assert vowels_count("Hello") == 2
    assert vowels_count("Hello World") == 3
    assert vowels_count("U") == 1
    assert vowels_count("u") == 1
    assert vowels_count("AEIOU") == 5
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOUaeiou") == 10
    assert vowels_count("aeiouAEIOU") == 10
    