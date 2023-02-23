#https://leetcode.com/problems/3sum-closest/
#https://www.educative.io/courses/grokking-the-coding-interview/3YlQz7PE7OA
import math
def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    small_diff = math.inf
    for i in range(len(arr)):
        left = i +1
        right= len(arr) - 1
        while left < right:
            target_diff = target_sum - (arr[i] + arr[left]+ arr[right])
            print(target_diff)
            if target_diff == 0:
                return target_sum
            if abs(target_diff) < small_diff:
                small_diff = target_diff
            if target_diff < 0:
                right = right -1
            else:
                left = left + 1
    return target_sum - small_diff
    

output = triplet_sum_close_to_target([-1,2,1,-4], 1)
print('!!')
print(output)
# output = triplet_sum_close_to_target([-3, -1, 1, 2], 1)
# print('!!')
# print(output)
# output = triplet_sum_close_to_target([1, 0, 1, 1], 100)
# print('!!')
# print(output)