def find_max(words):
   
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]
assert find_max(['hello', 'world', 'hello', 'universe', 'universe', 'hello']) == 'universe'
