

def removeDuplicates(nums) -> int:
    for i in range(len(nums)-1):
        j = i + 1
        while j < len(nums)-1 :
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                j = j +1

    return len(nums)




nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))