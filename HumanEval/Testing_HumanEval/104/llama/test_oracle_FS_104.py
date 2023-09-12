def unique_digits(x):
    
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)


#</code>
#<test>
def test():
    
    assert unique_digits("") == []

    assert unique_digits("5") == ["5"]

    assert unique_digits("22") == ["2", "22"]
    
    assert unique_digits("12345") == ["1", "2", "3", "4", "5"]