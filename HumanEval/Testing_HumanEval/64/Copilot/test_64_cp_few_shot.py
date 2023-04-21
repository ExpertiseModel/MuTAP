from script_64_cp_few_shot import vowels_count



def test_vowels_count():
    assert vowels_count('') == 0
    assert vowels_count('a') == 1
    assert vowels_count('b') == 0
    assert vowels_count('aeiou') == 5
    assert vowels_count('aeiouAEIOU') == 10
    assert vowels_count('Hello') == 2
    assert vowels_count('Hello World') == 3
    assert vowels_count('U') == 1
    assert vowels_count('u') == 1
    assert vowels_count('AEIOU') == 5
    assert vowels_count('aeiou') == 5
    assert vowels_count('y') == 1
    assert vowels_count('Y') == 1
    assert vowels_count('yy') == 2
    assert vowels_count('yyY') == 3
    assert vowels_count('yyYy') == 4
    
