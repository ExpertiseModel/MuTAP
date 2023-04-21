def unique_digits(x):
    
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

def test():
    assert unique_digits([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
    assert unique_digits([100, 200, 300, 400, 500, 600, 700, 800, 900]) == [100, 200, 300, 400, 500, 600, 700, 800, 900]
    assert unique_digits([11, 22, 33, 44, 55, 66, 77, 88, 99]) == [11, 22, 33, 44, 55, 66, 77, 88, 99]
    assert unique_digits([1, 1, 1, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [1, 3, 7]