def find_averages_of_subarrays(K, arr):
  result = []
  win_start = 0
  win_end = 0
  win_sum = 0
  result = []
  for win_end in range(len(arr)-1):
    win_sum = win_sum + arr[win_end]
    if win_end >= K-1:
        result.append(win_sum/K)
        win_sum = win_sum - arr[win_start]
        win_start = win_start + 1

  return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()