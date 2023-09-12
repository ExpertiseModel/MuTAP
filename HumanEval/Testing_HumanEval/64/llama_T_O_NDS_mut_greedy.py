def vowels_count(s):
    
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels
assert vowels_count("aeiouAEIOUy") == 11
assert vowels_count("aeiouAEIOU") == 10
