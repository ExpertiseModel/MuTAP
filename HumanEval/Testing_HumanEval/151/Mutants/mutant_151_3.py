def double_the_difference(lst):
    
   return sum([i ** 2 for i in lst if (i > 0 or i % 2 != 0 or '.' not in str(i))])
