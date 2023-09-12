[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def words_in_sentence(sentence):
    
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `words_in_sentence` function:
1. Test with a simple sentence:
```python
sentence = "This is a simple sentence."
assert words_in_sentence(sentence) == "This is simple sentence."
```
2. Test with a sentence containing multiple words with the same length:
```python
sentence = "The quick brown fox jumps over the fence."
assert words_in_sentence(sentence) == "The quick brown fox jumps over the fence."
```
3. Test with a sentence containing words of varying lengths:
```python
sentence = "The quick brown fox jumps over the fence quickly."
assert words_in_sentence(sentence) == "Quick brown fox jumps quickly over the fence."
```
4. Test with a sentence that contains a word that is not adjacent to any other word:
```python
sentence = "The quick brown fox jumped over the fence alone."
assert words_in_sentence(sentence) == "The quick brown fox alone jumped over the f