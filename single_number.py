


def singleNumber(nums) -> int:

    m = {}

    for i in range(len(nums)):
        if nums[i] in m:
            m[nums[i]] = m[nums[i]] + 1
        else:
            m[nums[i]] = 1

    print(m)
    for k,v in enumerate(m):
        if v == 1:
            return k

nums = [2,2,1]
#Output: 1

print(singleNumber(nums))