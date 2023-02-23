# # # # n = 4562
# # # # rev = 0
 
# # # # while(n > 0):
# # # #     r = n % 10
# # # #     rev = rev * 10 + r
# # # #     n = n // 10
 
# # # # print(rev)

# # # # n = 100
# # # # rev = 0
# # # # while n > 0:
# # # #     r = n % 10
# # # #     rev = rev * 10 + r
# # # #     n = n //10
# # # # print(rev)

# # # import math

# # # n = 29
# # # print(math.log(n,3))

# # # def check_number_power_of_three(n):
# # #     if n <= 0:
# # #         return False
# # #     if n % 3 == 0:
# # #         d = n //3
# # #         return check_number_power_of_three(d)
# # #     if n == 1:
# # #         return True
# # #     return False

# # # print(check_number_power_of_three(n))


# # # m ={
# # #     1:2,
# # #     2:3
# # # }
# # # for k in m.keys():
# # #     m[k] = m[k] +1

# # # print(m)

# # nums1 = [1,0]
# # print(nums1[len(nums1)-1])
# # print(len(nums1)-1)
# # print(nums1[-1])
# # nums1.pop(len(nums1)-1)
# # print('after pop')
# # print(nums1)
    
# #  [-2,1,-3,4,-1,2,1,-5,4]
# # -2 = 0 (index 0)
# # -2,1 = 1 (index 0 + index1)
# # -2,1,-3 = 2 (index 0 + index1 + index2)
# # -2,1,-3,4 = 3 (index 0 + index1 + index2 +index3)
# # -2,1,-3,4,-1 = 4
# # -2,1,-3,4,-1,2 = 5
# # -2,1,-3,4,-1,2,1 = 6
# # -2,1,-3,4,-1,2,1,-5 = 7
# # -2,1,-3,4,-1,2,1,-5,4 = 8


# 1
# # -1,-3
# # -1,-3,4
# # -1,-3,4,-1
# # -1,-3,4,-1,2
# # -1,-3,4,-1,2,1
# # -1,-3,4,-1,2,1,-5
# # -1,-3,4,-1,2,1,-5,4





# # 1
# # 1,-3
# # 1,-3,4


# # def maxSubArray(nums: list[int]) -> int: 
# #     mem = [0 for _ in range(len(nums))]
# #     print(len(nums))
# #     max_sum = 0
# #     for i in range(len(nums)):
# #         print('staring recur starting from :'+str(i))
# #         max_sum = maxRecursive(mem,nums,max_sum,i)
# #         print('end recur started from :'+str(i)+"with max val"+str(max_sum))
# #     return max_sum


# # def maxRecursive(mem,nums,max_sum,n):
        
# #     if n >= len(nums) :
# #         return 0
    
# #     val = 0
# #     if mem[n] != 0:
# #         val = mem[n]
# #     else:
# #         val = maxRecursive(mem,nums,max_sum,n+1)
# #     print(n)
    
# #     val2 = nums[n] + val 
# #     print('max_sum:'+str(val))
# #     print('val'+str(val2))
# #     if max_sum < val:
# #         print('printing n index'+str(n))
# #         max_sum = val
# #     print('after max_sum:'+str(max_sum))
# #     mem[n] = val
# #     return max_sum

# # input = [-2,1,-3,4,-1,2,1,-5,4]
# # #input = [5,4,-1,7,8]
# #print(maxSubArray(input))


# # comb = []
# # for j in range(len(input)):
# #     for i in range(len(input)):
# #         comb.append(input[j:i+1])
# # print(comb)

# # max_sum = 0
# # for c in comb:
# #     val = sum(c)
# #     if val > max_sum:
# #         max_sum = val

# # print(max_sum)

# # test_str = "abcde"
# # count = 0
# # for i in range(len(test_str)):
# #     print(test_str[i:3+count])
# #     count = count +1

# # def maxSubArray(A):
# #     if not A:
# #         return 0

# #     curSum = maxSum = A[0]
# #     for num in A[1:]:
# #         curSum = max(num, curSum + num)
# #         maxSum = max(maxSum, curSum)

# #     return maxSum

# # input = [5,4,-1,7,8]
# # print(maxSubArray(input))

# print(19//10)
# print(19%10)

# def get_next(n):
#             total_sum = 0
#             while n > 0:
#                 n, digit = divmod(n, 10)
#                 total_sum +=  digit ** 2
#                 print(total_sum)
#             return total_sum
    
# def isHappy(n: int) -> bool:

#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = get_next(n)

#     return n == 1

# isHappy(19)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

m = {}
for r in range(len(board)):
    for c in range(len(board[0])):
        if r-c in m:
            m[r-c] = m[r-c] + [board[r][c]]
        else:
            m[r-c] = [board[r][c]]

print(m)

m1 = {}

for r in range(len(board)-1,-1,-1):
    for c in range(len(board[0])-1,-1,-1):
        if r-c in m1:
            m1[r-c] = m1[r-c] + [board[r][c]]
        else:
            m1[r-c] = [board[r][c]]

print(m1)



def diagonalOrder(arr, row, col):
     
    result = [[] for _ in range(row+col -1)]
    # even is insert , odd is append
    count = 0
    for r in range(row):
        for c in range(col):
            if (r + c) %2==0:
                result[r+c].insert(0,arr[count])
            else:
                result[r+c].append(arr[count])
            count = count + 1
    print(result)

l2 = [-2,-2,1,1,4,4,3,3,3]

l1 = [
      [3, 3, 4],
      [3, 4, 1],
      [1,-2,-2]
    ]

row = 3
col = 3

diagonalOrder(list(reversed(l2)),row,col)