def diagonalOrder(arr, row, col):
     
    result = [[] for _ in range(row+col -1)]
    # even is insert , odd is append
    for r in range(row):
        for c in range(col):
            if (r + c) %2==0:
                result[r+c].insert(0,arr[r][c])
            else:
                result[r+c].append(arr[r][c])
    print(result)

    

# Driver Code
# we have a matrix of n rows
# and m columns
row = 3
col = 3
 
# Function call
#arr = [[1, 2, 3, 4],[ 5, 6, 7, 8],[9, 10, 11, 12 ],[13, 14, 15, 16 ],[ 17, 18, 19, 20]]
arr =[  [1,2,3],
        [4,5,6],
        [7,8,9]]
diagonalOrder(arr, row, col)