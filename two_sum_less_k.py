#1099 Two Sum Less Than K60.5% Easy
import math
def two_sum_less_k(arr, k):
    arr.sort()
    if len(arr) ==1:
        return -1
    min_dff = math.inf
    for i in range(len(arr)):
        left = arr[i]
        right= len(arr) - 1
        while left < right:
            target_diff = k - (arr[left] + arr[right])
            if target_diff > 0:
                min_dff = min(min_dff,target_diff)
                left = left + 1
            else:
                right = right -1
    return k- min_dff
    

output = two_sum_less_k([34,23,1,24,75,33,54,8], 60)
print('!!')
print(output)