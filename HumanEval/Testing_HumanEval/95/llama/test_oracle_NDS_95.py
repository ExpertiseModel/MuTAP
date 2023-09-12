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


# test case
def test():
   
    # create a dictionary with only strings as keys


    # expected result: "start"

    assert check_dict_case({"apple": 1, "banana": 2, "orange": 3}) == "start"



    # expected result: "mixed"

    assert check_dict_case({"Apple": 1, "baNana": 2, "OrAnGe": 3}) == "mixed"