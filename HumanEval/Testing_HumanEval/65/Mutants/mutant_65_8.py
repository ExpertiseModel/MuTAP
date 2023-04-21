def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
       return s[:]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]
