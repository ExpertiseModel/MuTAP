def sort_array(array):
    
   return [] if len(array) == 0 else sorted(array, reverse=(array[0] + array[-1]) * 2 == 0)
