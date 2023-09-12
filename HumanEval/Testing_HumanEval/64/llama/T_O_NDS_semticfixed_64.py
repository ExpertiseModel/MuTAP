def vowels_count(s):
    
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels


# test case

def test():
    # Case 1: Testing with a string containing only vowels
    assert vowels_count("aeiouAEIOU") == 10

    # Case 2: Testing with a string containing only consonants
    assert vowels_count("bcdefghijklmnopqrstuvwxyz") == 4

    # Case 3: Testing with a string containing a mixture of vowels and consonants
    assert vowels_count("aeiouAEIOUbcd") == 10

    # Case 4: Testing with a string containing a vowel followed by a consonant
    assert vowels_count("aeiouAEIOUy") == 11

    # Case 5: Testing with a string containing a vowel followed by another vowel
    assert vowels_count("aeiouAEIOUaeiou") == 15

    #
