[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def encode_cyclic(s: str):
    
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    
    return encode_cyclic(encode_cyclic(s))




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `encode_cyclic` function:
1. Test with a single-character string:
```python
assert encode_cyclic("a") == "a"
```
2. Test with a string of length 3:

```python
assert encode_cyclic("abc") == "aabbc"
```
3. Test with a string of length 6:

```python
assert encode_cyclic("abcdef") == "aabbcdef"
```
4. Test with a string of length 9:

```python
assert encode_cyclic("abcdefghijklmn") == "aabbcdefghijklmnopqrstuvw"
```
5. Test with a string of length 12:

```python
assert encode_cyclic("abcdefghijklmnopqrstuvwxyz") == "aabbcdefghijklmnopqrstuvwxyzaabbcdefghijklmnopqrstuvw"
```
6. Test with a string of length 15:

```python
assert encode