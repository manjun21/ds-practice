
def twoSum(nums, target) -> list:   
    
    
    m = {}
    for i in range(len(nums)):
        if nums[i] in m:
            m[nums[i]] = m[nums[i]] +1
        else:
            m[nums[i]] = i
    
    
    nums.sort()
    left = 0
    right = len(nums) - 1
    output = []
    while left < right:
        sums = nums[left] + nums[right]
        diff = target - sums
        if diff == 0:
            output.append(nums[left])
            output.append(nums[right])
            break
        elif diff > 0:
            left = left +1  
        else:
            right = right - 1
    
    print(output)
    return [m[output[0]],m[output[1]]]

nums = [7,11,2,15]
7,8,11,15
target = 22

print(twoSum(nums,target))

