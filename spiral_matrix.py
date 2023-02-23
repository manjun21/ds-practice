
# #https://leetcode.com/problems/spiral-matrix/

# def spiralMatrixPrint(row,col,arr):

#     top = 0
#     bottom = row -1
#     left= 0
#     right = col -1

#     dir = 0
#     output = []
#     while (top <=bottom and left <= right):

#         if dir == 0:
#             for i in range(left,right +1):
#                 output.append(arr[top][i])
#             dir = 1
#             top = top +1
#         elif dir == 1:
#             for i in range(top,bottom +1 ):
#                 output.append(arr[i][right])
#             dir = 2
#             right = right -1
#         elif dir ==2:
#             for i in range(right,left -1, -1 ):
#                 output.append(arr[bottom][i])
#             dir = 3
#             bottom = bottom - 1
#         elif dir ==3:

            


# array = [[1,2,3,4],
#      [12,13,14,5],
#      [11,16,15,6],
#      [10,9,8,7]]

# for row in array:
#     print(row)
#     row[0] = 0
# print(array)

# for r in range(len(array)):
#     for c in range(len(array[0])):
           
# print(array)

# spiralMatrixPrint(4, 4, array)

# s = "abcd"

# for i in range(3,-1,-1):
#     print(s[i])