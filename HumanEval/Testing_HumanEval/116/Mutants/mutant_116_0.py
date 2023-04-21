def sort_array(arr):
    
   return sorted(sorted(arr), key=lambda x: (bin(x)[:].count('1')))
