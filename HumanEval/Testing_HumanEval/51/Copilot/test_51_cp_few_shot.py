from script_51_cp_few_shot import remove_vowels


def test_remove_vowels():
    assert remove_vowels("a") == ""
    assert remove_vowels("b") == "b"
    assert remove_vowels("aeiou") == ""
    assert remove_vowels("aeiouAEIOU") == ""
    assert remove_vowels("Hello") == "Hll"
    assert remove_vowels("Hello World") == "Hll Wrld"
    assert remove_vowels("U") == ""
    assert remove_vowels("u") == ""
    assert remove_vowels("AEIOU") == ""
    assert remove_vowels("aeiou") == ""
    assert remove_vowels("AEIOUaeiou") == ""
    assert remove_vowels("aeiouAEIOU") == ""
    assert remove_vowels("f") == "f"
    assert remove_vowels("g") == "g"
    assert remove_vowels("h") == "h"
    assert remove_vowels("j") == "j"
    assert remove_vowels("k") == "k"
