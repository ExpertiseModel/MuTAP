def unique_digits(x):
    
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)
assert unique_digits([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
