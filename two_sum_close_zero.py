import math

# x +y = 0
# x = -y
def two_sum_close_zero(A,target):
    A.sort()
    left = 0
    right = len(A) - 1
    min_left = 0
    min_right = 0
    minDiff = math.inf
    while left< right:
        curr_sum = A[left] + A[right]
        diff = abs(target - curr_sum)
        if (diff < minDiff):
            minDiff = diff
            min_left = A[left]
            min_right = A[right]
        elif (curr_sum < target):
            left = left +1
        elif (curr_sum > target):
            right = right - 1
        else:
            break
    return min_left,min_right
        
# nums = [1, 2, 3, 4, 5]
# target = 10
# print(two_sum_close_zero(nums,target))
#Output: [4, 5]




A = [1, 60, -10, 70, -80, 85]
target = 0

print(two_sum_close_zero(A,target))