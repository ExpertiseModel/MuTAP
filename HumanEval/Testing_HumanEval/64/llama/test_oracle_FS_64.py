def vowels_count(s):
    
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels


#</code>
#<test>
def test():
    
    assert vowels_count("hello") == 2
    assert vowels_count("world") == 2
    assert vowels_count("python") == 3
#</test>

#<test>
    assert vowels_count("Hello, how are you?") == 4
    assert vowels_count("This is a string with several") == 6
    assert vowels_count("The quick brown fox jumps over the") == 5
#</test>

    assert vowels_count("") == 0

    assert vowels_count("abcdefghijklmnopqrstuvwxyz") == 14