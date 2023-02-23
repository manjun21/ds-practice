def dfs(board,word,r,c,ci):
    
    if ci == len(word):
        return True
    
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
        return False
    if board[r][c] != word[ci]:
        return False
    
    curr = board[r][c]
    board[r][c] = '#'
    a1 = dfs(board,word,r+1,c,ci+1)
    a2 = dfs(board,word,r,c+1,ci+1)
    a3 = dfs(board,word,r-1,c,ci+1)
    a4 = dfs(board,word,r,c-1,ci+1)
    board[r][c] = curr

    return a1 or a2 or a3 or a4


def exist(board: list[list[str]], word: str) -> bool:
    row = len(board)
    col = len(board[0])
    for r in range(row):
        for c in range(col):
            if board[r][c] == word[0] and dfs(board,word,r,c,0):
                return True
            
    
    return False

def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    search_result = exist(board,word)
    print(search_result)


if __name__ == "__main__":
    main()