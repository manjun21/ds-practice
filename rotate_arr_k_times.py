
def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    for _ in range(-1,k-1):
        #print(i)
        n = nums.pop()
        #print(n)
        nums.insert(0,n)

    print(nums)

nums = [1,2,3,4,5,6,7]
k = 3
#Output: [5,6,7,1,2,3,4]
rotate(nums,k)