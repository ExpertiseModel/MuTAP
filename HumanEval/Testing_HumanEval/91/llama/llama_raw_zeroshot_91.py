[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


# test case
def test():
    assert [/INST]  Certainly! Here are some test cases for the `is_bored` function in Python using the `unittest` module:
```
import unittest

class TestIsBored(unittest.TestCase):
    def test_single_word(self):
        text = "I am bored."
        self.assertEqual(is_bored(text), 1)
    def test_two_words(self):
        text = "I am really bored."
        self.assertEqual(is_bored(text), 2)
    def test_ends_with_period(self):
        text = "I am so bored."
        self.assertEqual(is_bored(text), 1)
    def test_ends_with_question(self):
        text = "I am wondering if I am bored."
        self.assertEqual(is_bored(text), 1)
    def test_ends_with_exclamation(self):
        text = "I am so bored!!"
        self.assertEqual(is_bored(text), 1)
