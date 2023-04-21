def check_dict_case(dict):
    
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower" 




def test():
    assert check_dict_case({'a':1}) == True
    assert check_dict_case({'a':1, 'b':2}) == True
    assert check_dict_case({'a':1, 'b':2, '1':3}) == True
    assert check_dict_case({'a':1, 'b':2, '1':3}) == True
    assert check_dict_case({'A':1, 'B':2}) == True
    assert check_dict_case({'a':1, 'b':2, '1':3}) == True
    assert check_dict_case({'a':1, 'b':2, '1':3, '2':4, 'A':5}) == True
    assert check_dict_case({'a':1}) == True
    assert check_dict_case({'a':1, 'b':2}) == True
    assert check_dict_case({'a':1, 'b':2, '1':3}) == True
    assert check_dict_case({'a':1, 'b':2, '1':3, 'aa':4}) == True
    assert check_dict_case({'a':1, 'b':2, '1':3, 'aa':4, 'A':5}) == True
    assert check_dict_case({'a':1, 'b':2, '1':3, 'aa':4, 'A':5, 'BB':6}) == True
    assert check_dict_case({'a':1, 'b':2, 'c':3}) == True
    assert check_dict_case({'a':1, 'b':2, 'c':3, 'd':4}) == True
    assert check_dict_case({'a':1, '1':2, 'c':3}) == False
    assert check_dict_case({'a':1, '1':2, 'c':3, 'd':4}) == False
    assert check_dict_case({'a':1, 'b':2, '1':3}) == True
