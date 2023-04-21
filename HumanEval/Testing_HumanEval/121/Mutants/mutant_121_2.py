def solution(lst):
    
   return sum([x for (idx, x) in enumerate(lst) if (idx % 2 == 0 or x % 2 == 1)])
