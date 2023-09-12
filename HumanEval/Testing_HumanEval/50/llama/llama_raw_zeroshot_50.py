[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def encode_shift(s: str):
    
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

# test case
def test():
    assert [/INST]  Gladly! Here are some test cases for the `encode_shift` and `decode_shift` functions in Python:
```python
# Test encode_shift
def test_encode_shift():
    input_strings = ["hello", "world", "python", ""]
    for input_string in input_strings:
        output = encode_shift(input_string)
        assert isinstance(output, str)
        # Check that the output is a string of lengths 4, 7, 7, and 1
        assert len(output) == 4
    # Test edge cases
    input_string = ""
    output = encode_shift(input_string)
    assert output == ""

    input_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = encode_shift(input_string)
    assert output == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Test decode_shift
def test_decode_shift():
    input_strings = ["hello", "world", "python", ""]
    for input