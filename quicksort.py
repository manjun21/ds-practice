

def QuickSort(arr):

    if len(arr) < 2:
        return arr
        
    current_index = 0
    for i in range(1,len(arr)):
        if arr[i] <= arr[0]:
            current_index = current_index +1
            temp = arr[i]
            arr[i] = arr[current_index]
            arr[current_index] = temp
    print(arr)
    temp = arr[0]
    arr[0] = arr[current_index]
    arr[current_index] = temp

    left= QuickSort(arr[0:current_index])
    right = QuickSort(arr[current_index+1:len(arr)])

    return left + [arr [current_index]] + right

array_to_be_sorted = [4,2,7,3,1,6]
print(QuickSort(array_to_be_sorted))