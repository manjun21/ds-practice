#https://leetcode.com/problems/k-diff-pairs-in-an-array/
def findPairs(arr: list[int], k: int) -> int:
    count = 0
    n = len(arr)
     
    # Pick all elements one by one
    for i in range(0, n):
         
        # See if there is a pair of this picked element
        for j in range(i+1, n) :
             
            if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
                count += 1
                 
    return count

nums = [1,3,1,5,4]
k = 0
print(findPairs(nums,k))