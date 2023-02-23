#https://www.educative.io/courses/grokking-the-coding-interview/gxk639mrr5r
def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        target_sum = -arr[i]
        left = i +1
        right= len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([-target_sum,arr[left],arr[right]])
                left = left +1
                right = right -1
            elif current_sum > target_sum:
                right = right -1
            else:
                left = left +1
    print(triplets)


    

search_triplets([0, -1, 2, -3, 1])
search_triplets([1, -2, 1, 0, 5])
