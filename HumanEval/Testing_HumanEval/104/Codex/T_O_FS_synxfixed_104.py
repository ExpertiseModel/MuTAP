def unique_digits(x):
    
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

def test():

    assert unique_digits([5, 0, 6, 0, 1, 4, 6]) == [5, 6]
    assert unique_digits([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]) == [1, 2, 3, 4, 5, 6]
    assert unique_digits([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5]) == [1, 2, 3, 4, 5]
