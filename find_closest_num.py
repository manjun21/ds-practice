import math

def find_closest_num(A, target):
    left = 0 
    right = len(A) -1
    min_diff_left= math.inf
    min_diff_right = math.inf
    min_diff = math.inf

    closest_num = math.inf

    while left < right:
        mid = left + right //2

        if mid +1 < len(A):
            min_diff_right = abs(target- A[mid+1])
        if mid > 0:
            min_diff_left = abs(target- A[mid -1])

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
            print('closest_num left'+str(closest_num))

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]
            print('closest_num right'+str(closest_num))
        

        if A[mid] < target:
            left = mid +1
        elif A[mid] > target:
            right = mid -1
        else:
            return A[mid]

    return closest_num




A1 = [2,5,6,7,8,8,9]
print(find_closest_num(A1, 4))