def is_nested(string):
   
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

    


# test case


def test():
    assert is_nested('[[]]') == True 
    assert is_nested('[]]]]]]][[[[[]') == False 
    assert is_nested('[][]') == False 
    assert is_nested('[]') == False 
    assert is_nested('[[][]]') == True 
    assert is_nested('[[]][[') == True 
    assert is_nested('[[]]') == True  # Pass
    assert is_nested('[]]]]]]][[[[[]') == False  # Fail (added extra closing bracket)
    assert is_nested('[][]') == False  # Pass
    assert is_nested('[]') == False  # Pass
    assert is_nested('[[][]]') == True  # Pass
    assert is_nested('[[]][[]') == True  # Pass (mutated version)
    assert is_nested('[[]]') == True
    assert is_nested('[]][]]') == True
    # Test for the mutation where an extra opening bracket is added
    assert is_nested('[][]') == False
    assert is_nested('[][][]') == True
    # Test for the mutation where the order of the closing bracket is changed
    assert is_nested('[[]]') == True
    assert is_nested('[][][]') == True
    # Test for the mutation where the closing bracket is missing
    assert is_nested('[]') == False
    assert is_nested('[') == False
    # Test nestedness of nested brackets
    assert is_nested('[[]') == False
    # Test nestedness of deeply nested brackets
    assert is_nested('[[][]]') == True
    # Test nestedness of brackets with a gap
    assert is_nested('[[]]') == True
    # Test nestedness of brackets with different lengths
    assert is_nested('[[]][') == True
    # Test if the function can handle different types of brackets
    assert is_nested('{') == False
 


