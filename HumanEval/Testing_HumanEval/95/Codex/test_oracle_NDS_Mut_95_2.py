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
    assert check_dict_case({"a": "b"}) == True
    assert check_dict_case({"a": "b", "c": "d"}) == True
    assert check_dict_case({"a": "b", "c": "d", "e": "f"}) == True
    assert check_dict_case({"a": "b", "c": "d", "e": "f", "1": "2"}) == True
    assert check_dict_case({'1': '2', '3': '4', '5': '6', '7': '8', '9': '10', '11': '12', '13': '14', '15': '16', '17': '18', '19': '20', '21': '22', '23': '24', '25': '26', '27': '28',