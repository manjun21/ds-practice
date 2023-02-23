#https://leetcode.com/problems/top-k-frequent-elements/
from heapq import *
def top_k_freq_elements(nums,k):

    freq_map= {}
    for i in range(len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]] = freq_map[nums[i]] + 1
        else:
            freq_map[nums[i]] = 1
    
    print(freq_map)
    max_heap =[]
    for n,f in freq_map.items():
        heappush(max_heap,(-f,n))
    print(max_heap)
    count = 0
    output = [] 
    while count < k:
        f,n = heappop(max_heap)
        output.append(n)
        count = count +1
    print(output)


nums = [1, 1, 1, 2, 2, 3]
k = 2

top_k_freq_elements(nums,k)
