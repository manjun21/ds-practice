def find_LRS_length(s):
    dp = [ [-1 for _ in range(len(s))] for _ in range(len(s))]
    return find_LRS_length_recursive(dp,s,0,0)

def find_LRS_length_recursive(dp,s,i1,i2):

    if i1== len(s) or i2 == len(s):
        return 0
    
    if dp[i1][i2] == -1:
        if i1!=i2 and s[i1] == s[i2] :
            dp[i1][i2] =  1 + find_LRS_length_recursive(dp,s,i1+1,i2+1)
        else:
            c1 = find_LRS_length_recursive(dp,s,i1,i2+1)
            c2 = find_LRS_length_recursive(dp,s,i1+1,i2)
            dp[i1][i2] = max(c1,c2)
    
    return dp[i1][i2]

print(find_LRS_length("tomorrow"))
print(find_LRS_length("aabdbcec"))
print(find_LRS_length("fmff")) 