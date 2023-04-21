from script_19_cp_few_shot import sort_numbers

def test_sort_numbers():
    assert sort_numbers("one two three four five six seven eight nine zero") == "zero one two three four five six seven eight nine"
    assert sort_numbers("one two three four five six seven eight nine") == "one two three four five six seven eight nine"
    assert sort_numbers("one two three four five six seven eight") == "one two three four five six seven eight"
    assert sort_numbers("one two three four five six seven") == "one two three four five six seven"
    assert sort_numbers("one two three four five six") == "one two three four five six"
    assert sort_numbers("one two three four five") == "one two three four five"
    assert sort_numbers("one two three four") == "one two three four"
    assert sort_numbers("one two three") == "one two three"
    assert sort_numbers("one two") == "one two"
    assert sort_numbers("one") == "one"
    assert sort_numbers("") == ""