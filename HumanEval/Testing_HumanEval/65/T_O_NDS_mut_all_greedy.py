def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]
assert circular_shift(1000000000001, 3) == "0011000000000"
assert circular_shift(10, 2)== "10"
assert circular_shift(41, 3) == "14"
