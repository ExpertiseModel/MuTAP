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
    assert [/INST]  Sure, here are some test cases for the `encode_shift` and `decode_shift` functions using Python:
```
--- Encoding Test Cases ---
def test_encode_shift_simple():
    s = "Hello World!"
    result = encode_shift(s)
    expected = "7eleHrLdWrld!"
    assert result == expected

def test_encode_shift_mixed_case():
    s = "HeLlO WoRld!"
    result = encode_shift(s)
    expected = "7ehLloWrld!"
    assert result == expected

--- Decoding Test Cases ---
def test_decode_shift_simple():
    s = "7eleHrLdWrld!"
    result = decode_shift(s)
    expected = "Hello World!"
    assert result == expected

def test_decode_shift_mixed_case():
    s = "7ehLloWrld!"
    result = decode_shift(s)
    expected = "HeLlO WoRld!"
    assert result == expected
```