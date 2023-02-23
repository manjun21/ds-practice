
def binary_search_iterative(data, target):
    left = 0
    right = len(data) -1
    #print(left)
    #print(right)
    while left < right:
        mid = (right - left) //2
        #print(mid)
        if data[mid] > target:
            right = right -1
        else:
            left = left + 1
    
    return data[left]


#data = [1, 2, 4, 5, 6, 6, 8, 9]
#target = 11
data = [2, 5, 6, 7, 8, 8, 9]
target = 4
print(binary_search_iterative(data,target))