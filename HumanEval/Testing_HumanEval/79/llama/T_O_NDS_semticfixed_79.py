
def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"


# test case

def test():
    assert decimal_to_binary(0) == "db0db"

    assert decimal_to_binary(123) == "db1111011db"

    assert decimal_to_binary(-123) == "dbb1111011db"

    assert decimal_to_binary(-6) == "dbb110db"
 
