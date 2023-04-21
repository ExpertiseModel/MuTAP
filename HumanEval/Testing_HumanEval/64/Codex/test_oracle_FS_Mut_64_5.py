def vowels_count(s):
    
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels



def test():
    vowels_count("abcdefghijklmnopqrstuvwxyz") == 5
    assert 
    vowels_count("code") == 2
    assert 
    vowels_count("Kata") == 2
    assert 
    vowels_count("KAY") == 2
    # The following case is an improvement so it should be generated as a
    # test case
    assert vowels_count("cody") == 3

