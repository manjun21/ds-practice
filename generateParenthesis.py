def generateParenthesis(n: int) -> list[str]:
    output = []
    def backtrack(left=0,right=0,S=[]):
        if len(S) == 2 * n:
            output.append("".join(S))
            return
        if left < n:
            S.append('(')
            backtrack(left +1,right,S)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(left,right +1,S)
            S.pop()
    
    backtrack()
    return output

n = 3
print(generateParenthesis(n))