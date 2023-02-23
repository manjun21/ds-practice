import math

# x +y = 0
# x = -y
def two_sum_less_than_k(A,target):
    A.sort()
    left = 0
    right = len(A) - 1
    max_sum = -1
    while left< right:
        curr_sum = A[left] + A[right]
        if curr_sum == target:
            max_sum= A[left] + A[right]
            break
        elif curr_sum < target:
            curr_max_sum = A[left] + A[right]
            max_sum = max(max_sum, curr_max_sum)
            left = left +1 
        else :
            right = right -1
    return max_sum
        
# nums = [1, 2, 3, 4, 5]
# target = 10
# print(two_sum_close_zero(nums,target))
#Output: [4, 5]




#A = [34,23,1,24,75,33,54,8]
#target = 60

A = [10,20,30] 
target = 15

print(two_sum_less_than_k(A,target))