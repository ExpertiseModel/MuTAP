[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `digitSum` function using Python:
```
class TestDigitSum:
    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)
    
    def test_lowercase_string(self):
        self.assertEqual(digitSum("hello"), 7)
    
    def test_uppercase_string(self):
        self.assertEqual(digitSum("HELLO"), 7)
    
    def test_mixed_case_string(self):
        self.assertEqual(digitSum("HeLlO"), 7)
    
    def test_whitespace_string(self):
        self.assertEqual(digitSum("   Hello   "), 7)

    def test_special_characters(self):
        self.assertEqual(digitSum("!@#$%"), 0)

if __name__ == "__main__":
    unittest.main()
```

Explanation:

* `test_empty_string`: Tests that the function returns the correct