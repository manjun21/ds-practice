from heapq import *

def find_k_largest_numbers(nums,k):

    
    # for i in range(k):
    #     heappush(mini_heap,nums[i])

    # print(mini_heap)
    # for i in range(k,len(nums)):
    #     if nums[i] > mini_heap[0]:
    #         print('----')
    #         print(mini_heap)
    #         heappop(mini_heap)
    #         print(mini_heap)
    #         heappush(mini_heap,nums[i])
    #         print(mini_heap)
    #         print('----')
    mini_heap = []
    for n in nums:
        heappush(mini_heap, n)
    
    print(mini_heap)
    output = []
    count = 0 
    while count < k:
        output.append(heappop(mini_heap))
        count = count +1
    
    print(output)

    max_heap = []
    for n in nums:
        heappush(max_heap, -n)
    
    print(max_heap)
    output = []
    count = 0 
    while count < k:
        output.append(-heappop(max_heap))
        count = count +1
    print(output)
    

def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

main()