from script_113_cp_normal  import odd_count
def test_odd_count():
    assert odd_count(["123", "456", "789"]) == ["the number of odd elements 2 in the string 2 of the input.", "the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 3 in the string 3 of the input."]
    assert odd_count(["11", "22", "33"]) == ["the number of odd elements 2 in the string 2 of the input.", "the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 2 in the string 2 of the input."]
    assert odd_count(["1", "2", "3"]) == ["the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input."]
    assert odd_count(["0", "1", "2"]) == ["the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input."]
    assert odd_count(["00", "01", "02"]) == ["the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input."]
    assert odd_count(["000", "001", "002"]) == ["the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input."]
