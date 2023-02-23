#https://leetcode.com/problems/toeplitz-matrix/
def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
    row = len(matrix)
    col = len(matrix[0])
    print(row)
    print(col)
    for i in range(row-1):
        for j in range(col-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                print(i)
                print(j)
                return False
            
    return True


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
isToeplitzMatrix(matrix)