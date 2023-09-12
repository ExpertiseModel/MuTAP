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
assert check_dict_case({"apple": 1, "banana": 2, 3: "orange"}) == True
assert check_dict_case({ "APPLE": 1, "BANANA": 2, "ORANGE": 3 }) == True
assert check_dict_case({'Apple': 1, 'baNana': 2, 'orange': 3}) == False
