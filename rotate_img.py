#https://leetcode.com/problems/rotate-image/
def rotate(matrix: list[list[int]]) -> None:
    row = len(matrix)
    col = len(matrix[0])
    top = 0
    bottom = row - 1

    while top < bottom:
        matrix[top],matrix[bottom] = matrix[bottom],matrix[top]
        top = top +1
        bottom = bottom -1
    #print(matrix)
    print(row)
    print(col)
    for i in range(row):
        for j in range(i+1,col):
            print(i)
            print(j)
            print(matrix[i][j])
            print(matrix[j][i])
            print("---")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)

rotate([[1,2,3],[4,5,6],[7,8,9]])
#rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])