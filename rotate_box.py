

def rotateTheBox(box: list[list[str]]) -> list[list[str]]:
        for row in box:
            move_position = len(row) - 1             # initialize with the last position in row
            for j in range(len(row) - 1, -1, -1):    # iterate from the end of the row
                if row[j] == "*":                    # we cannot move stones behind obstacles,
                    move_position = j - 1            # so update move position to the first before obstacle
                elif row[j] == "#":                  # if stone, move it to the "move_position"
                    row[move_position], row[j] = row[j], row[move_position]
                    move_position -= 1
        #print(*box[::-1])
        return zip(*box[::-1])

def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    if i+1 < m and j+1 < n:
         adjacent_indices.append((i+1,j+1))
    if i-1 < m and j+1 > 0:
         adjacent_indices.append((i-1,j+1))
         
    if i-1 > 0 and j-1 > 0:
         adjacent_indices.append((i-1,j-1)) 
    if i+1 < m and j-1 > 0:
         adjacent_indices.append((i+1,j-1))
    
    
    return adjacent_indices

box = [ ["1","2","3","4"],
        ["5","6","7","8"],
        ["9","10","11","12"]
    ]
# r = 3
# c = 0
# up = box[r-1][c]
# down = box[r+1][c]
# right = box[r][c+1]
# left = box[r][c-1] 
# dig1 = box[r+1][c+1]
# dig2 = box[r-1][c-1]
# dig3 = box[r-1][c+1]
# dig4 = box[r+1][c-1]
# print(up)
# print(down)
# print(right)
# print(left)
# print(dig1)
# print(dig2)
# print(dig3)
# print(dig4)
print('----')
r = get_adjacent_indices(1,1,3,4)
for i,j in r:
    print(box[i][j])

#print(box)
# r = rotateTheBox(box)
# for i in r:
#     print(i)