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


#</code>
#<test>
def test():
  
    assert check_dict_case({}) == False


    assert check_dict_case({"ABC": 1, 2: "def", "ghi": 3.0}) == "mixed"

    assert check_dict_case({"ABC": 1, "def": 2, "GHI": 3.0}) == "upper"


    assert check_dict_case({"abc": 1, "def": 2, "ghi": 3.0}) == "lower"


    dict = {"!"asma": 1, "$": 2, "?jkl