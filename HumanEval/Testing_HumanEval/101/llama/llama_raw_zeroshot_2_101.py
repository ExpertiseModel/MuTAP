[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()


# test case
def test():
    assert [/INST]  Here are some test cases for the `words_string` function:
```
test_cases = [
    {"function_call": "words_string('Hello, how are you?')", "expected_output": ["Hello", "how", "are", "you"]},
    {"function_call": "words_string('One, two, three, four, five')", "expected_output": ["One", "two", "three", "four", "five"]},
    {"function_call": "words_string('')", "expected_output": []},
    {"function_call": "words_string(';')", "expected_output": []},
    {"function_call": "words_string('" + ',').join(['a', 'b', 'c']) + "'", "expected_output": ["a", "b", "c"]},
    {"function_call": "words_string('a-b-c')", "expected_output": ["a", "b", "c"]},
    {"function_call": "words_string('A1, B2, C3, D4, E5')", "expected