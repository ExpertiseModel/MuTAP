def count_upper(s):
    
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count


# test case

def test():
    # Test that the function works for a simple string
    assert count_upper("Hello World!") == 0

    # Test that the function counts uppercase letters correctly

    assert count_upper("This is a TEST STRING") == 1

    # Test that the function raises a ValueError when passed a string that is not a string type
    assert count_upper(42) is not None
    # Test that the function counts uppercase letters even when the string is empty

    assert count_upper("") == 0

    # Test that the function counts uppercase letters for a string with multiple lines
    assert count_upper("""This is a multiple line string    with uppercase letters
    and lowercase letters too.""") == 6


