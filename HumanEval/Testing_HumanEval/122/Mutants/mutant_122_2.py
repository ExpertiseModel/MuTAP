def add_elements(arr, k):
    
   return sum((elem for elem in arr[:] if len(str(elem)) <= 2))
