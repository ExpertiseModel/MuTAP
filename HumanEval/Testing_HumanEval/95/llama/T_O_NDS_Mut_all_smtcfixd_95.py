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

    assert check_dict_case({"apple": 1, "banana": 2, "orange": 3}) == True



    # expected result: "mixed"

    assert check_dict_case({"Apple": 1, "baNana": 2, "OrAnGe": 3}) == False

    assert check_dict_case({"apple": 1, "banana": 2, "orange": 3}) == True


    # expected result: "mixed"

    assert check_dict_case({"Apple": 1, "baNana": 2, "OrAnGe": 3}) == False


    # create a new dictionary with a mixed case key


    # expected result: "mixed"

    assert check_dict_case({"aPPlE": 1, "bAnAna": 2, "oRaNgE": 3}) == False
    assert check_dict_case({"apple": 1, "banana": 2, 3: "orange"}) == True
    assert check_dict_case({"apple": 1, "banana": 2, "orange": 3}) == True


    # expected result: "mixed"

    assert check_dict_case({"Apple": 1, "baNana": 2, "OrAnGe": 3}) == False

    # expected result: "upper"

    assert check_dict_case({"Apple": 1, "baNana": 2, "OrAnGe": "Upper"}) == False

    # expected result: "lower"

    assert check_dict_case({"Apple": 1, "baNana": 2, "OrAnGe": "lower"}) == False
    # create a dictionary with mixed case keys
    # expected result: "mixed"
    assert check_dict_case({'Apple': 1, 'baNana': 2, 'orange': 3}) == False

    # create a dictionary with only upper case keys
    # expected result: "lower"
    assert check_dict_case({'Apple': 1, 'ORANGE': 2, 'baNana': 3}) == False

    # create a dictionary with only lower case keys
    # expected result: "lower"
    assert check_dict_case({'apple': 1, 'banana': 2, 'orange': 3}) == True
    assert check_dict_case({ "APPLE": 1, "BANANA": 2, "ORANGE": 3 }) == True

