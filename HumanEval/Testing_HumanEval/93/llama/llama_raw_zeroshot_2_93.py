[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


# test case
def test():
    assert [/INST]  Here are some test cases for the `encode` function:
```
test_cases = [
    {'message': 'Hello', 'expected': 'HlLlO'},
    {'message': 'heLlO', 'expected': 'hElLlO'},
    {'message': 'A', 'expected': 'A'},
    {'message': 'aeiou', 'expected': 'aeiouAEIOU'},
    {'message': 'ABC', 'expected': 'ABC'},
    {'message': '中文字符', 'expected': '㊙ㄧㄢㄣㄤㄥ'},
    {'message': '😃', 'expected': '😃'},
    {'message': 'ö', 'expected': 'Oe'},
    {'message': 'Ü', 'expected': 'Ue'},
    {'message': 'π', 'expected': 'Pi'},
    {'message': ' foo', 'expected': 'foo'},
]

for test in test_cases:
    print(f"Testing {test['message']}: {test['expected']}")
    result =