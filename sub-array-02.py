import math
def smallest_subarray_sum(s, arr):
  # TODO: Write your code here
  #Input: [2, 1, 5, 2, 3, 2], S=7
  win_start = 0
  win_end = 0
  win_sum = 0
  min_len = math.inf
  for win_end in range(len(arr)):
    win_sum = win_sum + arr[win_end]
    print('win_sum'+str(win_sum))
    while win_sum >= s:
      min_len = min(min_len,win_end - win_start + 1)
      print(min_len)
      print('before win_sum'+str(win_sum))
      win_sum = win_sum - arr[win_start]
      print('after win_sum'+str(win_sum))
      win_start = win_start + 1
  
  print('min_len'+str(min_len))
  return min_len

smallest_subarray_sum(7, [2, 1, 5, 2, 8])