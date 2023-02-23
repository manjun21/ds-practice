
#https://leetcode.com/problems/spiral-matrix-ii/
def spiralMatrixPrint(n):

    row = n
    col = n
    top = 0
    bottom = row -1
    left= 0
    right = col -1
    arr = [[0 for _ in range(n)] for _ in range(n)]
    num =1
    dir = 0
    print(arr)
    while (top <=bottom and left <= right):
        if dir == 0:    
            for i in range(left,right+1): # moving from left > right
                arr[top][i] = num
                num = num +1
            top = top +1
            dir = 1
        elif dir == 1:
            for i in range(top,bottom +1): # moving from top > bottom 
                #print(arr[i][right],end=" ")
                arr[i][right] = num
                num = num +1
            right = right -1
            dir = 2
        elif dir == 2:
            for i in range(right,left -1,-1): # moving from right > left
                #print(arr[bottom][i], end =" ")
                arr[bottom][i] = num
                num = num +1
            bottom = bottom -1
            dir =3
        elif dir == 3:
            for i in range(bottom,top -1,-1): # moving from right > left
                #print(arr[i][left], end =" ")
                arr[i][left] = num
                num = num +1
            left = left +1
            dir =0

    return arr
        


print(spiralMatrixPrint(3))