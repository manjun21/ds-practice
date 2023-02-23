#https://leetcode.com/problems/reshape-the-matrix/
def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    row = len(mat)
    col = len(mat[0])
    if row*col != r*c:
        return mat

    # flatten out
    temp = []
    for i in range(row):
        for j in range(col):
            temp.append(mat[i][j])
    
    output = [[0 for _ in range(c)] for _ in range(r)]
    k =0
    for i in range(r):
        for j in range(c):
            output[i][j] = temp[k]
            k = k +1
    output

mat = [[1,2],[3,4],[5,6]]
r = 2
c = 3

matrixReshape(mat,r,c)