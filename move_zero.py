def moveZeroes(nums) -> None:

    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))

    print(nums)


nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

moveZeroes(nums)