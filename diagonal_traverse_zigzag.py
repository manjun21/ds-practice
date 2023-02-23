#https://leetcode.com/problems/diagonal-traverse/
def diagonalOrder(arr, row, col):
     
    # we will use a 2D vector to
    # store the diagonals of our array
    # the 2D vector will have (n+m-1)
    # rows that is equal to the number of
    # diagonals
    ans = [[] for i in range(row +col - 1)]
    print(ans)
    for i in range(row):
        for j in range(col):
            if (i + j)%2 == 0:
                ans[i + j].insert(0,arr[i][j])     
            else:
                ans[i + j].append(arr[i][j])
    print(ans)
    output = []
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j])
            output.append(ans[i][j])

    return output
 
# Driver Code
# we have a matrix of n rows
# and m columns
row = 3
col = 3
 
# Function call
#arr = [[1, 2, 3, 4],[ 5, 6, 7, 8],[9, 10, 11, 12 ],[13, 14, 15, 16 ],[ 17, 18, 19, 20]]
arr =[[1,2,3],
      [4,5,6],
      [7,8,9]]
diagonalOrder(arr, row, col)