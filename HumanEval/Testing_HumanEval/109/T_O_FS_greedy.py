def move_one_ball(arr):
    
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True
assert move_one_ball([17, 0, 0, 18, 4, 17, 6, 3, 19, 10, 2, 0, 17, 0, 6, 10]) == False
assert move_one_ball([1, 2, 3, 4, 5]) == True
