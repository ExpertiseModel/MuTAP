def find_max(words):
   
   return sorted(words, key=lambda x: ((len(set(x)), x)))[0]
