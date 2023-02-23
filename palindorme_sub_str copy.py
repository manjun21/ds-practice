#Constraint: 0<=len(s)<=1000
#Given a string:
#1.) Take all prefixes of the string and choose the longest palindrome between them.
#2.) If chosen prefix has atleast two characters, cut this from s and go back to step 1 with the updated string. Otherwise, end the algo with the current string s.


def is_palindrome(s):
    return s == s[::-1]

def solution(s):
    prefixes = []
    for i in range(len(s)):
        prefixes.append(s[:i+1])
    print(prefixes)

    longest = None
    for prefix in prefixes:
        if is_palindrome(prefix):
            if longest:
                if len(prefix) > len(longest):
                    longest = prefix
            else:
                longest = prefix
    
    print('longest:'+str(longest))
 
    while longest:
        if len(longest)>=2:
            print('calling agin with:'+s[len(longest):])
            return solution(s[len(longest):])
        else:
            return s
    return s  
    

s1 = 'aaacodedoc'
#s2 = 'codesignal'
print(solution(s1))