def lcs_length(s1,s2):
        mem = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
        return lcs_recursive(mem,s1,s2,0,0)
    
def lcs_recursive(mem,s1,s2,i1,i2):
    if i1 >= len(s1) or i2 >= len(s2):
        return 0
    
    if mem[i1][i2] != -1:
        return mem[i1][i2]
    
    if s1[i1] == s2[i2]:
        mem[i1][i2] = 1 + lcs_recursive(mem,s1,s2,i1+1,i2+1)
    else:
        d1 = lcs_recursive(mem,s1,s2,i1,i2+1)
        d2 = lcs_recursive(mem,s1,s2,i1+1,i2)
        mem[i1][i2] = max(d1,d2)
    return mem[i1][i2]
    
text1 = "abcde"
text2 = "ace" 
print(lcs_length(text1,text2))