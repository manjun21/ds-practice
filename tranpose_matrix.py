#https://leetcode.com/problems/transpose-matrix/
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(i+1,col):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(transpose(matrix))

1,2,3
4,5,6
7,8,9

1,4,7
2,5,8
3,6,9