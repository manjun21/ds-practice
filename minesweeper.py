  
    
def isValidIndx(self,i,j,m,n):
    if i >= 0 and i < m and j >= 0 and j < n:
        return True
    else:
        return False

def getVal(self,i,b):
    return b[i[0]][i[1]]


def getAdjstMinesPresent(self,adj,b):
    mcount = 0
    for i in adj:
        if b[i[0]][i[1]] == 'M':
            mcount = mcount +1
    return mcount,

def find_adj_elements(self,i,j,m,n):
    adj = []
    if self.isValidIndx(i-1,j-1,m,n):
        adj.append((i-1,j-1))
    if self.isValidIndx(i-1,j,m,n):
        adj.append((i-1,j))
    if self.isValidIndx(i-1,j+1,m,n):
        adj.append((i-1,j+1))
    if self.isValidIndx(i,j-1,m,n):
        adj.append((i,j-1))
    if self.isValidIndx(i,j+1,m,n):
        adj.append((i,j+1))
    if self.isValidIndx(i+1,j-1,m,n):
        adj.append((i+1,j-1))
    if self.isValidIndx(i+1,j,m,n):
        adj.append((i+1,j))
    if self.isValidIndx(i+1,j+1,m,n):
        adj.append((i+1,j+1))
    return adj



def updateBoardRecr(self,board: list[list[str]], click: list[int]) -> list[list[str]]:
    doneClicks = set()
    return self.updateBoard(board, click,doneClicks) 


def updateBoard(self,board: list[list[str]], click: list[int],doneClicks:set) -> list[list[str]]:
    clickVal = board[click[0]][click[1]]
    c = str(click[0])+"-"+str(click[1])
    if c in doneClicks:
        return board
    
    if clickVal == 'M':
        board[click[0]][click[1]] = 'X'
        return board
    
    r = len(board)
    c = len(board[0])
    adj = self.find_adj_elements(click[0],click[1],r,c)
    adjstMines = self.getAdjstMinesPresent(adj,board)
    
    doneClicks.add(str(click[0])+"-"+str(click[1]))
    
    if clickVal == 'E' and adjstMines > 0:
        board[click[0]][click[1]] = str(adjstMines)
    else:
        board[click[0]][click[1]] = 'B'
        for a in adj:
            board = self.updateBoard(board,[a[0],a[1]],doneClicks)    
    return board


#board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
board1 = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
#click = [3,0]
click1 = [1,2]

print(updateBoardRecr(board1,click1))


            