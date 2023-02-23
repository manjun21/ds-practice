import math

# x +y = 0
# x = -y
def three_sum_close_zero(A,target):
    A.sort()
    minDiff = math.inf
    num1 = 0
    num2= 0
    num3 = 0
    for i in range(len(A)-2):
        left = i +1
        right = len(A) - 1
        while left< right:
            curr_sum = A[i] + A[left] + A[right]
            diff = abs(target - curr_sum)
            if (diff < minDiff):
                minDiff = diff
                num1 = A[i]
                num2 = A[left]
                num3 = A[right]
            elif (curr_sum < target):
                left = left +1
            elif (curr_sum > target):
                right = right - 1
    return num1 + num2 + num3
    


A = [-1,2,1,-4]
target = 1

# A = [0,0,0]
# target = 1

print(three_sum_close_zero(A,target))