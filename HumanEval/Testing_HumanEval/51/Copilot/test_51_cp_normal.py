from script_51_cp_normal import remove_vowels

def test_remove_vowels():
    assert remove_vowels("hello") == "hll"
    assert remove_vowels("world") == "wrld"
    assert remove_vowels("python") == "pythn"
    assert remove_vowels("javascript") == "jvscrpt"
    assert remove_vowels("java") == "jv"
    assert remove_vowels("ruby") == "rby"
    assert remove_vowels("php") == "ph"
    assert remove_vowels("c") == "c"
    assert remove_vowels("c++") == "c++"
    assert remove_vowels("c#") == "c#"
    assert remove_vowels("c") == "c"
    assert remove_vowels("c++") == "c++"
    assert remove_vowels("c#") == "c#"
    assert remove_vowels("c") == "c"
    assert remove_vowels("c++") == "c++"
    assert remove_vowels("c#") == "c#"
