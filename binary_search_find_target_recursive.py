
def binary_search_iterative(data, target,left,right):
    
    if left > right:
        return left

    while left <= right:
        mid = right - left //2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            return binary_search_iterative(data,target,left,mid-1)
        else:
            return binary_search_iterative(data,target,mid+1,right)
    return left

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37

print(binary_search_iterative(data,target,0,len(data)-1))