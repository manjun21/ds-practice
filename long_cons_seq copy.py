#https://leetcode.com/problems/longest-consecutive-sequence/
#https://www.geeksforgeeks.org/longest-consecutive-subsequence/
#https://atharayil.medium.com/longest-consecutive-sequence-day-29-python-aa170b1a8cc0

def longestConsecutive(nums: list[int]) -> int:
    s = set(nums)
    count = 0
    for x in nums:
        if x-1 not in s:
            y = x +1
            while y in s:
                y = y +1
            count = max(count,y-x)
    return count
    
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))